export type WaitingData = {
    [key: string]: (result: any) => void;
};
declare class ScriptSDK {
    private waitingData;
    constructor();
    private generateId;
    private event;
    private send;
}
declare const _default: ScriptSDK;
export default _default;
