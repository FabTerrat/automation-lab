from abc import ABC, abstractmethod
import json

import os 
from dotenv import load_dotenv
from openai import OpenAI

from prompt_builder import PromptBuilder


class LLMClient(ABC):

    @abstractmethod
    def analyze_lead(self, message):
        pass
    

class FakeLLMClient(LLMClient):

    def analyze_lead(self, message):
        prompt = PromptBuilder.build_lead_prompt(message)

        raw_response = self._fake_api_call(prompt)

        return json.loads(raw_response)
    
    def _fake_api_call(self, prompt):
        """
        Simule la réponse texte d'une vrai API LLM.
        Une vrai api renvoie souvent du texte, qu'il faut ensuite parser.
        """

        return """
        {
            "category": "automation",
            "priority": "High",
            "score": 87,
            "confidence": 0.82,
            "summary": "Le prospect cherche à automatiser la qualification de ses prospects.",
            "reason": "Besoin clair, budget mentionné et urgence implicite."
        }
        """
    
class OpenAIClient(LLMClient):

    def __init__(self, model="gpt-4.1-mini"):
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY est manquante dans le fichier .env")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def analyze_lead(self, message):
        prompt = PromptBuilder.build_lead_prompt(message)

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        raw_response = response.output_text

        #Ici ces prints permettent de voir la sortie réel du LLM et faire le nettoyage adéquate si on a pas du JSON pur 
        print("\n --- RAW RESPONSE ---")
        print(repr(raw_response))
        print("--- END RAW RESPONSE ---\n")
        # --------------------------------------

        #Nettoyage pour obtenir un vrai JSON exploitable
        clean_response = raw_response.strip()

        if clean_response.startswith("```json"):
            clean_response = clean_response.removeprefix("```json").strip()

        if clean_response.startswith("```"):
            clean_response = clean_response.removeprefix("```").strip()

        if clean_response.endswith("```"):
            clean_response = clean_response.removesuffix("```").strip()
        # -------------------------------------------

        # ------------- Ou faire ------------
        #start = raw_response.find("{")
        #end = raw_response.rfind("}")
        #if start == -1 or end == -1:
            #raise ValueError("Aucun JSON détecté dans la réponse du LLM.")
        #
        # clean_response = raw_response[start:end + 1]

        print("\n --- Clean RESPONSE ---")
        print(repr(clean_response))
        print("--- END Clean RESPONSE ---\n")
        # --------------------------------------

        return json.loads(clean_response)