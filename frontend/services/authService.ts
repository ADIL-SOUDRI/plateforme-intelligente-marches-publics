const API_URL = process.env.NEXT_PUBLIC_API_URL;

console.log("API_URL =", API_URL);

export async function registerUser(data: {
  nom: string;
  prenom: string;
  email: string;
  mot_de_passe: string;
}) {
  console.log("URL register =", `${API_URL}/auth/register`);

  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await response.json();

  if (!response.ok) {
    throw new Error( result.detail || "Erreur lors de l'inscription"  );
  }

  return result;
}
export async function loginUser(data: {
  email: string;
  mot_de_passe: string;
  role: string;
}) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await response.json();

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string" ? result.detail: "Email, mot de passe ou rôle incorrect");
  }

  return result;
}