export interface DocumentReference {
  id: number;
  nom_fichier: string;
  taille: number;
  chemin_fichier?: string | null;
  date_ajout: string;
  id_admin: number;

  titre?: string;
  type?: string;
}

export interface DocumentReferenceCreate {
  titre: string;
  type: string;
}

export interface DocumentReferenceUpdate {
  titre: string;
  type: string;
  id_admin: number;
}