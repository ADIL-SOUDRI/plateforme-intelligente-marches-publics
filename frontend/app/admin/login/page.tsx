"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { loginUser } from "@/services/authService";

export default function AdminLoginPage() {

  const router = useRouter();

  const [email, setEmail] = useState("");
  const [motDePasse, setMotDePasse] = useState("");

  const [erreur, setErreur] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {

    e.preventDefault();

    setErreur("");
    setLoading(true);

    try {

      const resultat = await loginUser({
        email,
        mot_de_passe: motDePasse,
        role: "administrateur",
      });

      console.log("Login administrateur réussi :", resultat);

      localStorage.setItem(
        "access_token",
        resultat.access_token
      );

      document.cookie =
        `access_token=${resultat.access_token}; path=/`;

      router.replace("/admin/dashboard");

    } catch (error) {

      console.error(error);

      if (error instanceof Error) {
        setErreur(error.message);
      } else {
        setErreur("Erreur lors de la connexion");
      }

    } finally {

      setLoading(false);

    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-50">

      <div className="w-full max-w-md bg-white p-8 rounded-xl shadow-xl border border-gray-200">

        <div className="text-center mb-6">

          <div className="w-16 h-16 mx-auto mb-4 flex items-center justify-center rounded-full bg-blue-50 text-4xl">
            🛡️
          </div>

          <h1 className="text-2xl font-bold text-gray-800">
            Connexion Administrateur
          </h1>

          <p className="text-gray-500 mt-2">
            Espace d'administration
          </p>

        </div>


        <form
          onSubmit={handleSubmit}
          className="space-y-4"
        >

          <div>

            <label className="block mb-1 text-sm font-medium text-gray-700">
              Email
            </label>

            <input
              type="email"
              value={email}
              onChange={(e) =>
                setEmail(e.target.value)
              }
              placeholder="exemple@email.com"
              required
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-3 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />

          </div>


          <div>

            <label className="block mb-1 text-sm font-medium text-gray-700">
              Mot de passe
            </label>

            <input
              type="password"
              value={motDePasse}
              onChange={(e) =>
                setMotDePasse(e.target.value)
              }
              placeholder="••••••••"
              required
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-3 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />

          </div>


          {erreur && (

            <p className="text-red-500 text-sm bg-red-50 border border-red-100 rounded-lg px-3 py-2">
              {erreur}
            </p>

          )}


          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2.5 rounded-lg font-medium shadow-sm transition-colors"
          >

            {loading
              ? "Connexion..."
              : "Se connecter"}

          </button>

        </form>


        <button
          onClick={() => router.push("/")}
          className="w-full mt-4 text-gray-500 text-sm hover:text-blue-600 transition-colors"
        >
          ← Retour
        </button>

      </div>

    </main>
  );
}