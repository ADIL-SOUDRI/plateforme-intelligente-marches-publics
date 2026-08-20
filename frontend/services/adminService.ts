import { Administrateur } from "@/types/auth";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getCurrentAdmin(): Promise<Administrateur> {
  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Administrateur non connecté");
  }

  const response = await fetch(`${API_URL}/admin/me`, {
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
        : "Impossible de récupérer le profil administrateur"
    );
  }

  return result;
}