"use client";

export default function Loading() {
  return (
    <div className="flex justify-start mb-4">
      <div className="bg-gray-100 rounded-2xl px-4 py-3">
        <p className="text-gray-500">
          Assistant est en train de réfléchir...
        </p>
      </div>
    </div>
  );
}