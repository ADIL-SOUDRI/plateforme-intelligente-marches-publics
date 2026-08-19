import { DocumentReference } from "@/types/document";


const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getDocumentsReferences(): Promise<
  DocumentReference[]
> {

  const token =
    localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/documents-references`,
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
        : "Erreur lors de la récupération des documents"
    );
  }

  return result;
}

export async function getDocumentReference(
  id: number
): Promise<DocumentReference> {

  const token =
    localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const response = await fetch(
    `${API_URL}/documents-references/${id}`,
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
        : "Erreur lors de la récupération du document"
    );
  }

  return result;
}