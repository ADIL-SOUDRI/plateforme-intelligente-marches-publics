import { useEffect, useState } from "react";
import { DocumentReference } from "@/types/document";
import { updateDocument } from "@/services/adminDocumentService";

interface Props {
  open: boolean;
  document: DocumentReference;
  idAdmin: number;
  onClose: () => void;
  onUpdated: (documentModifie: DocumentReference) => void;
}

export default function DocumentUpdateModal({
  open,
  document,
  idAdmin,
  onClose,
  onUpdated,
}: Props) {

  const [titre, setTitre] = useState("");
  const [type, setType] = useState("");
  const [loading, setLoading] = useState(false);
  const [erreur, setErreur] = useState("");

  useEffect(() => {
    if (document) {
      setTitre(document.titre || "");
      setType(document.type || "");
      setErreur("");
    }
  }, [document]);

  if (!open) {
    return null;
  }

  async function handleUpdate() {

    setErreur("");

    if (!titre.trim()) {
      setErreur("Le titre est obligatoire.");
      return;
    }

    if (!type) {
      setErreur("Veuillez sélectionner un type.");
      return;
    }

    try {

      setLoading(true);

      const documentModifie =
        await updateDocument(
          document.id,
          {
            titre: titre,
            type: type,
            id_admin: idAdmin,
          }
        );

      onUpdated(documentModifie);

    } catch (error) {

      console.error(error);

      setErreur(
        error instanceof Error
          ? error.message
          : "Erreur lors de la modification"
      );

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">

      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-xl border border-gray-200">

        <h2 className="text-xl font-bold mb-5 text-gray-800">
          Modifier le document
        </h2>

        {erreur && (
          <div className="mb-4 bg-red-50 border border-red-200 text-red-600 p-3 rounded-lg">
            {erreur}
          </div>
        )}

        <div className="space-y-4">

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Titre
            </label>

            <input
              type="text"
              value={titre}
              onChange={(e) => setTitre(e.target.value)}
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Type
            </label>

            <select
              value={type}
              onChange={(e) => setType(e.target.value)}
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
            >
              <option value="">
                Sélectionner un type
              </option>

              <option value="CCAG">
                CCAG
              </option>

              <option value="DECRET">
                Décret
              </option>

              <option value="CPS">
                CPS
              </option>

              <option value="GUIDE">
                Guide
              </option>
              <option value="AUTRE"> 
                Autre 
              </option>
            </select>
          </div>

        </div>

        <div className="flex justify-end gap-3 mt-6">

          <button
            onClick={onClose}
            disabled={loading}
            className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors"
          >
            Annuler
          </button>

          <button
            onClick={handleUpdate}
            disabled={loading}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            {loading
              ? "Modification..."
              : "Enregistrer"}
          </button>

        </div>

      </div>

    </div>
  );
}