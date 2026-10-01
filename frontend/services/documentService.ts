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
    `${API_URL}/documents-importes_by_utilisateur`,
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
export async function importerDocument(
  titre: string,
  type: string,
  fichier: File
): Promise<DocumentReference> {

  const token = localStorage.getItem("access_token");

  if (!token) {
    throw new Error("Utilisateur non connecté");
  }

  const formData = new FormData();

  formData.append("titre", titre);
  formData.append("type", type);
  formData.append("fichier", fichier);

  const response = await fetch(
    `${API_URL}/documents-importes`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "Erreur lors de l'importation du document"
    );
  }

  return result;
}