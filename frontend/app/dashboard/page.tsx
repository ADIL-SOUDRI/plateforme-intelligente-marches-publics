"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";
import { getHistoriqueUtilisateur } from "@/services/chatService";
import { MessageResponse } from "@/types/chat";

export default function DashboardPage() {

  const router = useRouter();

  const [user, setUser] = useState<Utilisateur | null>(null);
  const [loading, setLoading] = useState(true);
  const [historique, setHistorique] = useState<MessageResponse[]>([]);

  useEffect(() => {

    async function chargerUtilisateur() {

      try {

        const utilisateur = await getCurrentUser();

        setUser(utilisateur);

        const historiqueUtilisateur =
          await getHistoriqueUtilisateur(
            utilisateur.id_utilisateur
          );

        setHistorique(historiqueUtilisateur);

      } catch (error) {

        console.error(error);

        localStorage.removeItem("access_token");

        window.location.replace("/login");

      } finally {

        setLoading(false);

      }
    }

    chargerUtilisateur();

  }, [router]);


  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-slate-100">
        <p className="text-slate-600 font-medium">
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

      <Navbar
        nomUtilisateur={`${user.prenom} ${user.nom}`}
        email={user.email}
      />

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-8">

          {/* En-tête */}
          <div className="mb-8">

            <h1 className="text-3xl font-bold text-slate-800">
              Bienvenue, {user.prenom}
            </h1>

            <p className="text-slate-500 mt-2">
              Plateforme intelligente d'assistance aux marchés publics.
            </p>

          </div>


          {/* Blocs principaux */}
          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">


            {/* Assistant */}
            <div
              onClick={() => router.push("/chat")}
              className="group cursor-pointer bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-lg hover:border-blue-300 transition duration-200"
            >

              <div className="flex items-center justify-between mb-5">

                <div className="w-14 h-14 rounded-xl bg-blue-100 flex items-center justify-center">
                  <span className="text-2xl">
                    💬
                  </span>
                </div>

                <span className="text-blue-600 text-xl group-hover:translate-x-1 transition">
                  →
                </span>

              </div>

              <h2 className="text-xl font-bold text-slate-800 mb-2">
                Assistant
              </h2>

              <p className="text-sm text-slate-500 leading-6">
                Posez vos questions sur les marchés publics et obtenez
                des réponses basées sur les documents de référence.
              </p>

              <div className="mt-5 text-sm font-semibold text-blue-600">
                Accéder à l'assistant
              </div>

            </div>


            {/* Documents */}
            <div
              onClick={() => router.push("/documents")}
              className="group cursor-pointer bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-lg hover:border-indigo-300 transition duration-200"
            >

              <div className="flex items-center justify-between mb-5">

                <div className="w-14 h-14 rounded-xl bg-indigo-100 flex items-center justify-center">
                  <span className="text-2xl">
                    📚
                  </span>
                </div>

                <span className="text-indigo-600 text-xl group-hover:translate-x-1 transition">
                  →
                </span>

              </div>

              <h2 className="text-xl font-bold text-slate-800 mb-2">
                Documents Importés
              </h2>

              <p className="text-sm text-slate-500 leading-6">
                Consultez les documents de référence utilisés par
                la plateforme pour fournir des réponses fiables.
              </p>

              <div className="mt-5 text-sm font-semibold text-indigo-600">
                Consulter les documents
              </div>

            </div>


            {/* Historique */}
            <div
              onClick={() => router.push("/chat/historique")}
              className="group cursor-pointer bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-lg hover:border-emerald-300 transition duration-200"
            >

              <div className="flex items-center justify-between mb-5">

                <div className="w-14 h-14 rounded-xl bg-emerald-100 flex items-center justify-center">
                  <span className="text-2xl">
                    🕘
                  </span>
                </div>

                <span className="text-emerald-600 text-xl group-hover:translate-x-1 transition">
                  →
                </span>

              </div>

              <h2 className="text-xl font-bold text-slate-800 mb-2">
                Historique
              </h2>

              <p className="text-sm text-slate-500 leading-6">
                Retrouvez vos anciennes questions et les réponses
                générées par l'assistant.
              </p>

              <div className="mt-5 flex items-center justify-between">

                <span className="text-sm font-semibold text-emerald-600">
                  Voir l'historique
                </span>

                <span className="text-xs bg-emerald-50 text-emerald-700 px-2 py-1 rounded-full">
                  {historique.length} question{historique.length !== 1 ? "s" : ""}
                </span>

              </div>

            </div>

          </div>


          {/* Section activité récente */}
          <div className="mt-8 bg-white rounded-2xl border border-slate-200 shadow-sm p-6">

            <div className="flex items-center justify-between mb-5">

              <div>
                <h2 className="text-xl font-bold text-slate-800">
                  Activité récente
                </h2>

                <p className="text-sm text-slate-500 mt-1">
                  Vos dernières interactions avec l'assistant
                </p>
              </div>

              <span className="text-2xl">
                📊
              </span>

            </div>


            {historique.length === 0 ? (

              <div className="py-8 text-center">

                <div className="text-4xl mb-3">
                  💬
                </div>

                <p className="text-slate-500">
                  Aucune question posée pour le moment.
                </p>

                <button
                  onClick={() => router.push("/chat")}
                  className="mt-4 px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition"
                >
                  Poser une question
                </button>

              </div>

            ) : (

              <div className="space-y-3">

                {[...historique]
                  .sort(
                    (a, b) =>
                      new Date(b.date_creation).getTime() -
                      new Date(a.date_creation).getTime()
                  )
                  .slice(0, 5)
                  .map((chat) => (

                  <div
                    key={chat.id}
                    className="flex items-center justify-between gap-4 p-4 rounded-xl bg-slate-50 hover:bg-blue-50 transition"
                  >

                    <div className="min-w-0">

                      <p className="font-medium text-slate-700 truncate">
                        {chat.question}
                      </p>

                      <p className="text-xs text-slate-400 mt-1">
                        {new Date(
                          chat.date_creation
                        ).toLocaleDateString("fr-FR")}
                      </p>

                    </div>

                    <span className="text-blue-600">
                      →
                    </span>

                  </div>

                ))}

              </div>

            )}

          </div>

        </main>

      </div>

    </div>
  );
}