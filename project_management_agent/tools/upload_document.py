from project_management_agent.services.rag_service import rag_service

def upload_document(pdf_path: str) -> str:
    result = rag_service.index_document(pdf_path)

    return (
        f"{result}\n\n"
        "Your document has been added to the knowledge base. "
        "You can now ask questions such as:\n"
        "- Summarize the document\n"
        "- What are the project risks?\n"
        "- What technologies are mentioned?"
    )