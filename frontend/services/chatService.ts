import { MessageResponse } from "@/types/chat";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function poserQuestion(
  question: string
): Promise<MessageResponse> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(`${API_URL}/chats-ss`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,
    },

    body: JSON.stringify({
      question: question,
    }),
  });

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Erreur lors de la communication avec l'assistant"
    );
  }

  return result;
}


export async function getHistoriqueUtilisateur(
  idUtilisateur: number
): Promise<MessageResponse[]> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/chats/utilisateur/${idUtilisateur}`,
    {
      method: "GET",

      headers: {
        "Authorization": `Bearer ${token}`,
      },
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Erreur lors de la récupération de l'historique"
    );
  }

  return result;
}
export async function getChat(
  id: number
): Promise<MessageResponse> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/chats/${id}`,
    {
      method: "GET",

      headers: {
        "Authorization": `Bearer ${token}`,
      },
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Erreur lors de la récupération du chat"
    );
  }

  return result;
}