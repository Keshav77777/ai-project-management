from project_management_agent.services.rag_service import rag_service


def ask_document(
    question: str,
    top_k: int = 3,
) -> str:
    """
    Ask a question about the uploaded documents.

    Args:
        question: User's question.
        top_k: Number of chunks to retrieve.

    Returns:
        Answer generated from retrieved context.
    """
    print(">>> ask_document called")

    return rag_service.ask(
        question=question,
        top_k=top_k,
    )