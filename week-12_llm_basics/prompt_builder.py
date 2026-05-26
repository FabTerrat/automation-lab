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
