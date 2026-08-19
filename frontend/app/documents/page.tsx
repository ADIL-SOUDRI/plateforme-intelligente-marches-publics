"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import { getCurrentUser } from "@/services/userService";
import { getDocumentsReferences } from "@/services/documentService";

import { Utilisateur } from "@/types/auth";
import { DocumentReference } from "@/types/document";


export default function DocumentsPage() {
  const router = useRouter();

  const [user, setUser] =useState<Utilisateur | null>(null);

  const [documents, setDocuments] =useState<DocumentReference[]>([]);

  const [loading, setLoading] =useState(true);

  const [erreur, setErreur] =  useState("");


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
          <h1 className="text-3xl font-bold text-gray-800">
            Documents
          </h1>
          <p className="text-gray-600 mt-2">
            Documents de référence des marchés publics.
          </p>
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
                      {new Date( document.date_ajout ).toLocaleDateString("fr-FR")}
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