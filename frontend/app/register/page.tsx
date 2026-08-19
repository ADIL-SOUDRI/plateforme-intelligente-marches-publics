"use client";

import { FormEvent, useState } from "react";
import { registerUser } from "@/services/authService";
import { useRouter } from "next/navigation";

export default function RegisterPage() {

  const router = useRouter();

  const [nom, setNom] = useState("");
  const [prenom, setPrenom] = useState("");
  const [email, setEmail] = useState("");
  const [motDePasse, setMotDePasse] = useState("");

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {

    e.preventDefault();

    setError("");
    setLoading(true);

    try {

      await registerUser({
        nom,
        prenom,
        email,
        mot_de_passe: motDePasse,
      });

      router.push("/login");

    } catch (error) {

      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Une erreur est survenue");
      }

    } finally {

      setLoading(false);

    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="w-full max-w-md bg-white p-8 rounded-xl shadow">

        <h1 className="text-2xl font-bold text-center mb-6">
          Créer un compte
        </h1>

        {error && (
          <div className="mb-4 p-3 bg-red-100 text-red-700 rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">

          <div>
            <label className="block mb-1">
              Nom
            </label>

            <input
              type="text"
              value={nom}
              onChange={(e) => setNom(e.target.value)}
              className="w-full border p-2 rounded"
              required
            />
          </div>

          <div>
            <label className="block mb-1">
              Prénom
            </label>

            <input
              type="text"
              value={prenom}
              onChange={(e) => setPrenom(e.target.value)}
              className="w-full border p-2 rounded"
              required
            />
          </div>

          <div>
            <label className="block mb-1">
              Email
            </label>

            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full border p-2 rounded"
              required
            />
          </div>

          <div>
            <label className="block mb-1">
              Mot de passe
            </label>

            <input
              type="password"
              value={motDePasse}
              onChange={(e) => setMotDePasse(e.target.value)}
              className="w-full border p-2 rounded"
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white p-2 rounded"
          >
            {loading ? "Inscription..." : "S'inscrire"}
          </button>

        </form>

        <p className="text-center mt-4">
          Déjà un compte ?{" "}
          <a
            href="/login"
            className="text-blue-600"
          >
            Se connecter
          </a>
        </p>

      </div>

    </main>
  );
}