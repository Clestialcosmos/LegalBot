function TypingIndicator() {
  return (
    <div className="flex justify-start">

      <div className="flex items-end gap-3 sm:gap-4">

        {/* Avatar */}
        <div className="flex h-10 w-10 sm:h-14 sm:w-14 items-center justify-center rounded-full bg-gradient-to-br from-violet-600 to-fuchsia-600 text-lg sm:text-2xl text-white shadow-lg">
          🤖
        </div>

        {/* Bubble */}
        <div className="rounded-2xl sm:rounded-[28px] border border-violet-200 bg-white px-4 py-4 sm:px-6 sm:py-5 shadow-lg">

          <p className="mb-3 text-xs sm:text-sm font-bold text-violet-700">
            ⚖️ LegalBot
          </p>

          <div className="flex gap-2">

            <span className="h-2.5 w-2.5 sm:h-3 sm:w-3 animate-bounce rounded-full bg-violet-600"></span>

            <span className="h-2.5 w-2.5 sm:h-3 sm:w-3 animate-bounce rounded-full bg-violet-600 [animation-delay:0.2s]"></span>

            <span className="h-2.5 w-2.5 sm:h-3 sm:w-3 animate-bounce rounded-full bg-violet-600 [animation-delay:0.4s]"></span>

          </div>

        </div>

      </div>

    </div>
  );
}

export default TypingIndicator;