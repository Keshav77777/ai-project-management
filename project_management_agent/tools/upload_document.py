from pathlib import Path

from project_management_agent.memory.memory_manager import memory_manager
from project_management_agent.services.rag_service import rag_service


def upload_document(pdf_path: str) -> str:
    """
    Upload and index a PDF document.

    Args:
        pdf_path: Path to the PDF document.

    Returns:
        Success or failure message.
    """

    result = rag_service.index_document(pdf_path)

    # Store the document in memory only if indexing succeeded.
    if result.startswith("Indexed"):
        memory_manager.set_last_uploaded_document(
            Path(pdf_path).name
        )

    return (
        f"{result}\n\n"
        "Your document has been added to the knowledge base.\n"
        "You can now ask questions such as:\n"
        "- Summarize the document\n"
        "- What are the project risks?\n"
        "- What technologies are mentioned?"
    )