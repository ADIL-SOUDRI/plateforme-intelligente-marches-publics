"use client";

import { Utilisateur } from "@/types/auth";

interface Props {
  utilisateurs: Utilisateur[];
  onView: (id: number) => void;
  onUpdate: (utilisateur: Utilisateur) => void;
  onDelete: (
    id: number,
    nom: string,
    prenom: string
  ) => void;
}

export default function UserTable({
  utilisateurs,
  onView,
  onUpdate,
  onDelete,
}: Props) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead className="bg-blue-50">
            <tr>

              <th className="text-left px-6 py-4 text-sm font-semibold text-blue-900">
                ID
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-blue-900">
                Nom
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-blue-900">
                Prénom
              </th>

              <th className="text-left px-6 py-4 text-sm font-semibold text-blue-900">
                Email
              </th>

              <th className="text-center px-6 py-4 text-sm font-semibold text-blue-900">
                Actions
              </th>

            </tr>
          </thead>

          <tbody>

            {utilisateurs.length === 0 ? (
              <tr>
                <td
                  colSpan={5}
                  className="text-center py-10 text-gray-500"
                >
                  Aucun utilisateur trouvé.
                </td>
              </tr>
            ) : (
              utilisateurs.map((utilisateur) => (

                <tr
                  key={utilisateur.id_utilisateur}
                  className="border-t border-gray-100 hover:bg-blue-50 transition-colors duration-150"
                >

                  <td className="px-6 py-4 text-gray-700">
                    {utilisateur.id_utilisateur}
                  </td>

                  <td className="px-6 py-4 text-gray-800">
                    {utilisateur.nom}
                  </td>

                  <td className="px-6 py-4 text-gray-800">
                    {utilisateur.prenom}
                  </td>

                  <td className="px-6 py-4 text-gray-700">
                    {utilisateur.email}
                  </td>

                  <td className="px-6 py-4">

                    <div className="flex justify-center gap-2">

                      <button
                        onClick={() =>
                          onView(
                            utilisateur.id_utilisateur
                          )
                        }
                        className="px-3 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 shadow-sm transition-all duration-200"
                        title="Consulter"
                      >
                        👁
                      </button>

                      {/* Modifier */}
                      <button
                        onClick={() =>
                          onUpdate(utilisateur)
                        }
                        className="px-3 py-2 bg-amber-500 text-white rounded-lg hover:bg-amber-600 shadow-sm transition-all duration-200"
                        title="Modifier"
                      >
                        ✏️
                      </button>

                      {/* Supprimer */}
                      <button
                        onClick={() =>
                          onDelete(
                            utilisateur.id_utilisateur,
                            utilisateur.nom,
                            utilisateur.prenom
                          )
                        }
                        className="px-3 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 shadow-sm transition-all duration-200"
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