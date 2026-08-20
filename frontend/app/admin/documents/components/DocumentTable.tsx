"use client";

import { DocumentReference } from "@/types/document";

interface Props {
  documents: DocumentReference[];

  onView: (id: number) => void;

  onDelete: (
    id: number,
    nomFichier: string
  ) => void;
}

export default function DocumentTable({
  documents,
  onView,
  onDelete,
}: Props) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">


      <div className="px-6 py-5 border-b border-gray-200">

        <h2 className="text-xl font-semibold text-gray-800">
          Documents
        </h2>

        <p className="text-sm text-gray-500 mt-1">
          Liste des documents de référence.
        </p>

      </div>


      <div className="overflow-x-auto">

        <table className="w-full">

          <thead className="bg-gray-50">

            <tr>

              <th className="text-left px-6 py-4 text-sm font-semibold text-gray-600">
                ID
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-gray-600">
                Fichier
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-gray-600">
                Taille
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-gray-600">
                Date d'ajout
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-gray-600">
                Administrateur
              </th>

              <th className="text-center px-6 py-4 text-sm font-semibold text-gray-600">
                Actions
              </th>

            </tr>

          </thead>

          <tbody>

            {documents.length === 0 ? (

              <tr>

                <td
                  colSpan={6}
                  className="text-center py-10 text-gray-500"
                >
                  Aucun document trouvé.
                </td>

              </tr>

            ) : (

              documents.map((document) => (

                <tr
                  key={document.id}
                  className="border-t border-gray-100 hover:bg-blue-50/50 transition-colors"
                >

                  <td className="px-6 py-4 text-gray-600">
                    {document.id}
                  </td>

                  <td className="px-6 py-4">

                    <div className="flex items-center gap-3">

                      <span className="text-2xl">
                        📄
                      </span>

                      <span className="font-medium text-gray-800">
                        {document.nom_fichier}
                      </span>

                    </div>

                  </td>


                  <td className="px-6 py-4 text-gray-600">
                    {document.taille} Ko
                  </td>


                  <td className="px-6 py-4 text-gray-600">

                    {new Date(
                      document.date_ajout
                    ).toLocaleDateString("fr-FR")}

                  </td>


                  <td className="px-6 py-4 text-gray-600">
                    Admin #{document.id_admin}
                  </td>


                  <td className="px-6 py-4">

                    <div className="flex justify-center gap-2">

                      {/* Consulter */}

                      <button
                        onClick={() =>
                          onView(document.id)
                        }
                        className="px-3 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors shadow-sm"
                        title="Consulter"
                      >
                        👁
                      </button>

                      <button
                        onClick={() =>
                          onDelete(
                            document.id,
                            document.nom_fichier
                          )
                        }
                        className="px-3 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors shadow-sm"
                        title="Supprimer"
                      >
                        🗑
                      </button>

                    </div>

                  </td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}