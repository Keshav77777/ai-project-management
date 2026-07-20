from google import genai

from project_management_agent.config import GOOGLE_API_KEY,MODEL_NAME_FOR_GENERATING_ANSWERS
from project_management_agent.prompts.rag_prompt import RAG_PROMPT

class LLMService:
    """
    Handles interactions with the Gemini LLM.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model = MODEL_NAME_FOR_GENERATING_ANSWERS

    def generate_answer(
        self,
        question: str,
        context: list[str],
    ) -> str:
        """
        Generate an answer using retrieved context.
        """

        context_text = "\n\n".join(context)
        prompt = RAG_PROMPT.format(
        context=context_text,
        question=question,
        )



        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text