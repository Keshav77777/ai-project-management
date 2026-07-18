from chromadb import PersistentClient
from chromadb.api.models.Collection import Collection


class VectorStore:
    """
    Handles all interactions with ChromaDB.
    """

    def __init__(self):
        self.client = PersistentClient(
            path="project_management_agent/knowledge/chroma_db"
        )

        self.collection: Collection = self.client.get_or_create_collection(
            name="project_documents"
        )
    def add_documents(
    self,
    ids: list[str],
    documents: list[str],
    embeddings: list[list[float]],
    ):
        """
        Store documents and their embeddings.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
        )

    def search(
    self,
    query_embedding: list[float],
    top_k: int = 3,
    ):
        """
        Retrieve the most similar documents.
        """
    
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )