import { useEffect, useRef } from "react";

import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";

function ChatWindow({
  messages,
  loading,
}) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, loading]);

  return (
    <div className="h-full overflow-y-auto bg-gradient-to-b from-violet-50 via-white to-violet-100">

      <div className="mx-auto flex w-full max-w-5xl flex-col gap-5 sm:gap-6 lg:gap-8 px-3 sm:px-5 lg:px-6 py-5 sm:py-8">

        {messages.map((message, index) => (
          <MessageBubble
            key={index}
            sender={message.sender}
            text={message.text}
            sources={message.sources}
          />
        ))}

        {loading && <TypingIndicator />}

        <div ref={bottomRef} />

      </div>

    </div>
  );
}

export default ChatWindow;