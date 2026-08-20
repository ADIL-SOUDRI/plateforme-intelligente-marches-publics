// import { NextResponse } from "next/server";
// import type { NextRequest } from "next/server";

// export function middleware(request: NextRequest) {
//   const token = request.cookies.get("access_token")?.value;

//   const pathname = request.nextUrl.pathname;

//   const routesProtegees = [
//     "/dashboard",
//     "/chat",
//     "/documents",
//     "/historique",
//     "/profil",
//   ];

//   const routeProtegee = routesProtegees.some(
//     (route) =>
//       pathname === route ||
//       pathname.startsWith(route + "/")
//   );

//   // Pas connecté → login
//   if (routeProtegee && !token) {
//     return NextResponse.redirect(
//       new URL("/login", request.url)
//     );
//   }

//   // Déjà connecté → ne pas retourner au login
// //   if (pathname === "/login" && token) {
// //     return NextResponse.redirect(
// //       new URL("/dashboard", request.url)
// //     );
// //   }

//   return NextResponse.next();
// }

// export const config = {
//   matcher: [
//     "/dashboard/:path*",
//     "/chat/:path*",
//     "/documents/:path*",
//     "/historique/:path*",
//     "/profil/:path*",
//     "/login",
//   ],
// };

import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {

  const token = request.cookies.get("access_token")?.value;

  const pathname = request.nextUrl.pathname;

  const routesProtegees = [
    "/dashboard",
    "/chat",
    "/documents",
    "/historique",
    "/profil",
  ];

  const routeProtegee = routesProtegees.some(
    (route) =>
      pathname === route ||
      pathname.startsWith(route + "/")
  );

  if (routeProtegee && !token) {

    return NextResponse.redirect(
      new URL("/login", request.url)
    );

  }


  return NextResponse.next();
}

export const config = {

  matcher: [
    "/dashboard/:path*",
    "/chat/:path*",
    "/documents/:path*",
    "/historique/:path*",
    "/profil/:path*",
  ],

};