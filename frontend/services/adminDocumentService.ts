import { DocumentReference } from "@/types/document";

const API_URL = process.env.NEXT_PUBLIC_API_URL ;
// const API_URL = process.env.NEXT_PUBLIC_API_URL;


function getToken(): string | null {
  return localStorage.getItem("access_token");
}


async function getErrorMessage(
  response: Response
): Promise<string> {

  try {

    const data = await response.json();

    if (data?.detail) {
      return Array.isArray(data.detail)
        ? data.detail
            .map((error: any) => error.msg)
            .join(", ")
        : data.detail;
    }

  } catch {
    // Rien
  }

  return `Erreur HTTP ${response.status}`;
}


export async function getAllDocuments(): Promise<
  DocumentReference[]
> {

  const token = getToken();

  const response = await fetch(
    `${API_URL}/documents-references`,
    {
      method: "GET",

      headers: {
        Authorization: `Bearer ${token}`,
      },

      cache: "no-store",
    }
  );


  if (!response.ok) {

    throw new Error(
      await getErrorMessage(response)
    );

  }


  return response.json();
}

export async function getDocument(
  id: number
): Promise<DocumentReference> {

  const token = getToken();

  const response = await fetch(
    `${API_URL}/documents-references/${id}`,
    {
      method: "GET",

      headers: {
        Authorization: `Bearer ${token}`,
      },

      cache: "no-store",
    }
  );


  if (!response.ok) {

    throw new Error(
      await getErrorMessage(response)
    );

  }


  return response.json();
}

export async function createDocument(
  formData: FormData
): Promise<DocumentReference> {

  const token = getToken();

  const response = await fetch(
    `${API_URL}/documents-references`,
    {
      method: "POST",

      headers: {
        Authorization: `Bearer ${token}`,
      },

      body: formData,
    }
  );


  if (!response.ok) {

    throw new Error(
      await getErrorMessage(response)
    );

  }


  return response.json();
}
export async function updateDocument(
  id: number,
  data: {
    titre: string;
    type: string;
    id_admin: number;
  }
): Promise<DocumentReference> {

  const token = getToken();

  const response = await fetch(
    `${API_URL}/documents-references/${id}`,
    {
      method: "PUT",

      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },

      body: JSON.stringify(data),
    }
  );


  if (!response.ok) {

    throw new Error(
      await getErrorMessage(response)
    );

  }


  return response.json();
}

export async function deleteDocument(
  id: number
): Promise<void> {

  const token = getToken();

  const response = await fetch(
    `${API_URL}/documents-references/${id}`,
    {
      method: "DELETE",

      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );


  if (!response.ok) {

    throw new Error(
      await getErrorMessage(response)
    );

  }
}