"use client";

import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import Message from "@/components/Message";
import Loading from "@/components/Loading";

import {Message as MessageType,MessageResponse,} from "@/types/chat";

import { poserQuestion } from "@/services/chatService";


interface ChatBoxProps {
  chatSelectionne: MessageResponse | null;
}


export default function ChatBox({
  chatSelectionne,
}: ChatBoxProps) {

  const [question, setQuestion] = useState("");

  const [messages, setMessages] =
    useState<MessageType[]>([]);

  const [loading, setLoading] =
    useState(false);

  const [erreur, setErreur] =
    useState("");


  useEffect(() => {

    if (!chatSelectionne) {
      return;
    }

    const messagesHistorique: MessageType[] = [

      {
        id: chatSelectionne.id,
        role: "user",
        contenu: chatSelectionne.question,
      },

      {
        id: chatSelectionne.id + 1,
        role: "assistant",
        contenu: chatSelectionne.reponse,
      },

    ];

    setMessages(messagesHistorique);

    setErreur("");

  }, [chatSelectionne]);


  async function handleSubmit(
    e: FormEvent
  ) {

    e.preventDefault();

    if (!question.trim()) {
      return;
    }

    setErreur("");

    const questionUtilisateur =
      question.trim();

    const messageUtilisateur: MessageType = {
      id: Date.now(),
      role: "user",
      contenu: questionUtilisateur,
    };

    setMessages((messages) => [
      ...messages,
      messageUtilisateur,
    ]);

    setQuestion("");

    setLoading(true);

    try {

      const resultat =
        await poserQuestion(
          questionUtilisateur
        );

      console.log(
        "RÉPONSE BACKEND :",
        resultat
      );

      console.log(
        "RÉPONSE RAG :",
        resultat.reponse
      );

      const messageAssistant: MessageType = {

        id: Date.now() + 1,

        role: "assistant",

        contenu: resultat.reponse,

      };

      setMessages((messages) => [
        ...messages,
        messageAssistant,
      ]);

    } catch (error) {

      console.error(error);

      if (error instanceof Error) {

        setErreur(error.message);

      } else {

        setErreur(
          "Une erreur est survenue."
        );

      }

    } finally {

      setLoading(false);

    }

  }


  return (

    <div className="bg-white border border-slate-200 rounded-xl shadow-sm flex flex-col h-[calc(100vh-10rem)]">

      <div className="flex-1 overflow-y-auto p-6 bg-slate-50">
        {messages.length === 0 && (

          <div className="h-full flex flex-col items-center justify-center text-center">

            <div className="w-16 h-16 flex items-center justify-center rounded-full bg-blue-50 text-4xl mb-4">
              🤖
            </div>

            <h2 className="text-2xl font-semibold text-slate-800">
              Assistant intelligent
            </h2>

            <p className="text-slate-500 mt-2 max-w-md">
              Interrogez l’assistant pour obtenir des réponses pertinentes à partir des documents de référence.
            </p>

          </div>

        )}


        {messages.map((message) => (

          <Message
            key={message.id}
            message={message}
          />

        ))}


        {loading && <Loading />}
        {erreur && (

          <div className="mt-4 bg-red-50 border border-red-200 text-red-600 p-3 rounded-lg">

            {erreur}

          </div>

        )}

      </div>

      <form
        onSubmit={handleSubmit}
        className="border-t border-slate-200 bg-white p-4 flex gap-3"
      >

        <input
          type="text"
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          placeholder="Posez votre question..."
          disabled={loading}
          className="flex-1 border border-slate-200 rounded-xl px-4 py-3 text-slate-800 placeholder-slate-400 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 disabled:bg-slate-100"
        />


        <button
          type="submit"
          disabled={
            loading ||
            !question.trim()
          }
          className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700 transition disabled:bg-slate-300 disabled:cursor-not-allowed"
        >

          {loading
            ? "..."
            : "➤"}

        </button>

      </form>

    </div>

  );
}