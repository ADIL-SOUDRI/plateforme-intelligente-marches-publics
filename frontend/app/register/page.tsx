"use client";

import { FormEvent, useState } from "react";
import { registerUser } from "@/services/authService";

export default function InscriptionPage() {
  const [nom, setNom] = useState("");
  const [prenom, setPrenom] = useState("");
  const [email, setEmail] = useState("");
  const [motDePasse, setMotDePasse] = useState("");

  const [message, setMessage] = useState("");
  const [erreur, setErreur] = useState("");
  const [chargement, setChargement] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();

    setMessage("");
    setErreur("");
    setChargement(true);

    try {
      await registerUser({
        nom,
        prenom,
        email,
        mot_de_passe: motDePasse,
      });

      setMessage("Inscription réussie !");
      setNom("");
      setPrenom("");
      setEmail("");
      setMotDePasse("");

    } catch (error) {
      if (error instanceof Error) {
        setErreur(error.message);
      } else {
        setErreur("Une erreur est survenue.");
      }
    } finally {
      setChargement(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-slate-100 p-6">

      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl border border-slate-200 p-8">

        <h1 className="text-3xl font-bold text-center text-slate-800 mb-2">
          Créer un compte
        </h1>

        <p className="text-center text-slate-500 text-sm mb-7">
          Créez votre compte pour accéder à la plateforme
        </p>

        <form onSubmit={handleSubmit} className="space-y-5">

          <div>
            <label className="block mb-2 font-medium text-slate-700">
              Nom
            </label>

            <input
              type="text"
              value={nom}
              onChange={(e) => setNom(e.target.value)}
              required
              className="w-full border border-slate-300 bg-slate-50 rounded-lg px-4 py-3 text-slate-800 outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
              placeholder="Votre nom"
            />
          </div>

          <div>
            <label className="block mb-2 font-medium text-slate-700">
              Prénom
            </label>

            <input
              type="text"
              value={prenom}
              onChange={(e) => setPrenom(e.target.value)}
              required
              className="w-full border border-slate-300 bg-slate-50 rounded-lg px-4 py-3 text-slate-800 outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
              placeholder="Votre prénom"
            />
          </div>

          <div>
            <label className="block mb-2 font-medium text-slate-700">
              Email
            </label>

            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full border border-slate-300 bg-slate-50 rounded-lg px-4 py-3 text-slate-800 outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
              placeholder="exemple@email.com"
            />
          </div>

          <div>
            <label className="block mb-2 font-medium text-slate-700">
              Mot de passe
            </label>

            <input
              type="password"
              value={motDePasse}
              onChange={(e) => setMotDePasse(e.target.value)}
              required
              className="w-full border border-slate-300 bg-slate-50 rounded-lg px-4 py-3 text-slate-800 outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-100"
              placeholder="••••••••"
            />
          </div>

          {erreur && (
            <div className="bg-red-50 border border-red-200 text-red-700 p-3 rounded-lg text-sm">
              {erreur}
            </div>
          )}

          {message && (
            <div className="bg-emerald-50 border border-emerald-200 text-emerald-700 p-3 rounded-lg text-sm">
              {message}
            </div>
          )}

          <button
            type="submit"
            disabled={chargement}
            className="w-full bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white font-semibold py-3 rounded-lg shadow-sm transition duration-200 disabled:bg-blue-300 disabled:cursor-not-allowed"
          >
            {chargement ? "Inscription..." : "S'inscrire"}
          </button>

        </form>

        <p className="text-center mt-6 text-sm text-slate-500">
          Vous avez déjà un compte ?{" "}

          <a
            href="/login"
            className="text-blue-600 font-medium hover:text-blue-700 hover:underline transition"
          >
            Se connecter
          </a>
        </p>

      </div>

    </main>
  );
}