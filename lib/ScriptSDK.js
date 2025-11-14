import { system, world } from "@minecraft/server";
export class NotFoundException extends Error {
    constructor(msg) {
        super(msg);
        this.name = 'NotFoundException';
    }
}
class ScriptSDK {
    constructor() {
        this.waitingData = {};
        system.afterEvents.scriptEventReceive.subscribe((e) => this.event(e));
    }
    generateId(length = 10) {
        var result = '';
        var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var charactersLength = characters.length;
        for (var i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }
    event(e) {
        const { id, message, sourceEntity, sourceType } = e;
        const [message_type, message_id] = id.split(':');
        if (message_type == 'scriptsdkresult') {
            if (Object.keys(this.waitingData).includes(message_id)) {
                this.waitingData[message_id](message);
                delete this.waitingData[message_id];
            }
        }
    }
    async send(action, body = '', hasResult = false) {
        return new Promise((resolve) => {
            const id = this.generateId();
            world.getDimension('overworld').runCommand(`scriptevent scriptsdk:${id}-${action} ${body}`);
            if (!hasResult) {
                resolve(null);
            }
            this.waitingData[id] = (data) => {
                const result = data.split('#');
                if (result.length == 3) {
                    resolve({
                        success: result[0] == 'true',
                        code: parseInt(result[1]),
                        result: result[2]
                    });
                }
            };
        });
    }
    /**
     * Return player ip.
     */
    async getIp(playerName) {
        const result = await this.send('getIp', playerName, true);
        if (result?.success) {
            return result.result;
        }
        if (result?.code == 404)
            throw new NotFoundException(result?.result);
        throw new Error(result?.result);
    }
}
export default new ScriptSDK();
