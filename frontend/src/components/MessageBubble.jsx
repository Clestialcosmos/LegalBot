import SourceCard from "./SourceCard";

function MessageBubble({
  sender,
  text,
  sources = [],
}) {

  const isUser = sender === "user";

  return (

    <div
      className={`animate-[fade_0.35s_ease] flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >

      <div
        className={`flex w-full max-w-full sm:max-w-[95%] lg:max-w-[82%] gap-3 sm:gap-4 ${
          isUser
            ? "flex-row-reverse"
            : "flex-row"
        }`}
      >

        {/* Avatar */}

        <div
          className={`flex h-10 w-10 sm:h-14 sm:w-14 shrink-0 items-center justify-center rounded-full shadow-lg ${
            isUser
              ? "bg-gradient-to-br from-violet-600 to-purple-600 text-white"
              : "bg-gradient-to-br from-violet-600 to-fuchsia-600 text-white"
          }`}
        >

          <span className="text-lg sm:text-2xl">

            {isUser ? "👤" : "🤖"}

          </span>

        </div>

        {/* Bubble */}

        <div
          className={`flex-1 rounded-2xl sm:rounded-[28px] px-4 py-4 sm:px-6 sm:py-5 shadow-lg transition-all duration-300 ${
            isUser
              ? "bg-gradient-to-r from-violet-600 to-purple-600 text-white"
              : "border border-violet-200 bg-white"
          }`}
        >

          <div
            className={`mb-2 sm:mb-3 text-xs sm:text-sm font-bold ${
              isUser
                ? "text-violet-100"
                : "text-violet-700"
            }`}
          >

            {isUser
              ? "You"
              : "⚖️ LegalBot"}

          </div>

          <div
            className={`whitespace-pre-wrap break-all text-sm sm:text-base leading-7 sm:leading-8 ${
              isUser
                ? "text-white"
                : "text-gray-800"
            }`}
          >

            {text}

          </div>

          {!isUser &&
            sources.length > 0 && (

              <div className="mt-5 sm:mt-6 border-t border-violet-200 pt-4 sm:pt-5">

                <div className="mb-3 sm:mb-4 flex items-center gap-2 text-sm font-bold text-violet-700">

                  📚 Sources

                </div>

                <div className="space-y-2 sm:space-y-3">

                  {[
                    ...new Map(
                      sources.map((item) => [
                        `${item.source}-${item.page}`,
                        item,
                      ])
                    ).values(),
                  ].map((source, index) => (

                    <SourceCard
                      key={index}
                      source={source}
                    />

                  ))}

                </div>

              </div>

            )}

        </div>

      </div>

    </div>

  );

}

export default MessageBubble;