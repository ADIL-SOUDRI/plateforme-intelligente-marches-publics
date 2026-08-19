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


      localStorage.setItem(     "access_token",  resultat.access_token);

      router.push("/dashboard");

    } catch (error) {
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
    <main className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="w-full max-w-md bg-white p-8 rounded-xl shadow">

        <h1 className="text-2xl font-bold text-center mb-6">
          Connexion
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">

          {/* Email */}
          <div>
            <label className="block mb-1">
              Email
            </label>

            <input type="email" value={email}  onChange={(e) => setEmail(e.target.value)} placeholder="exemple@email.com" required  className="w-full border rounded-lg px-3 py-2" />
          </div>

          <div>
            <label className="block mb-1">
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
              className="w-full border rounded-lg px-3 py-2"
            />
          </div>

          {erreur && (
            <p className="text-red-500 text-sm">
              {erreur}
            </p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2 rounded-lg"
          >
            {loading
              ? "Connexion..."
              : "Se connecter"}
          </button>

        </form>

        <p className="text-center mt-4 text-sm">

          Vous n'avez pas de compte ?{" "}

          <a  href="/register" className="text-blue-600"  >
            S'inscrire
          </a>

        </p>

      </div>

    </main>
  );
}