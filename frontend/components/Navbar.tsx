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
    <header className="h-16 bg-white border-b flex items-center justify-between px-6">

      <div className="text-xl font-bold text-gray-800">
        Marchés Publics
      </div>

      <div className="relative">

        <button
          type="button"
          onClick={() => setProfilOuvert(!profilOuvert)}
          className="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
        >
          <span className="text-xl">
            👤
          </span>

          <span className="font-medium">
            {nomUtilisateur}
          </span>

          <span className="text-sm">
            ▼
          </span>
        </button>

        {profilOuvert && (
          <div className="absolute right-0 top-full mt-2 w-72 bg-white border border-gray-200 rounded-xl shadow-lg p-4 z-50">

            <div className="flex items-center gap-3">

              <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-xl">
                👤
              </div>

              <div>

                <p className="font-semibold text-gray-800">
                  {nomUtilisateur}
                </p>

                <p className="text-sm text-gray-500">
                  {email}
                </p>

              </div>

            </div>


            <hr className="my-4" />


            {/* Profil */}
            <button
        type="button"
        onClick={() => router.push("/dashboard/profile")}
        className="w-full text-left px-3 py-2 rounded-lg hover:bg-gray-100"
        >
        👤 Mon profil
        </button>

            <button
              type="button"
              onClick={handleLogout}
              className="w-full text-left px-3 py-2 rounded-lg hover:bg-gray-100 text-red-600"
            >
            </button>

          </div>
        )}

      </div>

    </header>
  );
}