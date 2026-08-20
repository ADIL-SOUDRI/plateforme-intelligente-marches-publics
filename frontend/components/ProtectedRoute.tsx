"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { getCurrentUser } from "@/services/userService";
import { Utilisateur } from "@/types/auth";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export default function ProtectedRoute({
  children,
}: ProtectedRouteProps) {

  const router = useRouter();

  const [user, setUser] =
    useState<Utilisateur | null>(null);

  const [loading, setLoading] =
    useState(true);


  useEffect(() => {

    async function verifierUtilisateur() {

      try {

        // Vérifier le token
        const token =
          localStorage.getItem("access_token");

        if (!token) {

          router.replace("/login");

          return;
        }

        const utilisateur =
          await getCurrentUser();

        setUser(utilisateur);


      } catch (error) {

        console.error(
          "Utilisateur non authentifié :",
          error
        );

        localStorage.removeItem(
          "access_token"
        );

        router.replace("/login");

      } finally {

        setLoading(false);

      }

    }


    verifierUtilisateur();

  }, [router]);


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
    <>
      {children}
    </>
  );
}