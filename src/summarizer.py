import os

from google import genai
from google.genai.types import GenerateContentConfig


class Summarizer:
    def __init__(self, model_id: str = "gemini-2.0-flash-exp") -> None:
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_id = model_id

    def __call__(self, text: str) -> str:
        return self._generate_summary(text)

    def _create_prompt(self, text: str) -> str:
        return f"summarize: {text}"

    def _generate_summary(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=GenerateContentConfig(
                response_modalities=["TEXT"],
            ),
        )

        return response.candidates[0].content.parts
