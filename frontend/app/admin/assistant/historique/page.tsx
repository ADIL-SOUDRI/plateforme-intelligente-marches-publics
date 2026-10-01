"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import AdminNavbar from "@/components/admin/AdminNavbar";
import AdminSidebar from "@/components/admin/AdminSidebar";

import { getCurrentAdmin } from "@/services/adminService";
import {getHistoriqueAdmin,getChat,} from "@/services/chatService";

import { MessageResponse } from "@/types/chat";


export default function AdminHistoriquePage() {

  const router = useRouter();

  const [admin, setAdmin] = useState<any>(null);

  const [historique, setHistorique] =
    useState<MessageResponse[]>([]);

  const [chatSelectionne, setChatSelectionne] =
    useState<MessageResponse | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [loadingChat, setLoadingChat] =
    useState(false);


  useEffect(() => {

    async function chargerHistorique() {

      const token =
        localStorage.getItem("access_token");

      if (!token) {
        router.replace("/admin/login");
        return;
      }

      try {
        const adminConnecte =
          await getCurrentAdmin();

        setAdmin(adminConnecte);

        const historiqueAdmin =
          await getHistoriqueAdmin(
            adminConnecte.id_admin
          );

        setHistorique(
          historiqueAdmin
        );

      } catch (error) {

        console.error(
          "Erreur historique admin :",
          error
        );

        localStorage.removeItem(
          "access_token"
        );

        document.cookie =
          "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

        router.replace("/admin/login");

      } finally {

        setLoading(false);

      }

    }

    chargerHistorique();

  }, [router]);

  async function handleSelectChat(
    chat: MessageResponse
  ) {

    try {

      setLoadingChat(true);

      const chatComplet =
        await getChat(chat.id);

      setChatSelectionne(
        chatComplet
      );

    } catch (error) {

      console.error(
        "Erreur récupération conversation :",
        error
      );

    } finally {

      setLoadingChat(false);
    }
  }


  if (loading) {

    return (
      <main className="min-h-screen flex items-center justify-center bg-gray-50">

        <p className="text-gray-600">
          Chargement de l'historique...
        </p>

      </main>
    );

  }


  if (!admin) {
    return null;
  }


  return (

    <div className="min-h-screen bg-gray-100">


      <AdminNavbar
        nomAdmin={`${admin.prenom} ${admin.nom}`}
        email={admin.email}
      />


      <div className="flex">


        <AdminSidebar />


        <main className="flex-1 p-8">

          <div className="mb-8">

            <h1 className="text-3xl font-bold text-gray-800">
              Historique des conversations
            </h1>

            <p className="text-gray-500 mt-2">
              Consultez vos questions et les réponses
              de l'assistant.
            </p>

          </div>


          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">



            <div className="bg-white rounded-xl border border-gray-200 shadow-sm">

              <div className="p-5 border-b">

                <h2 className="font-bold text-gray-800">
                  Mes conversations
                </h2>

                <p className="text-sm text-gray-500 mt-1">
                  {historique.length} conversation(s)
                </p>

              </div>


              <div className="max-h-150 overflow-y-auto p-3">

                {historique.length === 0 ? (

                  <div className="text-center py-10">

                    <div className="text-4xl mb-3">
                      💬
                    </div>

                    <p className="text-gray-500">
                      Aucun historique
                    </p>

                  </div>

                ) : (

                  <div className="space-y-2">

                    {[...historique]
                    .sort(
                      (a, b) =>
                        new Date(b.date_creation).getTime() -
                        new Date(a.date_creation).getTime()
                    )
                    .map((chat) => (

                      <button
                        key={chat.id}
                        onClick={() =>
                          handleSelectChat(chat)
                        }
                        className={`
                          w-full
                          text-left
                          p-4
                          rounded-lg
                          border
                          transition
                          ${
                            chatSelectionne?.id === chat.id
                              ? "bg-blue-50 border-blue-300"
                              : "border-gray-200 hover:bg-gray-50"
                          }
                        `}
                      >

                        <p className="font-medium text-gray-800 line-clamp-2">

                          {chat.question}

                        </p>

                        <p className="text-xs text-gray-400 mt-2">

                          {new Date(
                            chat.date_creation
                          ).toLocaleString("fr-FR")}

                        </p>

                      </button>

                    ))}

                  </div>

                )}

              </div>

            </div>

            <div className="lg:col-span-2">

              <div className="bg-white rounded-xl border border-gray-200 shadow-sm">

                {!chatSelectionne ? (

                  <div className="min-h-125 flex flex-col items-center justify-center text-center p-8">

                    <div className="text-5xl mb-4">
                      💬
                    </div>

                    <h2 className="text-xl font-semibold text-gray-800">
                      Sélectionnez une conversation
                    </h2>

                    <p className="text-gray-500 mt-2">
                      Cliquez sur une question dans
                      votre historique pour afficher
                      la conversation.
                    </p>

                  </div>

                ) : (

                  <div>

                    <div className="p-5 border-b">

                      <h2 className="font-bold text-gray-800">
                        Conversation
                      </h2>

                      <p className="text-sm text-gray-400 mt-1">

                        {new Date(
                          chatSelectionne.date_creation
                        ).toLocaleString("fr-FR")}

                      </p>

                    </div>


                    <div className="p-6 space-y-6">


                      <div className="flex justify-end">

                        <div className="max-w-[80%]">

                          <p className="text-xs text-gray-400 mb-1 text-right">
                            Vous
                          </p>

                          <div className="bg-blue-600 text-white rounded-2xl rounded-br-md px-5 py-3">

                            {chatSelectionne.question}

                          </div>

                        </div>

                      </div>


                      <div className="flex justify-start">

                        <div className="max-w-[80%]">

                          <p className="text-xs text-gray-400 mb-1">
                            Assistant
                          </p>

                          <div className="bg-gray-100 text-gray-800 rounded-2xl rounded-bl-md px-5 py-3 whitespace-pre-wrap">

                            {loadingChat
                              ? "Chargement..."
                              : chatSelectionne.reponse
                            }

                          </div>

                        </div>

                      </div>

                    </div>

                  </div>

                )}

              </div>

            </div>

          </div>

        </main>

      </div>

    </div>

  );
}