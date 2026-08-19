"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";

export default function ProfilePage() {
  const router = useRouter();

  const [user, setUser] = useState<Utilisateur | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function chargerProfil() {
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

    chargerProfil();
  }, [router]);

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p>Chargement du profil...</p>
      </main>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <main className="min-h-screen bg-gray-100 p-8">

      <div className="max-w-2xl mx-auto">

        <button
          onClick={() => router.push("/dashboard")}
          className="mb-6 text-blue-600 hover:underline"
        >
          ← Retour au Dashboard
        </button>

        <div className="bg-white rounded-xl shadow-sm p-8">

          <div className="flex items-center gap-4 mb-8">

            <div className="w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center text-3xl">
              👤
            </div>

            <div>
              <h1 className="text-2xl font-bold text-gray-800">
                Mon profil
              </h1>

              <p className="text-gray-500">
                Informations de votre compte
              </p>
            </div>

          </div>

          <div className="space-y-5">

            <div>
              <p className="text-sm text-gray-500">
                Prénom
              </p>

              <p className="text-lg font-medium">
                {user.prenom}
              </p>
            </div>

            <div>
              <p className="text-sm text-gray-500">
                Nom
              </p>

              <p className="text-lg font-medium">
                {user.nom}
              </p>
            </div>

            <div>
              <p className="text-sm text-gray-500">
                Email
              </p>

              <p className="text-lg font-medium">
                {user.email}
              </p>
            </div>

          </div>

        </div>

      </div>

    </main>
  );
}