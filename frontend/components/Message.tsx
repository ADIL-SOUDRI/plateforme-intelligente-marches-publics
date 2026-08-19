"use client";

import { Message as MessageType } from "@/types/chat";

interface MessageProps {
  message: MessageType;
}

export default function Message({ message }: MessageProps) {
  const isUser = message.role === "user";

  return (
    <div
      className={`flex mb-4 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-[75%] rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-100 text-gray-800"
        }`}
      >
        <p className="text-sm font-medium mb-1">
          {isUser ? "Vous" : "Assistant"}
        </p>

        <p className="whitespace-pre-wrap">
          {message.contenu}
        </p>
      </div>
    </div>
  );
}