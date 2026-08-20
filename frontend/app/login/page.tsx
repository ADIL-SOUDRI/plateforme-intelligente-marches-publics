"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { loginUser } from "@/services/authService";

export default function LoginPage() {
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
      role: "utilisateur",
    });

    console.log("Login réussi :", resultat);

    document.cookie = `access_token=${resultat.access_token}; path=/`;
    localStorage.setItem(
      "access_token",
      resultat.access_token
    );

    router.replace("/dashboard");

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
    // <main className="min-h-screen flex items-center justify-center bg-gray-100">
    <main className="min-h-screen flex items-center justify-center bg-white px-4">

      {/* <div className="w-full max-w-md bg-white p-8 rounded-xl shadow"> */}
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-lg border border-gray-100">

        <h1 className="text-2xl font-bold text-center mb-6 text-gray-800">
          Connexion
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">

          <div>
            <label className="block mb-2 text-sm font-medium text-gray-700 ">
              Email
            </label>

            <input type="email" value={email}  onChange={(e) => setEmail(e.target.value)} placeholder="exemple@email.com" required  className=" placeholder-gray-400 w-full border rounded-lg px-3 py-2" />
          </div>

          <div>
            <label className="block mb-2 text-sm font-medium text-gray-700">
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
              className="w-full border rounded-lg px-3 py-2 placeholder-gray-400 "
            />
          </div>

          {erreur && (
            <p className="text-red-600 text-sm bg-red-50 border border-red-100 rounded-lg px-3 py-2">
              {erreur}
            </p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 rounded-lg transition duration-200 disabled:opacity-50"
          >
            {loading
              ? "Connexion..."
              : "Se connecter"}
          </button>

        </form>

        <p className="text-center mt-5 text-sm text-gray-500">
          Vous n'avez pas de compte ?{" "}
          <a
            href="/register"
            className="text-blue-600 font-medium hover:text-blue-700 hover:underline transition"
          >
            S'inscrire
          </a>
        </p>

      </div>

    </main>
  );
}