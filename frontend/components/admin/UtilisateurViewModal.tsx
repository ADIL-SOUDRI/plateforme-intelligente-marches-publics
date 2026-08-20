"use client";

import { Utilisateur } from "@/types/auth";

interface Props {
  utilisateur: Utilisateur | null;
  open: boolean;
  onClose: () => void;
}

export default function UserViewModal({
  utilisateur,
  open,
  onClose,
}: Props) {

  if (!open || !utilisateur) {
    return null;
  }

  return (
    <div className="fixed inset-0 bg-slate-900/50 flex items-center justify-center z-50">

      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-2xl border border-gray-200">

        <h2 className="text-xl font-bold text-gray-800 mb-5">
          Informations utilisateur
        </h2>

        <div className="space-y-3">

          <p className="text-gray-700">
            <strong className="text-gray-900">ID :</strong>{" "}
            {utilisateur.id_utilisateur}
          </p>

          <p className="text-gray-700">
            <strong className="text-gray-900">Nom :</strong>{" "}
            {utilisateur.nom}
          </p>

          <p className="text-gray-700">
            <strong className="text-gray-900">Prénom :</strong>{" "}
            {utilisateur.prenom}
          </p>

          <p className="text-gray-700">
            <strong className="text-gray-900">Email :</strong>{" "}
            {utilisateur.email}
          </p>

        </div>

        <div className="flex justify-end mt-6">

          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 border border-gray-200"
          >
            Fermer
          </button>

        </div>

      </div>

    </div>
  );
}