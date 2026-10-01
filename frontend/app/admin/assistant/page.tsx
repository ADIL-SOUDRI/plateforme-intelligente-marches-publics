"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import AdminNavbar from "@/components/admin/AdminNavbar";
import AdminSidebar from "@/components/admin/AdminSidebar";

import ChatBox from "@/components/ChatBox";

import { getCurrentAdmin } from "@/services/adminService";

export default function AdminAssistantPage() {

  const router = useRouter();

  const [admin, setAdmin] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function chargerAdmin() {

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

      } catch (error) {

        console.error(
          "Erreur lors de la récupération de l'administrateur :",
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

    chargerAdmin();

  }, [router]);

  if (loading) {

    return (

      <main className="min-h-screen flex items-center justify-center bg-gray-50">

        <div className="text-center">

          <div className="text-4xl mb-4">
            🤖
          </div>

          <p className="text-gray-600">
            Chargement de l'assistant...
          </p>

        </div>

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



        <main className="flex-1 p-6">


          <div className="mb-5">

            <h1 className="text-2xl font-bold text-gray-800">

              Assistant marchés publics

            </h1>

            <p className="text-gray-500 mt-1">

              Posez vos questions concernant les
              marchés publics et consultez les réponses
              fournies par le système RAG.

            </p>

          </div>




          <ChatBox
            chatSelectionne={null}
          />

        </main>

      </div>

    </div>

  );
}