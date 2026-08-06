import { useState } from "react";

function InputBox({ onSend }) {
  const [message, setMessage] = useState("");

  function send() {
    const text = message.trim();

    if (!text) return;

    onSend(text);
    setMessage("");
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  return (
    <div className="flex flex-col gap-4 md:flex-row md:items-end">

      {/* Input */}
      <div className="relative flex-1">

        <textarea
          rows={2}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask your legal question..."
          className="min-h-[90px] max-h-48 w-full resize-y rounded-2xl sm:rounded-[28px] border border-violet-300 bg-violet-50 px-4 sm:px-6 py-4 sm:py-5 pr-14 sm:pr-16 text-sm sm:text-base text-gray-800 shadow-sm outline-none transition-all duration-300 placeholder:text-gray-400 focus:border-violet-500 focus:bg-white focus:ring-4 focus:ring-violet-100"
        />

        <div className="absolute bottom-4 right-4 sm:bottom-5 sm:right-5 text-xl sm:text-2xl">
          ⚖️
        </div>

      </div>

      {/* Button */}
      <button
        onClick={send}
        className="flex w-full md:w-auto items-center justify-center gap-2 rounded-2xl sm:rounded-[24px] bg-gradient-to-r from-violet-600 to-fuchsia-600 px-6 sm:px-8 py-4 sm:py-5 text-sm sm:text-base font-semibold text-white shadow-xl transition-all duration-300 hover:-translate-y-1 hover:shadow-violet-300 active:scale-95"
      >
        <span>Send</span>
        <span>➜</span>
      </button>

    </div>
  );
}

export default InputBox;