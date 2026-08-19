"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";

export default function DashboardPage() {

  const router = useRouter();

  const [user, setUser] = useState<Utilisateur | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function chargerUtilisateur() {

      try {

        const utilisateur = await getCurrentUser();

        setUser(utilisateur);

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


  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p>Chargement...</p>
      </main>
    );
  }


  if (!user) {
    return null;
  }


  return (
    <div className="min-h-screen bg-gray-100">

    <Navbar
    nomUtilisateur={`${user.prenom} ${user.nom}`}
    email={user.email}
    />

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-8">

          <h1 className="text-3xl font-bold text-gray-800">
            Bienvenue {user.prenom} 
          </h1>

          <p className="text-gray-600 mt-2">
            Plateforme d'assistance aux marchés publics.
          </p>

        </main>

      </div>

    </div>
  );
}