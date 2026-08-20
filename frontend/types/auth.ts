export interface RegisterRequest {
  nom: string;
  prenom: string;
  email: string;
  mot_de_passe: string;
}

export interface LoginRequest {
  email: string;
  mot_de_passe: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface Utilisateur {
  id_utilisateur: number;
  nom: string;
  prenom: string;
  email: string;
}
export interface Administrateur {
  id_admin: number;
  nom: string;
  prenom: string;
  email: string;
}