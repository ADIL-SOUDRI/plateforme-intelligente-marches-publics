"use client";

import { useEffect, useState } from "react";
import { Utilisateur } from "@/types/auth";

interface Props {
  utilisateur: Utilisateur | null;

  open: boolean;

  onClose: () => void;

  onUpdate: (data: {
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
  }) => void | Promise<void>;
}

export default function UserUpdateModal({
  utilisateur,
  open,
  onClose,
  onUpdate,
}: Props) {

  const [nom, setNom] = useState("");
  const [prenom, setPrenom] = useState("");
  const [email, setEmail] = useState("");
  const [motDePasse, setMotDePasse] = useState("");

  // Charger les informations de l'utilisateur
  useEffect(() => {

    if (utilisateur) {

      setNom(utilisateur.nom);
      setPrenom(utilisateur.prenom);
      setEmail(utilisateur.email);
      setMotDePasse("");

    }

  }, [utilisateur]);

  if (!open || !utilisateur) {
    return null;
  }

  async function handleSubmit() {

    await onUpdate({
      nom,
      prenom,
      email,
      mot_de_passe: motDePasse,
    });

  }

  return (
    <div className="fixed inset-0 bg-slate-900/50 flex items-center justify-center z-50">

      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-2xl border border-gray-200">

        <h2 className="text-xl font-bold text-gray-800 mb-5">
          Modifier l'utilisateur
        </h2>

        <div className="space-y-4">

          <input
            value={nom}
            onChange={(e) => setNom(e.target.value)}
            placeholder="Nom"
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          />

          <input
            value={prenom}
            onChange={(e) => setPrenom(e.target.value)}
            placeholder="Prénom"
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          />

          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          />

          <input
            type="password"
            value={motDePasse}
            onChange={(e) => setMotDePasse(e.target.value)}
            placeholder="Nouveau mot de passe"
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          />

        </div>

        <div className="flex justify-end gap-3 mt-6">

          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 border border-gray-200"
          >
            Annuler
          </button>

          <button
            onClick={handleSubmit}
            className="px-4 py-2 bg-amber-500 text-white rounded-lg hover:bg-amber-600 shadow-sm"
          >
            Enregistrer
          </button>

        </div>

      </div>

    </div>
  );
}