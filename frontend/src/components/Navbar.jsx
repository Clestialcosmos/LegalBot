function Navbar({ onNewChat }) {
  return (
    <header className="sticky top-0 z-50 border-b border-violet-200 bg-white/90 backdrop-blur-xl">
      <div className="mx-auto flex h-16 sm:h-20 max-w-7xl items-center justify-between px-4 sm:px-6">

        {/* Logo */}
        <div className="flex items-center gap-3 sm:gap-4 min-w-0">

          <div className="flex h-12 w-12 sm:h-16 sm:w-16 flex-shrink-0 items-center justify-center rounded-2xl sm:rounded-3xl bg-gradient-to-br from-violet-600 to-purple-600 shadow-xl transition duration-300 hover:rotate-6">
            <span className="text-2xl sm:text-4xl">
              ⚖️
            </span>
          </div>

          <div className="min-w-0">
            <h1 className="truncate bg-gradient-to-r from-violet-700 to-fuchsia-600 bg-clip-text text-2xl sm:text-4xl font-black text-transparent">
              LegalBot
            </h1>

            <p className="hidden sm:block truncate font-medium text-gray-500">
              AI-powered Legal Assistant for India 🇮🇳
            </p>
          </div>

        </div>

        {/* Right */}
        <div className="flex items-center gap-2 sm:gap-4">

          <div className="hidden xl:block rounded-full bg-violet-100 px-5 py-3 font-semibold text-violet-700 whitespace-nowrap">
            Powered by Hybrid RAG
          </div>

          <button
            onClick={onNewChat}
            className="rounded-xl sm:rounded-2xl bg-gradient-to-r from-violet-600 to-purple-600 px-3 py-2 sm:px-6 sm:py-3 text-sm sm:text-base font-semibold text-white shadow-xl transition duration-300 hover:-translate-y-1 hover:shadow-violet-300 whitespace-nowrap"
          >
            <span className="hidden sm:inline">
              + New Chat
            </span>

            <span className="sm:hidden">
              +
            </span>
          </button>

        </div>

      </div>
    </header>
  );
}

export default Navbar;