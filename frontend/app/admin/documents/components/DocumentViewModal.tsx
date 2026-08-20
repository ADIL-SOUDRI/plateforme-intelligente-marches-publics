"use client";

import { DocumentReference } from "@/types/document";

interface Props {
  open: boolean;
  document: DocumentReference | null;
  onClose: () => void;
}

export default function DocumentViewModal({
  open,
  document,
  onClose,
}: Props) {

  if (!open || !document) {
    return null;
  }


  return (

    <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">

      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-xl border border-gray-200">

        <h2 className="text-xl font-bold mb-6 text-gray-800">
          Informations du document
        </h2>


        <div className="space-y-4">

          <div>
            <p className="text-sm text-gray-500">
              ID
            </p>

            <p className="font-medium text-gray-800">
              {document.id}
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Titre
            </p>

            <p className="font-medium text-gray-800">
              {document.titre || "-"}
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Type
            </p>

            <p className="font-medium text-gray-800">
              {document.type || "-"}
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Nom du fichier
            </p>

            <p className="font-medium text-gray-800 break-all">
              {document.nom_fichier}
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Taille
            </p>

            <p className="font-medium text-gray-800">
              {(document.taille / 1024 / 1024).toFixed(2)} MB
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Date d'ajout
            </p>

            <p className="font-medium text-gray-800">
              {new Date(
                document.date_ajout
              ).toLocaleString("fr-FR")}
            </p>
          </div>


          <div>
            <p className="text-sm text-gray-500">
              Administrateur
            </p>

            <p className="font-medium text-gray-800">
              {document.id_admin}
            </p>
          </div>

        </div>


        <div className="flex justify-end mt-6">

          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors"
          >
            Fermer
          </button>

        </div>

      </div>

    </div>
  );
}