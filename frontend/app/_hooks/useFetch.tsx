"use client";

import { Nullable, UseFetchOptions, UseFetchResult } from "@/types";
import { useEffect, useState } from "react";

export default (url: string, options: UseFetchOptions): UseFetchResult => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<Nullable<string>>(null);
  const [data, setData] = useState<any>({});

  const fetchData = async (payload?: BodyInit): Promise<void> => {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(url, {
        ...options,
        body: payload || options.body,
      });
      const json = await res.json();

      if (!res.ok) {
        throw new Error(json.message || "Something went wrong");
      }

      setData(json);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  if (!options.lazy) {
    useEffect(() => {
      fetchData();
    }, []);
  }

  return { loading, error, data, refetch: fetchData };
};
