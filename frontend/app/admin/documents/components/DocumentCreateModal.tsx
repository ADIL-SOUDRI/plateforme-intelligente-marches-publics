"use client"; 
 
import { useState } from "react"; 
 
import { 
  createDocument, 
} from "@/services/adminDocumentService"; 
 
import { DocumentReference } from "@/types/document"; 
 
interface Props { 
  open: boolean; 
  onClose: () => void; 
  onCreated: (document: DocumentReference) => void; 
} 
 
export default function DocumentCreateModal({ 
  open, 
  onClose, 
  onCreated, 
}: Props) { 
 
  const [titre, setTitre] = useState(""); 
  const [type, setType] = useState(""); 
  const [fichier, setFichier] = useState<File | null>(null); 
  const [loading, setLoading] = useState(false); 
  const [erreur, setErreur] = useState(""); 
 
  if (!open) { 
    return null; 
  } 
 
  async function handleCreate() { 
 
    setErreur(""); 
 
    if (!titre.trim()) { 
      setErreur("Le titre est obligatoire."); 
      return; 
    } 
 
    if (!type) { 
      setErreur("Veuillez sélectionner un type."); 
      return; 
    } 
 
    if (!fichier) { 
      setErreur("Veuillez sélectionner un fichier PDF."); 
      return; 
    } 
 
    if (fichier.type !== "application/pdf") { 
      setErreur("Seuls les fichiers PDF sont acceptés."); 
      return; 
    } 
 
    try { 
 
      setLoading(true); 
 
      const formData = new FormData(); 
 
      formData.append("titre", titre); 
      formData.append("type", type); 
      formData.append("fichier", fichier); 
 
      const nouveauDocument = await createDocument(formData); 
 
      onCreated(nouveauDocument); 
 
      setTitre(""); 
      setType(""); 
      setFichier(null); 
 
      onClose(); 
 
    } catch (error) { 
 
      console.error(error); 
 
      setErreur( 
        error instanceof Error 
          ? error.message 
          : "Erreur lors de l'ajout" 
      ); 
 
    } finally { 
      setLoading(false); 
    } 
  } 
 
  return ( 
 
    <div className="fixed inset-0 bg-gray-900/50 backdrop-blur-sm flex items-center justify-center z-50"> 
 
      <div className="bg-white rounded-xl p-6 w-full max-w-md shadow-2xl border border-gray-200"> 
 
        <h2 className="text-xl font-bold mb-5 text-gray-800"> 
          Ajouter un document 
        </h2> 
 
        {erreur && ( 
 
          <div className="mb-4 bg-red-50 border border-red-200 text-red-600 p-3 rounded-lg text-sm"> 
            {erreur} 
          </div> 
 
        )} 
 
        <div className="space-y-4"> 

 
          <div> 
 
            <label className="block text-sm font-medium text-gray-700 mb-1"> 
              Titre 
            </label> 
 
            <input 
              type="text" 
              value={titre} 
              onChange={(e) => setTitre(e.target.value)} 
              placeholder="Ex : CCAG Fournitures" 
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 placeholder-gray-400 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100" 
            /> 
 
          </div> 
 
 
          <div> 
 
            <label className="block text-sm font-medium text-gray-700 mb-1"> 
              Type 
            </label> 
 
            <select 
              value={type} 
              onChange={(e) => setType(e.target.value)} 
              className="w-full border border-gray-200 bg-gray-50 text-gray-800 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100" 
            > 
 
              <option value="" className="text-gray-400"> 
                Sélectionner un type 
              </option> 
 
              <option value="CCAG"> 
                CCAG 
              </option> 
 
              <option value="DECRET"> 
                Décret 
              </option> 
 
              <option value="CPS"> 
                CPS 
              </option> 
 
              <option value="GUIDE"> 
                Guide 
              </option> 
 
            </select> 
 
          </div> 
 

 
          <div> 
 
            <label className="block text-sm font-medium text-gray-700 mb-1"> 
              Fichier PDF 
            </label> 
 
            <input 
              type="file" 
              accept=".pdf,application/pdf" 
              onChange={(e) => 
                setFichier(e.target.files?.[0] || null) 
              } 
              className="w-full border border-gray-200 bg-gray-50 text-gray-600 rounded-lg px-4 py-2 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 file:mr-4 file:rounded-md file:border-0 file:bg-blue-50 file:px-3 file:py-1.5 file:text-sm file:font-medium file:text-blue-600 hover:file:bg-blue-100" 
            /> 
 
          </div> 
 
        </div> 
 
        <div className="flex justify-end gap-3 mt-6"> 
 
          <button 
            onClick={onClose} 
            disabled={loading} 
            className="px-4 py-2 bg-gray-100 text-gray-700 border border-gray-200 rounded-lg hover:bg-gray-200 transition-colors" 
          > 
            Annuler 
          </button> 
 
          <button 
            onClick={handleCreate} 
            disabled={loading} 
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 shadow-sm transition-colors disabled:bg-blue-300" 
          > 
            {loading ? "Traitement..." : "Ajouter"} 
          </button> 
 
        </div> 
 
      </div> 
 
    </div> 
  ); 
}