import { Utilisateur } from "@/types/auth";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

console.log("API_URL =", API_URL);

export async function getCurrentUser(): Promise<Utilisateur> {
  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(`${API_URL}/users/me`, {
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
        : "Impossible de récupérer le profil utilisateur"
    );
  }

  return result;
}