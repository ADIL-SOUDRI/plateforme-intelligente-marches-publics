"use client";

import { useEffect, useState } from "react";

import {
  getAllUsers,
  deleteUser,
} from "@/services/adminUserService";

import { Utilisateur } from "@/types/auth";

export function useAdminUsers() {

  const [utilisateurs, setUtilisateurs] =
    useState<Utilisateur[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [erreur, setErreur] =
    useState("");

  useEffect(() => {

    async function chargerUtilisateurs() {

      try {

        const liste = await getAllUsers();

        setUtilisateurs(liste);

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

    chargerUtilisateurs();

  }, []);


  async function supprimerUtilisateur(id: number) {

    const utilisateur =
      utilisateurs.find(
        (user) =>
          user.id_utilisateur === id
      );

    if (!utilisateur) {
      return;
    }

    const confirmation = window.confirm(
      `Voulez-vous supprimer ${utilisateur.prenom} ${utilisateur.nom} ?`
    );

    if (!confirmation) {
      return;
    }

    try {

      await deleteUser(id);

      setUtilisateurs(
        anciens =>
          anciens.filter(
            user =>
              user.id_utilisateur !== id
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


  return {
    utilisateurs,
    loading,
    erreur,
    supprimerUtilisateur,
  };
}