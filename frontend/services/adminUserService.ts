import { Utilisateur } from "@/types/auth";

const API_URL = process.env.NEXT_PUBLIC_API_URL;


export async function getAllUsers(): Promise<Utilisateur[]> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(`${API_URL}/users`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Impossible de récupérer les utilisateurs"
    );
  }

  return result;
}



export async function getUser(
  id: number
): Promise<Utilisateur> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/users/${id}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Impossible de récupérer l'utilisateur"
    );
  }

  return result;
}



export async function createUser(data: {
  nom: string;
  prenom: string;
  email: string;
  mot_de_passe: string;
}): Promise<Utilisateur> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(`${API_URL}/users`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },

    body: JSON.stringify(data),
  });

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Impossible de créer l'utilisateur"
    );
  }

  return result;
}



export async function updateUser(
  id: number,
  data: {
    nom: string;
    prenom: string;
    email: string;
    mot_de_passe: string;
  }
): Promise<Utilisateur> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/users/${id}`,
    {
      method: "PUT",

      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },

      body: JSON.stringify(data),
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Impossible de modifier l'utilisateur"
    );
  }

  return result;
}



export async function deleteUser(
  id: number
): Promise<Utilisateur> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/users/${id}`,
    {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Impossible de supprimer l'utilisateur"
    );
  }

  return result;
}