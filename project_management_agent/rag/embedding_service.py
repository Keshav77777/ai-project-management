from google import genai

from project_management_agent.config import GOOGLE_API_KEY


class EmbeddingService:
    """
    Generates embeddings using Google's Gemini Embedding API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model = "gemini-embedding-001"

    def embed_text(self, text: str) -> list[float]:
        """
        Generate an embedding for a single piece of text.
        """

        response = self.client.models.embed_content(
            model=self.model,
            contents=text,
        )

        return response.embeddings[0].values