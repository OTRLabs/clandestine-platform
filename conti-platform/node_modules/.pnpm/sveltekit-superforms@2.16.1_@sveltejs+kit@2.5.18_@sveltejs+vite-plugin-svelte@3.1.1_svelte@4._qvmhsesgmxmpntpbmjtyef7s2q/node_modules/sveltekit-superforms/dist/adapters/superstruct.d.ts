import { type ValidationAdapter, type ClientValidationAdapter, type RequiredDefaultsOptions, type Infer } from './adapters.js';
import type { Struct } from 'superstruct';
type StructObject<T extends Record<string, unknown>> = Struct<T, any>;
export declare const superstruct: <T extends StructObject<Infer<T>>>(schema: T, options: RequiredDefaultsOptions<Infer<T>>) => ValidationAdapter<Infer<T>>;
export declare const superstructClient: <T extends StructObject<Infer<T>>>(schema: T) => ClientValidationAdapter<Infer<T>>;
export {};
