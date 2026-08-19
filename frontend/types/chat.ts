export interface Message {
  id: number;
  role: "user" | "assistant";
  contenu: string;
}

export interface MessageResponse {
  id: number;
  question: string;
  reponse: string;
  date_creation: string;
  id_utilisateur: number;
  id_admin: number | null;
  id_document_importe: number | null;
}