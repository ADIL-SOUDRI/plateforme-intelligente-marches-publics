"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import AdminNavbar from "@/components/admin/AdminNavbar";
import AdminSidebar from "@/components/admin/AdminSidebar";

import { getCurrentAdmin } from "@/services/adminService";
import {
  getAllUsers,
  getUser,
  createUser,
  updateUser,
  deleteUser,
} from "@/services/adminUserService";

import { Utilisateur } from "@/types/auth";

import UserTable from "@/components/admin/UtilisateursTable";
import UserViewModal from "@/components/admin/UtilisateurViewModal";
import UserCreateModal from "@/components/admin/UserCreateModal";
import UserUpdateModal from "@/components/admin//UtilisateurUpdateModal";


export default function AdminUtilisateursPage() {
  const router = useRouter();

  const [admin, setAdmin] = useState<any>(null);

  const [utilisateurs, setUtilisateurs] =
    useState<Utilisateur[]>([]);

  const [loading, setLoading] = useState(true);

  const [erreur, setErreur] = useState("");

  const [utilisateurSelectionne, setUtilisateurSelectionne] =
    useState<Utilisateur | null>(null);

  const [showViewModal, setShowViewModal] =
    useState(false);

  const [showCreateModal, setShowCreateModal] =
    useState(false);

  const [showUpdateModal, setShowUpdateModal] =
    useState(false);



  useEffect(() => {
    async function chargerDonnees() {
      const token = localStorage.getItem("access_token");

      if (!token) {
        router.replace("/admin/login");
        return;
      }

      try {
        const adminConnecte = await getCurrentAdmin();

        setAdmin(adminConnecte);

        const liste = await getAllUsers();

        setUtilisateurs(liste);
      } catch (error) {
        console.error(error);

        localStorage.removeItem("access_token");

        document.cookie =
          "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

        router.replace("/admin/login");
      } finally {
        setLoading(false);
      }
    }

    chargerDonnees();
  }, [router]);


  async function handleView(id: number) {
    try {
      setErreur("");

      const utilisateur = await getUser(id);

      setUtilisateurSelectionne(utilisateur);

      setShowViewModal(true);
    } catch (error) {
      console.error(error);

      if (error instanceof Error) {
        setErreur(error.message);
      }
    }
  }



  function ouvrirModification(utilisateur: Utilisateur) {
    setUtilisateurSelectionne(utilisateur);

    setShowUpdateModal(true);
  }

  async function handleUpdate(data: {
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
  }) {
    if (!utilisateurSelectionne) {
      return;
    }

    try {
      setErreur("");

      const utilisateurModifie = await updateUser(
        utilisateurSelectionne.id_utilisateur,
        data
      );

      setUtilisateurs((anciens) =>
        anciens.map((user) =>
          user.id_utilisateur ===
          utilisateurModifie.id_utilisateur
            ? utilisateurModifie
            : user
        )
      );

      setShowUpdateModal(false);

      setUtilisateurSelectionne(null);
    } catch (error) {
      console.error(error);

      if (error instanceof Error) {
        setErreur(error.message);
      } else {
        setErreur("Erreur lors de la modification");
      }
    }
  }

 

  function ouvrirCreation() {
    setErreur("");
    setShowCreateModal(true);
  }

  async function handleCreate(data: {
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
  }) {
    try {
      setErreur("");

      const nouvelUtilisateur =
        await createUser(data);

      setUtilisateurs((anciens) => [
        ...anciens,
        nouvelUtilisateur,
      ]);

      setShowCreateModal(false);
    } catch (error) {
      console.error(error);

      if (error instanceof Error) {
        setErreur(error.message);
      } else {
        setErreur("Erreur lors de la création");
      }
    }
  }

 

  async function handleDelete(
    id: number,
    nom: string,
    prenom: string
  ) {
    const confirmation = window.confirm(
      `Voulez-vous supprimer ${prenom} ${nom} ?`
    );

    if (!confirmation) {
      return;
    }

    try {
      setErreur("");

      await deleteUser(id);

      setUtilisateurs((anciens) =>
        anciens.filter(
          (user) => user.id_utilisateur !== id
        )
      );
    } catch (error) {
      console.error(error);

      if (error instanceof Error) {
        setErreur(error.message);
      } else {
        setErreur("Erreur lors de la suppression");
      }
    }
  }



  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-gray-50">
        <p className="text-gray-600">
          Chargement...
        </p>
      </main>
    );
  }

  if (!admin) {
    return null;
  }


  return (
    <div className="min-h-screen bg-gray-50">

      <AdminNavbar
        nomAdmin={`${admin.prenom} ${admin.nom}`}
        email={admin.email}
      />

      <div className="flex">

        <AdminSidebar />

        <main className="flex-1 p-8">


          <div className="flex justify-between items-center mb-8">

            <div>
              <h1 className="text-3xl font-bold text-gray-800">
                Gestion des utilisateurs
              </h1>

              <p className="text-gray-500 mt-2">
                Consultez et gérez les utilisateurs
                de la plateforme.
              </p>
            </div>

            {/* BOUTON AJOUTER CONSERVÉ */}

            <button
              onClick={ouvrirCreation}
              className="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700"
            >
              ➕ Ajouter utilisateur
            </button>

          </div>


          {erreur && (
            <div className="mb-6 bg-red-50 border border-red-100 text-red-600 p-4 rounded-lg">
              {erreur}
            </div>
          )}

          <UserTable
            utilisateurs={utilisateurs}
            onView={handleView}
            onUpdate={ouvrirModification}
            onDelete={handleDelete}
          />

 

          <UserViewModal
            utilisateur={utilisateurSelectionne}
            open={showViewModal}
            onClose={() => {
              setShowViewModal(false);
              setUtilisateurSelectionne(null);
            }}
          />


          <UserCreateModal
            open={showCreateModal}
            onClose={() => setShowCreateModal(false)}
            onCreate={handleCreate}
          />

          <UserUpdateModal
            utilisateur={utilisateurSelectionne}
            open={showUpdateModal}
            onClose={() => {
              setShowUpdateModal(false);
              setUtilisateurSelectionne(null);
            }}
            onUpdate={handleUpdate}
          />

        </main>
      </div>
    </div>
  );
}