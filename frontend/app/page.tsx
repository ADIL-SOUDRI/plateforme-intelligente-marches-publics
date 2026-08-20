"use client";

import { useRouter } from "next/navigation";

export default function Home() {

  const router = useRouter();

  return (
    <main className="min-h-screen bg-gray-100 flex flex-col items-center justify-center px-6">

      {/* Titre */}
      <div className="text-center mb-10">

        <h1 className="text-4xl font-bold text-gray-800">
          Marchés Publics
        </h1>

        <p className="mt-3 text-gray-600">
          Plateforme intelligente d'assistance aux marchés publics
        </p>

      </div>


      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-3xl">



        <div className="bg-white rounded-2xl shadow-lg p-8 text-center">

          <div className="text-5xl mb-5">
            👤
          </div>

          <h2 className="text-2xl font-bold text-gray-800">
            Utilisateur
          </h2>

          <p className="text-gray-500 mt-3 mb-6">
            Accédez à l'assistant intelligent,
            consultez vos documents et votre historique.
          </p>

          <button
            onClick={() => router.push("/login")}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg transition"
          >
            Se connecter
          </button>

        </div>



        <div className="bg-white rounded-2xl shadow-lg p-8 text-center">

          <div className="text-5xl mb-5">
            🛡️
          </div>

          <h2 className="text-2xl font-bold text-gray-800">
            Administrateur
          </h2>

          <p className="text-gray-500 mt-3 mb-6">
            Gérez les utilisateurs, les documents
            et la plateforme.
          </p>

          <button
            onClick={() => router.push("/admin/login")}
            className="w-full bg-gray-800 hover:bg-gray-900 text-white py-3 rounded-lg transition"
          >
            Se connecter
          </button>

        </div>

      </div>

    </main>
  );
}