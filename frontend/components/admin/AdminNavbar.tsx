"use client";

interface AdminNavbarProps {
  nomAdmin: string;
  email: string;
}

export default function AdminNavbar({
  nomAdmin,
  email,
}: AdminNavbarProps) {

  return (

    <header className="h-16 bg-white border-b flex items-center justify-between px-6">

      <h1 className="text-xl font-bold text-gray-800">
        Marchés Publics
      </h1>


      <div className="flex items-center gap-3">

        <div className="text-right">

          <p className="font-semibold text-gray-800">
            {nomAdmin}
          </p>

          <p className="text-sm text-gray-500">
            {email}
          </p>

        </div>

        <div className="w-10 h-10 rounded-full bg-gray-800 text-white flex items-center justify-center">
          🛡️
        </div>

      </div>

    </header>
  );
}