import uuid

from project_management_agent.rag.document_loader import DocumentLoader
from project_management_agent.rag.text_splitter import TextSplitter
from project_management_agent.rag.embedding_service import EmbeddingService
from project_management_agent.rag.vector_store import VectorStore
from project_management_agent.rag.retriever import Retriever
from project_management_agent.rag.llm_service import LLMService


class RagService:
    """
    Service layer responsible for orchestrating the RAG pipeline.

    Responsibilities:
    - Load documents
    - Split documents into chunks
    - Generate embeddings
    - Store embeddings in ChromaDB
    - Retrieve relevant document chunks
    """

    def __init__(self):
        self.document_loader = DocumentLoader()
        self.text_splitter = TextSplitter()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.retriever = Retriever()
        self.llm_service=LLMService()

    def index_document(self, pdf_path: str) -> str:
        """
        Load a PDF, split it into chunks, generate embeddings,
        and store them in ChromaDB.
        """

        # Load PDF
        documents = self.document_loader.load_pdf(pdf_path)

        # Split into chunks
        chunks = self.text_splitter.split_documents(documents)

        # Extract text
        texts = [chunk.page_content for chunk in chunks]

        # Generate embeddings
        embeddings = [
            self.embedding_service.embed_text(text)
            for text in texts
        ]

        # Generate unique IDs
        ids = [
            str(uuid.uuid4())
            for _ in texts
        ]

        # Metadata
        metadatas = [
            chunk.metadata
            for chunk in chunks
        ]

        # Store in ChromaDB
        self.vector_store.add_documents(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        return f"Indexed {len(texts)} document chunks successfully."

    def ask(
        self,
        question: str,
        top_k: int = 3,
    ) -> str:
        """
        Retrieve relevant document chunks and generate
        an answer using the Gemini LLM.
        """

        context = self.retriever.retrieve(
            question=question,
            top_k=top_k,
            )

        answer = self.llm_service.generate_answer(
        question=question,
        context=context,
        )

        return answer


rag_service = RagService()