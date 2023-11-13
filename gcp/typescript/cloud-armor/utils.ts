import { PREFIX } from "./config";

export class Utils {
    static resourceName(baseName: string): string {
        return `${PREFIX}-${baseName}`;
    }
}

