from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load and return the Hugging Face embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
    )