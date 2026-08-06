function EmptyChat({ onSend }) {
  const questions = [
    { icon: "🚓", text: "What is an FIR?" },
    { icon: "📄", text: "How do I file an RTI application?" },
    { icon: "💳", text: "A cyber fraud happened to me. What should I do?" },
    { icon: "🛒", text: "How can I file a consumer complaint?" },
    { icon: "⚖️", text: "What are my rights during police arrest?" },
    { icon: "📨", text: "How do I send a legal notice?" },
  ];

  return (
    <div className="flex h-full items-center justify-center overflow-y-auto px-4 sm:px-6 py-8 sm:py-10">

      <div className="w-full max-w-5xl">

        {/* Robot */}
        <div className="mb-8 sm:mb-10 flex justify-center">

          <div className="relative">

            <div className="absolute -right-2 -top-2 flex h-8 w-8 sm:h-10 sm:w-10 items-center justify-center rounded-full bg-green-500 text-sm sm:text-base text-white shadow-lg animate-pulse">
              ✓
            </div>

            <div className="flex h-28 w-28 sm:h-40 sm:w-40 items-center justify-center rounded-full bg-gradient-to-br from-violet-600 via-purple-500 to-fuchsia-500 shadow-2xl animate-[float_4s_ease-in-out_infinite]">

              <span className="text-5xl sm:text-7xl">
                🤖
              </span>

            </div>

          </div>

        </div>

        {/* Heading */}

        <h1 className="text-center text-3xl sm:text-5xl lg:text-6xl font-black text-gray-900">

          Welcome to{" "}

          <span className="bg-gradient-to-r from-violet-700 to-fuchsia-600 bg-clip-text text-transparent">
            LegalBot
          </span>

        </h1>

        <p className="mx-auto mt-5 max-w-3xl text-center text-base sm:text-lg lg:text-xl leading-7 sm:leading-9 text-gray-600">

          Your AI-powered legal assistant for Indian laws.

          <br className="hidden sm:block" />

          Ask legal questions, understand your rights,
          and receive grounded answers with legal sources.

        </p>

        {/* Pills */}

        <div className="mt-7 sm:mt-8 flex flex-wrap justify-center gap-3">

          {[
            "⚖️ Indian Laws",
            "📚 Source-backed",
            "🌐 Multilingual",
            "🛡 Privacy First",
          ].map((item) => (

            <div
              key={item}
              className="rounded-full bg-violet-100 px-4 py-2 sm:px-5 sm:py-3 text-sm font-semibold text-violet-700"
            >
              {item}
            </div>

          ))}

        </div>

        {/* Suggested Questions */}

        <div className="mt-10 sm:mt-14 grid gap-4 sm:gap-5 md:grid-cols-2 lg:grid-cols-3">

          {questions.map((q) => (

            <button
              key={q.text}
              onClick={() => onSend(q.text)}
              className="group rounded-2xl sm:rounded-3xl border border-violet-200 bg-white p-5 sm:p-6 text-left shadow-md transition-all duration-300 hover:-translate-y-2 hover:border-violet-400 hover:shadow-xl"
            >

              <div className="mb-4 flex h-12 w-12 sm:h-14 sm:w-14 items-center justify-center rounded-2xl bg-violet-100 text-2xl sm:text-3xl">

                {q.icon}

              </div>

              <h3 className="text-sm sm:text-base font-semibold leading-6 text-gray-800 group-hover:text-violet-700">

                {q.text}

              </h3>

            </button>

          ))}

        </div>

        {/* Disclaimer */}

        <div className="mt-10 sm:mt-12 rounded-2xl sm:rounded-3xl border border-violet-200 bg-violet-50 p-5 sm:p-6 text-center text-sm sm:text-base leading-7 text-gray-600">

          <span className="font-bold text-violet-700">
            Disclaimer:
          </span>{" "}

          LegalBot provides general legal information based on retrieved legal
          documents and does not replace advice from a qualified advocate.

        </div>

      </div>

    </div>
  );
}

export default EmptyChat;