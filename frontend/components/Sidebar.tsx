"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

import { MessageResponse } from "@/types/chat";

interface SidebarProps {
  historique?: MessageResponse[];
  onSelectChat?: (chat: MessageResponse) => void;
}

export default function Sidebar({
  historique = [],
  onSelectChat,
}: SidebarProps) {

  const router = useRouter();

  function handleLogout() {
    localStorage.removeItem("access_token");
    router.push("/login");
  }

  return (
    <aside className="w-64 min-h-[calc(100vh-4rem)] bg-gray-900 text-white p-4">

      <nav className="space-y-2">

        <Link
          href="/dashboard"
          className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
          <span>🏠</span>
          <span>Dashboard</span>
        </Link>

        <Link
          href="/chat"
          className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
          <span>💬</span>
          <span>Assistant</span>
        </Link>

        <Link
          href="/documents"
          className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
          <span>📚</span>
          <span>Documents</span>
        </Link>

<div className="pt-2">

  <Link
    href="/chat"
    className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
  >
    <span>🕘</span>
    <span>Historique</span>
  </Link>


  <div className="max-h-80 overflow-y-auto">

    {historique.length === 0 ? (

      <p className="px-4 py-2 text-sm text-gray-500">
        Aucun historique
      </p>

    ) : (

      historique.map((chat) => (

        <button
          key={chat.id}
          onClick={() => {

            if (onSelectChat) {
              onSelectChat(chat);
            }

          }}
          className="w-full text-left px-4 py-2 rounded-lg hover:bg-gray-800"
        >

          <p className="text-sm text-gray-300 truncate">
            {chat.question}
          </p>

          <p className="text-xs text-gray-500 mt-1">
            {new Date(
              chat.date_creation
            ).toLocaleDateString("fr-FR")}
          </p>

        </button>

      ))

    )}

  </div>

</div>

        <Link
  href="/documents"
  className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
>
  <span>📚</span>
  <span>Documents</span>
</Link>

      </nav>

    </aside>
  );
}