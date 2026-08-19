"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { getHistoriqueUtilisateur,getChat} from "@/services/chatService";
import { MessageResponse } from "@/types/chat";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ChatBox from "@/components/ChatBox";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";


export default function ChatPage() {

  const router = useRouter();
  const [user, setUser] =
    useState<Utilisateur | null>(null);
  const [loading, setLoading] =useState(true);

  const [historique, setHistorique] = useState<MessageResponse[]>([]);

  const [chatSelectionne, setChatSelectionne] =useState<MessageResponse | null>(null);

  useEffect(() => {

    async function chargerUtilisateur() {
      try {

        const utilisateur =await getCurrentUser();
        setUser(utilisateur);

        const historiqueUtilisateur =await getHistoriqueUtilisateur(utilisateur.id_utilisateur);

        setHistorique( historiqueUtilisateur);


      } catch (error) {
        console.error(error);
        localStorage.removeItem("access_token");
        router.push("/login");

      } finally {
        setLoading(false);
      }

    }

    chargerUtilisateur();

  }, [router]);


  async function handleSelectChat(
  chat: MessageResponse
) {

  try {

    const chatComplet = await getChat(chat.id);

    setChatSelectionne(chatComplet);

  } catch (error) {

    console.error( "Erreur lors du chargement du chat :",error);

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

    <div className="min-h-screen bg-gray-100">

      {/* Navbar */}

      <Navbar
        nomUtilisateur={`${user.prenom} ${user.nom}`}
        email={user.email}
      />


      <div className="flex">

        <Sidebar
          historique={historique}
          onSelectChat={handleSelectChat}
        />
        <main className="flex-1 p-6">

          <div className="mb-4">

            <h1 className="text-2xl font-bold text-gray-800">

              Assistant marchés publics

            </h1>

            <p className="text-gray-500">

              Posez vos questions concernant les marchés publics.

            </p>

          </div>


          <ChatBox
            chatSelectionne={chatSelectionne}
            />
             </main>
             </div>
    </div>

  );
}