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
    <main className="min-h-screen flex items-center justify-center bg-gray-100 p-6">

      <div className="w-full max-w-md bg-white rounded-xl shadow-md p-8">

        <h1 className="text-2xl font-bold text-center mb-6">
          Créer un compte
        </h1>
        <form onSubmit={handleSubmit} className="space-y-4">

          <div>
            <label className="block mb-1 font-medium">
              Nom
            </label>

            <input
              type="text"
              value={nom}
              onChange={(e) => setNom(e.target.value)}
              required
              className="w-full border rounded-lg px-3 py-2"
              placeholder="Votre nom"
            />
          </div>

          <div>
            <label className="block mb-1 font-medium">
              Prénom
            </label>

            <input  type="text"  value={prenom}  onChange={(e) => setPrenom(e.target.value)}  required className="w-full border rounded-lg px-3 py-2"   placeholder="Votre prénom"  />
          </div>

          <div>
            <label className="block mb-1 font-medium">
              Email
            </label>

            <input  type="email"  value={email}  onChange={(e) => setEmail(e.target.value)}  required  className="w-full border rounded-lg px-3 py-2"  placeholder="exemple@email.com"  />
          </div>

          <div>
            <label className="block mb-1 font-medium">
              Mot de passe
            </label>

            <input  type="password"  value={motDePasse}  onChange={(e) => setMotDePasse(e.target.value)}  required  className="w-full border rounded-lg px-3 py-2"  placeholder="••••••••" />
          </div>

          {erreur && (
            <div className="bg-red-100 text-red-700 p-3 rounded-lg">
              {erreur}
            </div>
          )}

          {message && (
            <div className="bg-green-100 text-green-700 p-3 rounded-lg">
              {message}
            </div>
          )}

          <button  type="submit"  disabled={chargement}  className="w-full bg-blue-600 text-white py-2 rounded-lg" >
            {chargement ? "Inscription..." : "S'inscrire"}
          </button>

        </form>
        <p className="text-center mt-4 text-sm">
        Vous avez déjà un compte ?{" "}

        <a
            href="/login"
            className="text-blue-600 hover:underline"
        >
            Se connecter
        </a>
        </p>

      </div>

    </main>
  );
}