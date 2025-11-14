import { system } from "@minecraft/server";
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
    }
    async send(action, hasResult = false) {
        return new Promise((resolve) => {
            const id = this.generateId();
            if (!hasResult) {
                resolve(null);
            }
        });
    }
}
export default new ScriptSDK();
