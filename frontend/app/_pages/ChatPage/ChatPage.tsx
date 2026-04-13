"use client";

import { JSX, useState } from "react";

import { DEFAULT_ABORT_TIMEOUT, ROLES } from "@/constants";
import type { Message, UseFetchOptions, UseFetchResult } from "@/types";

import { useFetch } from "../../_hooks";
import { UseStates } from "./ChatPage.types";

const _useStates = (fetchStates: UseFetchResult): UseStates => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  return { messages, setMessages, input, setInput, ...fetchStates };
};

const _getFetchOptions = (): UseFetchOptions => ({
  method: "POST",
  headers: { "Content-Type": "application/json" },
  signal: AbortSignal.timeout(DEFAULT_ABORT_TIMEOUT),
  lazy: true,
});

const _sendMessage = (states: UseStates) => {
  const {
    input,
    setInput,
    setMessages,
    loading,
    data,
    refetch: postMessage,
  } = states;

  if (!input.trim() || loading) return;

  const userMessage: Message = { role: ROLES.USER, content: input };
  const messageToSend = input;

  setMessages((prev) => [...prev, userMessage]);
  setInput("");

  postMessage(JSON.stringify({ message: messageToSend }));
};

const _isNewResponse = (
  content: string | undefined,
  messages: Message[],
): boolean => {
  if (!content) return false;

  const lastMessage = messages
    .filter((message) => message.role === ROLES.ASSISTANT)
    .slice(-1)[0];
  return content !== lastMessage?.content;
};

const _updateMessages = (content: string, states: UseStates) => {
  const { messages, setMessages } = states;
  if (!_isNewResponse(content, messages)) return;

  const assistantMessage: Message = {
    role: ROLES.ASSISTANT,
    content,
  };

  setMessages((prev) => [...prev, assistantMessage]);
};

const _handleEnterKey =
  (states: UseStates) => (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      event.preventDefault();
      _sendMessage(states);
    }
  };

const _handleOnChange =
  (setInput: React.Dispatch<React.SetStateAction<string>>) =>
  (event: React.ChangeEvent<HTMLInputElement>) => {
    setInput(event.target.value);
  };

const _handleClickSubmit = (states: UseStates) => () => {
  _sendMessage(states);
};

const _shouldRenderLoadingBubble = (
  loading: boolean,
  messages: Message[],
): boolean => {
  if (!loading) return false;

  const lastMessage = messages.slice(-1)[0];
  return lastMessage?.role !== ROLES.ASSISTANT;
};

const _renderLoadingBubble = (): JSX.Element => (
  <div className="p-3 rounded-lg max-w-xs bg-gray-200 text-black ml-auto animate-pulse">
    ...
  </div>
);

const _renderMessages = (states: UseStates): JSX.Element => (
  <div className="flex-1 overflow-y-auto space-y-3 mb-4">
    {states.messages.map((msg, index) => (
      <div
        key={index}
        className={`p-3 rounded-lg max-w-xs ${
          msg.role === ROLES.USER
            ? "bg-blue-500 text-white ml-auto"
            : "bg-gray-200 text-black"
        }`}
      >
        {msg.content}
      </div>
    ))}
    {_shouldRenderLoadingBubble(states.loading, states.messages) &&
      _renderLoadingBubble()}
  </div>
);

const _renderInput = (states: UseStates): JSX.Element => (
  <div className="flex gap-2">
    <input
      type="text"
      value={states.input}
      onChange={_handleOnChange(states.setInput)}
      onKeyDown={_handleEnterKey(states)}
      placeholder="Type your message..."
      className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
    />
    <button
      onClick={_handleClickSubmit(states)}
      disabled={states.loading}
      className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 disabled:opacity-50"
    >
      {states.loading ? "..." : "Send"}
    </button>
  </div>
);

const _renderError = (error: string): JSX.Element => (
  <div className="flex bg-red-100 text-red-700 py-3 px-12 rounded-lg absolute top-24 left-1/2 transform -translate-x-1/2">
    {error}
  </div>
);

export default function ChatPage(): JSX.Element {
  const fetchResult: UseFetchResult = useFetch(
    `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/chat`,
    _getFetchOptions(),
  );
  const states = _useStates(fetchResult);
  const { error } = states;

  _updateMessages(states.data?.response, states);

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto p-4">
      {_renderMessages(states)}
      {_renderInput(states)}
      {error && _renderError(states.error!)}
    </div>
  );
}
