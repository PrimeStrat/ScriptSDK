export type WaitingData = {
    [key: string]: (result: any) => void;
};
export type actions = 'getIp';
export declare class NotFoundException extends Error {
    constructor(msg: string);
}
declare class ScriptSDK {
    private waitingData;
    constructor();
    private generateId;
    private event;
    private send;
    /**
     * Return player ip.
     */
    getIp(playerName: string): Promise<string>;
}
declare const _default: ScriptSDK;
export default _default;
