export type Nullable<T> = T | null;

export type Message = {
  role: "user" | "assistant";
  content: string;
};

export type UseFetchResult = {
  loading: boolean;
  error: Nullable<string>;
  data: any;
  refetch: (payload?: BodyInit) => void;
};

export type UseFetchOptions = RequestInit & {
  lazy?: boolean;
};
