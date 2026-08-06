function SourceCard({ source }) {
  const fileName =
    source?.source
      ?.split("\\")
      .pop()
      ?.replace(".pdf", "")
      ?.replace(".json", "")
      ?.replaceAll("_", " ") ||
    "Unknown Document";

  const act = source?.act;
  const section = source?.section;

  return (
    <div className="rounded-2xl border border-violet-200 bg-violet-50 p-4 sm:p-5 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-violet-400 hover:shadow-lg">

      <div className="flex items-start gap-3 sm:gap-4">

        {/* Icon */}
        <div className="flex h-10 w-10 sm:h-12 sm:w-12 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-violet-600 to-purple-600 text-lg sm:text-xl text-white shadow">
          📚
        </div>

        {/* Content */}
        <div className="min-w-0 flex-1">

          <h3 className="break-words text-sm sm:text-base font-bold text-violet-800">
            {fileName}
          </h3>

          {act && act !== "Unknown Act" && (
            <p className="mt-2 break-words text-xs sm:text-sm text-gray-700">
              <span className="font-semibold text-violet-700">
                Act:
              </span>{" "}
              {act}
            </p>
          )}

          {section && section !== "-" && (
            <p className="mt-1 break-words text-xs sm:text-sm text-gray-700">
              <span className="font-semibold text-violet-700">
                Section:
              </span>{" "}
              {section}
            </p>
          )}

          <p className="mt-1 text-xs sm:text-sm text-gray-700">
            <span className="font-semibold text-violet-700">
              Page:
            </span>{" "}
            {source.page ?? "-"}
          </p>

        </div>

      </div>

    </div>
  );
}

export default SourceCard;