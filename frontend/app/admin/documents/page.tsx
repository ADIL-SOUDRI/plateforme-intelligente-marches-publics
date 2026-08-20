"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import AdminNavbar from "@/components/admin/AdminNavbar";
import AdminSidebar from "@/components/admin/AdminSidebar";

import {
  getCurrentAdmin,
} from "@/services/adminService";

import {
  getAllDocuments,
  getDocument,
  deleteDocument,
} from "@/services/adminDocumentService";

import { DocumentReference } from "@/types/document";

import DocumentCreateModal from "./components/DocumentCreateModal";
import DocumentViewModal from "./components/DocumentViewModal";
import DocumentUpdateModal from "./components/DocumentUpdateModal";


export default function AdminDocumentsPage() {

  const router = useRouter();

  const [admin, setAdmin] =
    useState<any>(null);


  const [documents, setDocuments] =
    useState<DocumentReference[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [erreur, setErreur] =
    useState("");


  const [
    documentSelectionne,
    setDocumentSelectionne,
  ] =
    useState<DocumentReference | null>(null);

  const [showCreateModal, setShowCreateModal] =
    useState(false);

  const [showViewModal, setShowViewModal] =
    useState(false);

  const [showUpdateModal, setShowUpdateModal] =
    useState(false);


  useEffect(() => {

    async function chargerDonnees() {

      const token =
        localStorage.getItem("access_token");


      if (!token) {

        router.replace("/");

        return;
      }


      try {

        const adminConnecte =
          await getCurrentAdmin();

        setAdmin(adminConnecte);


        const liste =
          await getAllDocuments();

        setDocuments(liste);


      } catch (error) {

        console.error(error);

        setErreur(
          error instanceof Error
            ? error.message
            : "Erreur lors du chargement"
        );


      } finally {

        setLoading(false);

      }

    }


    chargerDonnees();

  }, [router]);

  async function handleView(
    id: number
  ) {

    try {

      setErreur("");

      const document =
        await getDocument(id);

      setDocumentSelectionne(document);

      setShowViewModal(true);


    } catch (error) {

      console.error(error);

      setErreur(
        error instanceof Error
          ? error.message
          : "Erreur lors de la consultation"
      );

    }

  }

  async function handleEdit(
    document: DocumentReference
  ) {

    setDocumentSelectionne(document);

    setShowUpdateModal(true);

  }



  function handleCreated(
    nouveauDocument: DocumentReference
  ) {

    setDocuments(
      (anciensDocuments) => [
        ...anciensDocuments,
        nouveauDocument,
      ]
    );

    setShowCreateModal(false);

  }


 
  function handleUpdated(
    documentModifie: DocumentReference
  ) {

    setDocuments(
      (anciensDocuments) =>
        anciensDocuments.map(
          (document) =>
            document.id === documentModifie.id
              ? documentModifie
              : document
        )
    );

    setDocumentSelectionne(null);

    setShowUpdateModal(false);

  }



  async function handleDelete(
    document: DocumentReference
  ) {

    const confirmation =
      window.confirm(
        `Voulez-vous supprimer "${document.nom_fichier}" ?`
      );


    if (!confirmation) {
      return;
    }


    try {

      setErreur("");

      await deleteDocument(document.id);


      setDocuments(
        (anciensDocuments) =>
          anciensDocuments.filter(
            (item) =>
              item.id !== document.id
          )
      );


    } catch (error) {

      console.error(error);

      setErreur(
        error instanceof Error
          ? error.message
          : "Erreur lors de la suppression"
      );

    }

  }



  if (loading) {

    return (

      <main className="min-h-screen flex items-center justify-center bg-slate-50">

        <p className="text-slate-600">
          Chargement...
        </p>

      </main>

    );

  }


  if (!admin) {
    return null;
  }



  return (

    <div className="min-h-screen bg-slate-50">


      {/* =================================================
          NAVBAR
      ================================================= */}

      <AdminNavbar
        nomAdmin={`${admin.prenom} ${admin.nom}`}
        email={admin.email}
      />


      <div className="flex">


        <AdminSidebar />


        <main className="flex-1 p-8">


       
          <div className="flex justify-between items-center mb-8">

            <div>

              <h1 className="text-3xl font-bold text-slate-800">
                Gestion des documents
              </h1>

              <p className="text-slate-500 mt-2">
                Consultez et gérez les documents de référence.
              </p>

            </div>


      
            <button
              onClick={() =>
                setShowCreateModal(true)
              }
              className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-lg font-medium shadow-sm transition-colors"
            >
              ➕ Ajouter un document
            </button>

          </div>


     
          {erreur && (

            <div className="mb-6 bg-red-50 border border-red-200 text-red-700 p-4 rounded-lg">

              {erreur}

            </div>

          )}


          <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">

            <p className="text-slate-500">
              Nombre de documents
            </p>

            <p className="text-3xl font-bold text-blue-600 mt-2">
              {documents.length}
            </p>

          </div>


   
          <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">

            <div className="overflow-x-auto">

              <table className="w-full">


        
                <thead className="bg-slate-100">

                  <tr>

                    <th className="text-left px-6 py-4 text-sm font-semibold text-slate-600">
                      ID
                    </th>

                    <th className="text-left px-6 py-4 text-sm font-semibold text-slate-600">
                      Titre
                    </th>

                    <th className="text-left px-6 py-4 text-sm font-semibold text-slate-600">
                      Type
                    </th>

                    <th className="text-left px-6 py-4 text-sm font-semibold text-slate-600">
                      Fichier
                    </th>

                    <th className="text-left px-6 py-4 text-sm font-semibold text-slate-600">
                      Date
                    </th>

                    <th className="text-center px-6 py-4 text-sm font-semibold text-slate-600">
                      Actions
                    </th>

                  </tr>

                </thead>


         
                <tbody>

                  {documents.length === 0 ? (

                    <tr>

                      <td
                        colSpan={6}
                        className="text-center py-10 text-slate-500"
                      >
                        Aucun document trouvé.
                      </td>

                    </tr>

                  ) : (

                    documents.map(
                      (document) => (

                        <tr
                          key={document.id}
                          className="border-t border-slate-100 hover:bg-blue-50 transition-colors"
                        >


                          <td className="px-6 py-4 text-slate-600">

                            {document.id}

                          </td>


                          <td className="px-6 py-4 font-medium text-slate-800">

                            {document.titre || "-"}

                          </td>


                          <td className="px-6 py-4 text-slate-600">

                            {document.type || "-"}

                          </td>


                          <td className="px-6 py-4 text-slate-600">

                            <span className="break-all">

                              {document.nom_fichier}

                            </span>

                          </td>

                          <td className="px-6 py-4 text-slate-600">

                            {new Date(
                              document.date_ajout
                            ).toLocaleDateString(
                              "fr-FR"
                            )}

                          </td>


                          <td className="px-6 py-4">

                            <div className="flex justify-center gap-2">


                              <button
                                onClick={() =>
                                  handleView(
                                    document.id
                                  )
                                }
                                className="px-3 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors shadow-sm"
                                title="Consulter"
                              >
                                👁
                              </button>


                              <button
                                onClick={() =>
                                  handleEdit(
                                    document
                                  )
                                }
                                className="px-3 py-2 bg-amber-500 text-white rounded-lg hover:bg-amber-600 transition-colors shadow-sm"
                                title="Modifier"
                              >
                                ✏️
                              </button>


                              <button
                                onClick={() =>
                                  handleDelete(
                                    document
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

                      )
                    )

                  )}

                </tbody>

              </table>

            </div>

          </div>



          <DocumentCreateModal

            open={showCreateModal}

            onClose={() =>
              setShowCreateModal(false)
            }

            onCreated={
              handleCreated
            }

          />


          <DocumentViewModal

            open={showViewModal}

            document={
              documentSelectionne
            }

            onClose={() => {

              setShowViewModal(false);

              setDocumentSelectionne(
                null
              );

            }}

          />

          {showUpdateModal &&
            documentSelectionne && (

              <DocumentUpdateModal

                open={showUpdateModal}

                document={
                  documentSelectionne
                }

                idAdmin={
                  admin.id_admin
                }

                onClose={() => {

                  setShowUpdateModal(
                    false
                  );

                  setDocumentSelectionne(
                    null
                  );

                }}

                onUpdated={
                  handleUpdated
                }

              />

            )}


        </main>

      </div>

    </div>

  );

}