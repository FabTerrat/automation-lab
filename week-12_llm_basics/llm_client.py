from abc import ABC, abstractmethod
import json

class LLMClient(ABC):

    @abstractmethod
    def analyze_lead(self, message):
        pass
    

class PromptBuilder:
    @staticmethod
    def build_lead_prompt(message):

        return f"""
            Tu es un assistant spécialisé dans la qualification de leads.

            Analyse le message suivant et retourne uniquement un JSON valide.

            Le JSON doit contenir exactement ces champs :
            - category : string
            - priority : Low, Medium ou High
            - score : integer entre 0 et 100
            - confidence : float entre 0 et 1
            - summary : string 
            - reason : string

            Critères :
            - Un besoin clair augmente le score
            - une urgence explicite augmente le score 
            - Un budget mentionné augmente le score
            - Un besoin lié à l'automation, au CRM, aux ventes ou aux opérations est pertinent


            Message : 
            {message}
            """


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