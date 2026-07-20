from project_management_agent.rag.embedding_service import EmbeddingService
from project_management_agent.rag.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant document chunks for a user question.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
    ) -> list[str]:
        """
        Retrieve the most relevant document chunks.
        """

        query_embedding = self.embedding_service.embed_text(question)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        return results["documents"][0]