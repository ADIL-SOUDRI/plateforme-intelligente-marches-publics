"use client";

import { useEffect, useState } from "react";
import { MessageResponse } from "@/types/chat";
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ChatBox from "@/components/ChatBox";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";

export default function ChatPage() {

  const [user, setUser] =
    useState<Utilisateur | null>(null);

  const [loading, setLoading] =
    useState(true);
  const [chatSelectionne, setChatSelectionne] =
  useState<MessageResponse | null>(null);

  useEffect(() => {

    const token =
      localStorage.getItem("access_token");

    // Pas de token → retour login
    if (!token) {
      window.location.replace("/login");
      return;
    }

    async function chargerUtilisateur() {

      try {

        const utilisateur =
          await getCurrentUser();

        setUser(utilisateur);

      } catch (error) {

        console.error(
          "Erreur lors du chargement de l'utilisateur :",
          error
        );

        localStorage.removeItem("access_token");

        window.location.replace("/login");

      } finally {

        setLoading(false);

      }
    }

    chargerUtilisateur();

  }, []);


  if (loading) {

    return (
      <main className="min-h-screen flex items-center justify-center">

        <p>
          Vérification de connexion...
        </p>

      </main>
    );

  }


  if (!user) {
    return null;
  }


  return (

    <div className="min-h-screen bg-gray-100">

      {/* Navbar */}

      <Navbar
        nomUtilisateur={`${user.prenom} ${user.nom}`}
        email={user.email}
      />


      <div className="flex">

        {/* Sidebar sans historique */}

        <Sidebar />


        {/* Contenu principal */}

        <main className="flex-1 p-6">

          <div className="mb-4">

            <h1 className="text-2xl font-bold text-gray-800">
              Bienvenue  {user.prenom}
            </h1>

            <p className="text-gray-500">
              Posez vos questions concernant les marchés publics.
            </p>

          </div>


          {/* Chatbot */}

          <ChatBox
            chatSelectionne={chatSelectionne}
            />

        </main>

      </div>

    </div>

  );
}