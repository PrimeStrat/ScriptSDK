import { ScriptEventCommandMessageAfterEvent, system } from "@minecraft/server";

export type WaitingData = {
    [key: string]: (result: any) => void;
}

class ScriptSDK {

    private waitingData : WaitingData = {};

    constructor() {
        system.afterEvents.scriptEventReceive.subscribe((e) => this.event(e))
    }

    private generateId(length = 10) : string {
        var result = '';
        var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var charactersLength = characters.length;
        for (var i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }

    private event(e : ScriptEventCommandMessageAfterEvent) {
        const { id, message, sourceEntity, sourceType } = e;
    }

    private async send(action : string, hasResult : boolean = false) {
        return new Promise((resolve) => {

            const id = this.generateId();

            if(!hasResult) {
                resolve(null);  
            }
        });
    }
}

export default new ScriptSDK();