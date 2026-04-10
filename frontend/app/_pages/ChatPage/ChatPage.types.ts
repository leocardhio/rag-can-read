import { Message, UseFetchResult } from "@/types";

export type UseStates = UseFetchResult & {
  messages: Message[];
  setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
  input: string;
  setInput: React.Dispatch<React.SetStateAction<string>>;
}