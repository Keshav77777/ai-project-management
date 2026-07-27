from project_management_agent.services.rag_service import rag_service


def upload_document(pdf_path: str) -> str:
    return rag_service.index_document(pdf_path)