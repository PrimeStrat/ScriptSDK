import { test } from "./type";

class ScriptSDK {
    constructor() {}

    test() : test {
        return {
            value: 'test'
        };
    }
}

export default new ScriptSDK();