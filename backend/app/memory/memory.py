from collections import deque


class ConversationMemory:
    """
    Stores recent conversation history.

    Keeps only the latest N messages to avoid
    sending excessively large prompts to the LLM.
    """

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self._messages = deque(maxlen=max_messages)

    def add(self, role: str, content: str):
        """
        Add a message to memory.

        Parameters
        ----------
        role : str
            "user" or "assistant"

        content : str
            Message content
        """

        if not content:
            return

        self._messages.append(
            {
                "role": role,
                "content": content.strip(),
            }
        )

    def history(self):
        """
        Return conversation history.
        """

        return list(self._messages)

    def clear(self):
        """
        Clear all stored messages.
        """

        self._messages.clear()

    def last_user_message(self):
        """
        Return the latest user message.
        """

        for message in reversed(self._messages):
            if message["role"] == "user":
                return message["content"]

        return None

    def last_assistant_message(self):
        """
        Return the latest assistant message.
        """

        for message in reversed(self._messages):
            if message["role"] == "assistant":
                return message["content"]

        return None

    def __len__(self):
        return len(self._messages)