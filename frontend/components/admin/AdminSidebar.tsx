"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

export default function AdminSidebar() {

  const router = useRouter();

  function handleLogout() {

    localStorage.removeItem(
      "access_token"
    );

    document.cookie =
      "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";

    router.replace("/admin/login");
  }

  return (

    <aside className="w-64 min-h-[calc(100vh-4rem)] bg-gray-900 text-white p-4">

      <nav className="space-y-2">

        <Link
          href="/admin/dashboard"
          className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
          <span>🏠</span>
          <span>Dashboard</span>
        </Link>


        <Link
        href="/admin/utilisateurs"
        className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
        <span>👥</span>
        <span>Utilisateurs</span>
        </Link>


        <Link
          href="/admin/documents"
          className="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-800"
        >
          <span>📚</span>
          <span>Documents</span>
        </Link>


        <button
          onClick={handleLogout}
          className="w-full flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-red-800 text-left mt-6"
        >
          <span>🚪</span>
          <span>Déconnexion</span>
        </button>

      </nav>

    </aside>
  );
}
