"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import { getCurrentUser } from "@/services/userService";
import { getDocumentsReferences , importerDocument } from "@/services/documentService";

import { Utilisateur } from "@/types/auth";
import { DocumentReference } from "@/types/document";


export default function DocumentsPage() {
  const router = useRouter();

  const [user, setUser] =useState<Utilisateur | null>(null);

  const [documents, setDocuments] =useState<DocumentReference[]>([]);

  const [loading, setLoading] =useState(true);

  const [erreur, setErreur] =  useState("");
  const [showImport, setShowImport] = useState(false);

const [titre, setTitre] = useState("");
const [type, setType] = useState("");
const [fichier, setFichier] = useState<File | null>(null);

const [importLoading, setImportLoading] = useState(false);


  useEffect(() => {

    async function chargerDonnees() {

      try {
        const utilisateur =await getCurrentUser();

        setUser(utilisateur);

        const resultat = await getDocumentsReferences();
        setDocuments(resultat);


      } catch (error) { console.error(error);
        if (error instanceof Error) {
          setErreur(error.message);
        } else {

          setErreur(
            "Une erreur est survenue."
          );

        }

      } finally {

        setLoading(false);

      }

    }


    chargerDonnees();

  }, []);

  async function handleImport(e: React.FormEvent) {

  e.preventDefault();

  if (!fichier) {
    setErreur("Veuillez sélectionner un fichier.");
    return;
  }

  try {

    setImportLoading(true);
    setErreur("");

    const document = await importerDocument(
      titre,
      type,
      fichier
    );

    setDocuments((documentsActuels) => [
      document,
      ...documentsActuels
    ]);

    setTitre("");
    setType("");
    setFichier(null);

    setShowImport(false);

  } catch (error) {

    if (error instanceof Error) {
      setErreur(error.message);
    } else {
      setErreur("Erreur lors de l'importation.");
    }

  } finally {

    setImportLoading(false);
  }
}

  if (loading) {

    return (
      <main className="min-h-screen flex items-center justify-center">
      <p>Chargement...</p>
      </main>
    );

  }


  if (!user) {
    return null;
  }


  return (

    <div className="min-h-screen bg-gray-100">

      <Navbar
        nomUtilisateur={`${user.prenom} ${user.nom}`}
        email={user.email}
      />
      <div className="flex">
        <Sidebar />
        <main className="flex-1 p-8">
          <div className="flex items-center justify-between">

  <div>
    <h1 className="text-3xl font-bold text-gray-800">
      Documents
    </h1>

    <p className="text-gray-600 mt-2">
      Documents de référence des marchés publics.
    </p>
  </div>

  <button
    onClick={() => setShowImport(true)}
    className="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700"
  >
    + Importer un document
  </button>

{showImport && (
  <div className="fixed inset-0 bg-gray-900/50 backdrop-blur-sm flex items-center justify-center z-50">

    <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-2xl border border-gray-200">

      {/* Titre */}
      <h2 className="text-xl font-bold mb-5 text-gray-800">
        Importer un document
      </h2>

      {/* Erreur */}
      {erreur && (
        <div className="mb-4 bg-red-50 border border-red-200 text-red-600 p-3 rounded-lg text-sm">
          {erreur}
        </div>
      )}

      <form
        onSubmit={handleImport}
        className="space-y-4"
      >

        {/* Titre */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Titre
          </label>

          <input
            type="text"
            value={titre}
            onChange={(e) => setTitre(e.target.value)}
            placeholder="Ex : CCAG Fournitures"
            required
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          />
        </div>

        {/* Type */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Type
          </label>

          <select
            value={type}
            onChange={(e) => setType(e.target.value)}
            required
            className="w-full border border-gray-200 bg-gray-50 text-gray-800 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
          >
            <option value="" className="text-gray-400">
              Sélectionner un type
            </option>

            <option value="CCAG">CCAG</option>
            <option value="DECRET">Décret</option>
            <option value="CPS">CPS</option>
            <option value="CIRCULAIRE">Circulaire</option>
            <option value="GUIDE">Guide</option>
            <option value="AUTRE">Autre</option>
          </select>
        </div>

        {/* Fichier */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Fichier PDF
          </label>

          <input
            type="file"
            accept=".pdf,application/pdf"
            onChange={(e) =>
              setFichier(e.target.files?.[0] || null)
            }
            required
            className="w-full border border-gray-200 bg-gray-50 text-gray-600 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 file:mr-4 file:rounded-md file:border-0 file:bg-blue-50 file:px-3 file:py-1.5 file:text-sm file:font-medium file:text-blue-600 hover:file:bg-blue-100"
          />
        </div>

        {/* Boutons */}
        <div className="flex justify-end gap-3 mt-6">

          <button
            type="button"
            onClick={() => setShowImport(false)}
            disabled={importLoading}
            className="px-4 py-2 bg-gray-100 text-gray-700 border border-gray-200 rounded-lg hover:bg-gray-200 transition-colors"
          >
            Annuler
          </button>

          <button
            type="submit"
            disabled={importLoading}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 shadow-sm transition-colors disabled:bg-blue-300"
          >
            {importLoading ? "Traitement..." : "Ajouter"}
          </button>

        </div>

      </form>

    </div>

  </div>
)}
</div>
          {/* Erreur */}
          {erreur && (
            <div className="mt-6 bg-red-50 text-red-600 p-4 rounded-lg">
              {erreur}
            </div>

          )}

          {!erreur &&
            documents.length === 0 && (

              <div className="mt-8 bg-white p-6 rounded-xl shadow-sm">
                <p className="text-gray-500">
                  Aucun document disponible.
                </p>
              </div>

            )}

          {documents.length > 0 && (
            <div className="mt-8 space-y-4">
              {documents.map((document) => (
                <div
                  key={document.id}
                  className="bg-white rounded-xl shadow-sm p-6 flex items-center justify-between"
                >

                  <div>

                    <h2 className="text-lg font-semibold text-gray-800">

                      📄 {document.nom_fichier}

                    </h2>


                    <p className="text-sm text-gray-500 mt-2">

                      Taille :{" "}
                      {document.taille} Ko

                    </p>
                    <p className="text-sm text-gray-500">

                      Ajouté le :{" "}
                      {new Date( document.date_importation ).toLocaleDateString("fr-FR")}
                    </p>
                  </div>
                  <button
                    onClick={() =>
                        router.push( `/documents/${document.id}`) }
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                  >
                    Consulter
                  </button>

                </div>

              ))}

            </div>

          )}

        </main>

      </div>

    </div>

  );
}