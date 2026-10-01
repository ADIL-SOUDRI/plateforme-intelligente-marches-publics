"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

interface NavbarProps {
  nomUtilisateur: string;
  email: string;
}

export default function Navbar({
  nomUtilisateur,
  email,
}: NavbarProps) {

  const router = useRouter();

  const [profilOuvert, setProfilOuvert] = useState(false);

  function handleLogout() {
    localStorage.removeItem("access_token");
    router.push("/login");
  }

  return (
    <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-6 shadow-sm">

      {/* Logo / Nom plateforme */}
      <div className="text-xl font-bold text-slate-800">
        Marchés <span className="text-blue-600">Publics</span>
      </div>

      <div className="relative">

        {/* Bouton utilisateur */}
        <button
          type="button"
          onClick={() => setProfilOuvert(!profilOuvert)}
          className="flex items-center gap-3 px-3 py-2 rounded-xl hover:bg-slate-50 transition duration-200"
        >

          <div className="w-9 h-9 rounded-full bg-blue-100 flex items-center justify-center">
            <span className="text-lg">
              👤
            </span>
          </div>

          <span className="font-medium text-slate-700">
            {nomUtilisateur}
          </span>

          <span className="text-xs text-slate-400">
            ▼
          </span>

        </button>

        {/* Menu profil */}
        {profilOuvert && (
          <div className="absolute right-0 top-full mt-2 w-72 bg-white border border-slate-200 rounded-xl shadow-xl p-4 z-50">

            {/* Informations utilisateur */}
            <div className="flex items-center gap-3">

              <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-xl">
                👤
              </div>

              <div className="min-w-0">

                <p className="font-semibold text-slate-800 truncate">
                  {nomUtilisateur}
                </p>

                <p className="text-sm text-slate-500 truncate">
                  {email}
                </p>

              </div>

            </div>

            <hr className="my-4 border-slate-200" />

            {/* Profil */}
            <button
              type="button"
              onClick={() => router.push("/dashboard/profile")}
              className="w-full text-left px-3 py-2.5 rounded-lg text-slate-700 hover:bg-blue-50 hover:text-blue-700 transition duration-200"
            >
              <span className="mr-2">👤</span>
              Mon profil
            </button>

            {/* Déconnexion */}
            <button
              type="button"
              onClick={handleLogout}
              className="w-full text-left px-3 py-2.5 rounded-lg text-red-600 hover:bg-red-50 hover:text-red-700 transition duration-200"
            >
              <span className="mr-2">↪</span>
              Déconnexion
            </button>

          </div>
        )}

      </div>

    </header>
  );
}