import json
from llm_client import FakeLLMClient

def fake_llm_analyze(message):
    """
    Simule une réponse de LLM.
    Plus tard, cette fonction sera remplacée par OpenAI, Claude, Gemini, etc.
    """

    return {
        "category":"automation",
        "priority":"High",
        "score": 87,
        "confidence": 0.82,
        "summary": "Le prospect chercher à automatiser des tâches répétitives liées à son activité.",
        "reason": "Besoin clair, urgence implicite et potentiel de valeur métier."
    }

def validate_llm_result(result):
    require_fields = [
        "category",
        "priority",
        "score",
        "confidence",
        "summary",
        "reason"
    ]

    for field in require_fields:
        if field not in result :
            raise ValueError(f"Champ manquant dans la réponse LLM : {field}")
    
    if not isinstance(result["score"], int):
        raise ValueError("Le score doit être un entier.")
    
    if result["score"] < 0 or result["score"] > 100 :
        raise ValueError("Le score doit être compris entre 0 et 100")
    
    if not isinstance(result["confidence"], float):
        raise ValueError("L'indice confidence doit être un nombre décimal.")
    
    if result["confidence"] < 0 or result["confidence"] > 1 :
        raise ValueError("L'indice confidence doit être compris entre 0 et 1")
    
    return True


def decide_next_action(result):
    confidence = result["confidence"]
    priority = result["priority"]

    if confidence >= 0.8 and priority == "High":
        return "create_task"
    
    if confidence >= 0.6:
        return "humain_review"
    
    return "ignore_or_review_later"



def main():
    lead_message="""
    Bonjour,
    Je dirige une petite agence et nous perdons beaucoup de temps
    à qualifier manuellement nos prospects.
    J'aimerais automatiser une partie du suivi commercial rapidement.
    Budget autour de 3000 euros.
    """

    print ("Analyse de lead en cours...")

    client = FakeLLMClient()
    result = client.analyze_lead(lead_message)

    validate_llm_result(result)

    print("\nRésultat structuré : ")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    action = decide_next_action(result)

    print("\nAction recommandée :")

    if action == "create_task":
        print("Créer automatiquement une tâche de suivi")
    elif action == "humain_review":
        print("Envoyer le lead en validation humaine")
    elif action == "ignore_or_review_later":
        print("Ne pas traiter automatiquement pour l'instant")


if __name__ == "__main__":
    main()
