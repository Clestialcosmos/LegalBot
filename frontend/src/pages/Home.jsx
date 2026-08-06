import { useState } from "react";

import Navbar from "../components/Navbar";
import EmptyChat from "../components/EmptyChat";
import ChatWindow from "../components/ChatWindow";
import InputBox from "../components/InputBox";
import LegalBotMascot from "../components/LegalBotMascot";

import { askQuestion } from "../services/api";

function Home() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const showLanding = messages.length === 0;

  async function handleSend(text) {
    if (!text.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text,
      },
    ]);

    setLoading(true);

    try {
      const response = await askQuestion(text);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.answer,
          sources: response.sources || [],
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to LegalBot.",
          sources: [],
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleNewChat() {
    setMessages([]);
    setLoading(false);
  }

  return (
    <div className="relative min-h-screen overflow-hidden bg-gradient-to-br from-violet-50 via-white to-purple-100">

      {/* Background */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -left-24 top-10 h-64 w-64 sm:h-80 sm:w-80 rounded-full bg-violet-300/20 blur-3xl"></div>

        <div className="absolute right-0 top-40 h-72 w-72 sm:h-[420px] sm:w-[420px] rounded-full bg-fuchsia-300/20 blur-3xl"></div>

        <div className="absolute bottom-0 left-1/3 h-64 w-64 sm:h-80 sm:w-80 rounded-full bg-purple-300/20 blur-3xl"></div>
      </div>

      <Navbar onNewChat={handleNewChat} />

      <main className="relative z-10 mx-auto flex min-h-[calc(100vh-64px)] sm:min-h-[calc(100vh-80px)] max-w-7xl flex-col px-4 sm:px-6 py-4 sm:py-6">

        {showLanding ? (
          <>
            {/* Hero */}
            <section className="rounded-3xl sm:rounded-[36px] border border-violet-200 bg-white/80 p-5 sm:p-8 shadow-xl backdrop-blur-xl">

              <div className="grid items-center gap-8 lg:grid-cols-2">

                {/* Left */}
                <div>

                  <span className="inline-flex rounded-full bg-violet-100 px-3 py-2 sm:px-4 text-xs sm:text-sm font-semibold text-violet-700">
                    ⚖️ AI Powered Legal Assistant
                  </span>

                  <h1 className="mt-5 text-3xl sm:text-4xl lg:text-5xl font-black leading-tight text-gray-900">
                    Understand
                    <span className="bg-gradient-to-r from-violet-700 to-fuchsia-600 bg-clip-text text-transparent">
                      {" "}Indian Laws
                    </span>
                    <br />
                    with Confidence
                  </h1>

                  <p className="mt-5 max-w-xl text-base sm:text-lg leading-7 sm:leading-8 text-gray-600">
                    Ask legal questions in English or Hindi.
                    Receive AI-powered answers backed by legal documents.
                  </p>

                  <div className="mt-6 flex flex-wrap gap-3">
                    <span className="rounded-full bg-violet-100 px-3 py-2 text-sm font-semibold text-violet-700">
                      📚 Verified Sources
                    </span>

                    <span className="rounded-full bg-violet-100 px-3 py-2 text-sm font-semibold text-violet-700">
                      🌐 English • Hindi
                    </span>

                    <span className="rounded-full bg-violet-100 px-3 py-2 text-sm font-semibold text-violet-700">
                      🔒 Private & Secure
                    </span>
                  </div>

                </div>

                {/* Right */}
                <div className="flex justify-center">
                  <LegalBotMascot />
                </div>

              </div>

            </section>

            {/* Suggestions */}
            <section className="mt-5 sm:mt-6">
              <EmptyChat onSend={handleSend} />
            </section>

            {/* Input */}
            <div className="mt-5 sm:mt-6 rounded-3xl border border-violet-200 bg-white p-4 sm:p-5 shadow-xl">
              <InputBox onSend={handleSend} />
            </div>

          </>
        ) : (
          <>
            {/* Chat */}
            <div className="flex-1 overflow-hidden rounded-3xl border border-violet-200 bg-white shadow-xl">
              <ChatWindow
                messages={messages}
                loading={loading}
              />
            </div>

            {/* Input */}
            <div className="mt-5 sm:mt-6 rounded-3xl border border-violet-200 bg-white p-4 sm:p-5 shadow-xl">
              <InputBox onSend={handleSend} />
            </div>
          </>
        )}

      </main>
    </div>
  );
}

export default Home;