"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";

import AdminNavbar from "@/components/admin/AdminNavbar";
import AdminSidebar from "@/components/admin/AdminSidebar";

import { getCurrentAdmin } from "@/services/adminService";

export default function AdminDashboardPage() {

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

        console.error(error);

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


  // ======================================================
  // CHARGEMENT
  // ======================================================

  if (loading) {

    return (
      <main className="min-h-screen flex items-center justify-center bg-gray-50">

        <div className="text-center">

          <p className="text-gray-600">
            Chargement...
          </p>

        </div>

      </main>
    );

  }


  if (!admin) {
    return null;
  }


  // ======================================================
  // INTERFACE
  // ======================================================

  return (

    <div className="min-h-screen bg-gray-50">

      {/* ==================================================
          NAVBAR
      ================================================== */}

      <AdminNavbar
        nomAdmin={`${admin.prenom} ${admin.nom}`}
        email={admin.email}
      />


      <div className="flex">

        {/* ==================================================
            SIDEBAR
        ================================================== */}

        <AdminSidebar />


        {/* ==================================================
            CONTENU PRINCIPAL
        ================================================== */}

        <main className="flex-1 p-8">

          {/* Titre */}

          <div className="mb-8">

            <h1 className="text-3xl font-bold text-gray-800">

              Bienvenue {admin.prenom} 👋

            </h1>

            <p className="text-gray-500 mt-2">

              Tableau de bord administrateur.

            </p>

          </div>


          {/* ==================================================
              STATISTIQUES
          ================================================== */}

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">


            {/* ==================================================
                UTILISATEURS
            ================================================== */}

            <Link
              href="/admin/utilisateurs"
              className="
                block
                bg-white
                p-6
                rounded-xl
                shadow-sm
                border
                border-gray-200
                hover:shadow-md
                hover:border-blue-200
                hover:bg-blue-50/30
                transition-all
              "
            >

              <div className="flex items-center justify-between">

                <p className="text-gray-500">
                  Utilisateurs
                </p>

                <div className="
                  w-10
                  h-10
                  flex
                  items-center
                  justify-center
                  rounded-lg
                  bg-blue-50
                  text-blue-600
                ">
                  👥
                </div>

              </div>

              <p className="text-3xl font-bold text-blue-600 mt-4">
                -
              </p>

              <p className="text-sm text-gray-400 mt-2">
                Gérer les utilisateurs
              </p>

            </Link>


            {/* ==================================================
                DOCUMENTS
            ================================================== */}

            <Link
              href="/admin/documents"
              className="
                block
                bg-white
                p-6
                rounded-xl
                shadow-sm
                border
                border-gray-200
                hover:shadow-md
                hover:border-blue-200
                hover:bg-blue-50/30
                transition-all
              "
            >

              <div className="flex items-center justify-between">

                <p className="text-gray-500">
                  Documents
                </p>

                <div className="
                  w-10
                  h-10
                  flex
                  items-center
                  justify-center
                  rounded-lg
                  bg-blue-50
                  text-blue-600
                ">
                  📄
                </div>

              </div>

              <p className="text-3xl font-bold text-blue-600 mt-4">
                -
              </p>

              <p className="text-sm text-gray-400 mt-2">
                Gérer les documents
              </p>

            </Link>


            {/* ==================================================
                QUESTIONS
            ================================================== */}

            <div className="
              bg-white
              p-6
              rounded-xl
              shadow-sm
              border
              border-gray-200
            ">

              <div className="flex items-center justify-between">

                <p className="text-gray-500">
                  Questions
                </p>

                <div className="
                  w-10
                  h-10
                  flex
                  items-center
                  justify-center
                  rounded-lg
                  bg-blue-50
                  text-blue-600
                ">
                  💬
                </div>

              </div>

              <p className="text-3xl font-bold text-blue-600 mt-4">
                -
              </p>

              <p className="text-sm text-gray-400 mt-2">
                Questions posées au chatbot
              </p>

            </div>

          </div>


          {/* ==================================================
              INFORMATIONS
          ================================================== */}

          <div className="
            mt-8
            bg-white
            rounded-xl
            shadow-sm
            border
            border-gray-200
            p-6
          ">

            <h2 className="text-xl font-bold text-gray-800 mb-2">

              Espace administrateur

            </h2>

            <p className="text-gray-500">

              Depuis ce tableau de bord, vous pouvez
              gérer les utilisateurs, les documents
              et les différentes ressources de la
              plateforme d'assistance aux marchés publics.

            </p>

          </div>

        </main>

      </div>

    </div>
  );
}