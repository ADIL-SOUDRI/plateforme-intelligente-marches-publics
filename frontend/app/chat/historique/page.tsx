"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import { getCurrentUser } from "@/services/userService";

import {
  getHistoriqueUtilisateur,
  getChat,
} from "@/services/chatService";

import { Utilisateur } from "@/types/auth";
import { MessageResponse } from "@/types/chat";


export default function HistoriquePage() {

  const router = useRouter();


  const [user, setUser] =
    useState<Utilisateur | null>(null);


  const [historique, setHistorique] =
    useState<MessageResponse[]>([]);


  const [chatSelectionne, setChatSelectionne] =
    useState<MessageResponse | null>(null);


  const [loading, setLoading] =
    useState(true);


  const [loadingChat, setLoadingChat] =
    useState(false);


  /*
   * Charger utilisateur + historique
   */

  useEffect(() => {

    const token =
      localStorage.getItem("access_token");

    if (!token) {

      router.replace("/login");

      return;

    }


    async function chargerDonnees() {

      try {

        const utilisateur =
          await getCurrentUser();

        setUser(utilisateur);


        // const historiqueUtilisateur =
        //   await getHistoriqueUtilisateur(
        //     utilisateur.id_utilisateur
        //   );
        const historiqueUtilisateur =
        await getHistoriqueUtilisateur(
            utilisateur.id_utilisateur
        );

        const historiqueTrie =
        [...historiqueUtilisateur].sort(
            (a, b) =>
            new Date(b.date_creation).getTime() -
            new Date(a.date_creation).getTime()
        );

        setHistorique(historiqueTrie);

        // setHistorique(
        //   historiqueUtilisateur
        // );


      } catch (error) {

        console.error(error);

        localStorage.removeItem(
          "access_token"
        );

        router.replace("/login");


      } finally {

        setLoading(false);

      }

    }


    chargerDonnees();

  }, [router]);


  /*
   * Sélection d'une conversation
   */

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
        "Erreur lors du chargement de la conversation :",
        error
      );


    } finally {

      setLoadingChat(false);

    }

  }


  if (loading) {

    return (

      <main className="min-h-screen flex items-center justify-center">

        <p>
          Chargement...
        </p>

      </main>

    );

  }


  if (!user) {
    return null;
  }


  return (

    <div className="min-h-screen bg-slate-100">

      {/* ========================= */}
      {/* NAVBAR */}
      {/* ========================= */}

      <Navbar
        nomUtilisateur={`${user.prenom} ${user.nom}`}
        email={user.email}
      />


      <div className="flex">


        {/* ========================= */}
        {/* SIDEBAR */}
        {/* ========================= */}

        <Sidebar />


        {/* ========================= */}
        {/* CONTENU HISTORIQUE */}
        {/* ========================= */}

        <main className="flex-1 p-6">

          <div className="mb-6">

            <h1 className="text-2xl font-bold text-slate-800">

              Historique des conversations

            </h1>

            <p className="text-slate-500 mt-1">

              Sélectionnez une conversation pour
              afficher son contenu.

            </p>

          </div>


          {/* ========================= */}
          {/* LES DEUX ZONES */}
          {/* ========================= */}

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">


            {/* ========================= */}
            {/* ZONE 1 : LISTE DES CHATS */}
            {/* ========================= */}

            <section className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">

              <div className="p-5 border-b border-slate-200">

                <h2 className="font-bold text-slate-800">

                  Mes conversations

                </h2>

                <p className="text-sm text-slate-500 mt-1">

                  {historique.length} conversation(s)

                </p>

              </div>


              <div className="max-h-[650px] overflow-y-auto p-3">


                {historique.length === 0 ? (

                  <div className="text-center py-10">

                    <div className="text-4xl mb-3">
                      💬
                    </div>

                    <p className="text-slate-500">

                      Aucun historique

                    </p>

                  </div>

                ) : (

                  <div className="space-y-2">

                    {historique.map((chat) => (

                      <button
                        key={chat.id}
                        onClick={() =>
                          handleSelectChat(chat)
                        }
                        className={`
                          w-full
                          text-left
                          p-4
                          rounded-xl
                          border
                          transition
                          ${
                            chatSelectionne?.id === chat.id
                              ? "bg-blue-50 border-blue-300"
                              : "border-slate-200 hover:bg-slate-50"
                          }
                        `}
                      >

                        <p className="font-medium text-slate-800 line-clamp-3">

                          {chat.question}

                        </p>


                        <p className="text-xs text-slate-400 mt-2">

                          {new Date(
                            chat.date_creation
                          ).toLocaleString("fr-FR")}

                        </p>

                      </button>

                    ))}

                  </div>

                )}

              </div>

            </section>


            {/* ========================= */}
            {/* ZONE 2 : CHAT SÉLECTIONNÉ */}
            {/* ========================= */}

            <section className="lg:col-span-2">

              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm min-h-[650px]">


                {!chatSelectionne ? (

                  /* Aucun chat sélectionné */

                  <div className="h-[650px] flex flex-col items-center justify-center text-center p-8">

                    <div className="text-5xl mb-4">
                      💬
                    </div>

                    <h2 className="text-xl font-semibold text-slate-700">

                      Sélectionnez une conversation

                    </h2>

                    <p className="text-slate-500 mt-2 max-w-md">

                      Cliquez sur une conversation
                      dans la liste pour afficher
                      la question et la réponse.

                    </p>

                  </div>

                ) : (

                  /* Chat sélectionné */

                  <div>


                    {/* Header */}

                    <div className="p-5 border-b border-slate-200">

                      <h2 className="font-bold text-slate-800">

                        Conversation

                      </h2>

                      <p className="text-sm text-slate-400 mt-1">

                        {new Date(
                          chatSelectionne.date_creation
                        ).toLocaleString("fr-FR")}

                      </p>

                    </div>


                    {/* Messages */}

                    <div className="p-6 space-y-6">


                      {/* QUESTION UTILISATEUR */}

                      <div className="flex justify-end">

                        <div className="max-w-[80%]">

                          <p className="text-xs text-slate-400 mb-2 text-right">

                            Vous

                          </p>


                          <div className="bg-blue-600 text-white rounded-2xl rounded-br-md px-5 py-3">

                            <p className="whitespace-pre-wrap">

                              {chatSelectionne.question}

                            </p>

                          </div>

                        </div>

                      </div>


                      {/* RÉPONSE ASSISTANT */}

                      <div className="flex justify-start">

                        <div className="max-w-[80%]">

                          <p className="text-xs text-slate-400 mb-2">

                            Assistant

                          </p>


                          <div className="bg-slate-100 text-slate-800 rounded-2xl rounded-bl-md px-5 py-3">

                            {loadingChat ? (

                              <p>
                                Chargement...
                              </p>

                            ) : (

                              <p className="whitespace-pre-wrap">

                                {chatSelectionne.reponse}

                              </p>

                            )}

                          </div>

                        </div>

                      </div>


                    </div>

                  </div>

                )}

              </div>

            </section>

          </div>

        </main>

      </div>

    </div>

  );
}