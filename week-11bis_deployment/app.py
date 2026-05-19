# --- ajout pour le deploiement ---
import os
from dotenv import load_dotenv
#----------------------------------

from flask import Flask, request, jsonify

# Lire le fichier .env -------------
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
# ------------------

app = Flask(__name__)

def is_professional_email(email: str) -> bool:
    free_domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    domain = email.lower().split("@")[-1] if "@" in email else ""
    return domain not in free_domains and domain != ""

# Nettoyage et normalisation des besoins multiples
def normalize_test(value) -> str:
    if value is None:
        return ""
    return str(value).strip()

# traitement des besoins multiples
def parse_need_types(value) -> list[str]:
    text = normalize_test(value)
    if not text:
        return []
    
    return [item.strip() for item in text.split(",") if item.strip()]


def score_lead(data: dict) -> dict:

    score = 0
    reasons = []

    budget = data.get("budget_range", "")
    urgency = data.get("urgency", "")
    need_type = parse_need_types(data.get("need_type", ""))
    email = data.get("email", "")
    message = data.get("message", "")

    budget_scores = {
        "< 500": 5,
        "500 - 1500": 15,
        "1500 - 3000": 25,
        "3000+": 35,
    }

    urgency_scores = {
        "Low": 5,
        "Medium": 15,
        "High": 25,
    }

    need_scores = {
        "Automation": 20,
        "Ops": 15,
        "Sales": 15,
        "Admin": 10,
        "Other": 5,
    }

    #label pour les besoins et les justifications.
    need_labels = {
        "Automation": "automatisation",
        "Ops": "opérations",
        "Sales": "acquisition / vente",
        "Admin": "administratif",
        "Other": "générique",
    }

    #Et l'agglomérateur de besoin
    matched_needs = []


    #-- Puis calcul des scores
    score += budget_scores.get(budget, 0)
    if budget_scores.get(budget, 0) >= 25:
        reasons.append("budget élevé")

    score += urgency_scores.get(urgency, 0)
    if urgency == "High":
        reasons.append("urgence forte")

    #Maj score des need_type car devenu liste
    for need in need_type:
        points = need_scores.get(need, 0)
        score += points

        label = need_labels.get(need)

        if label:
            matched_needs.append(label)

    #Ajout de la raison groupée
    if matched_needs:
        reasons.append(
            "besoin orienté " + ", ".join(matched_needs)
        )
    
    if is_professional_email(email):
        score += 10
        reasons.append("email pro")

    if len(message) >= 20 :
        score += 10
        reasons.append("besoin décrit")

    #Définition du score final
    if  score >= 70 :
        priority = "High"
        segment = "Qualified Lead"
    elif score >= 40:
        priority = "Medium"
        segment = "Potential"
    else: 
        priority = "Low"
        segment = "Unqualified"
    
    reason = ", ".join(reasons) if reasons else "signal faible"

    #Voir ce qui a été analysé
    print("\n=== Lead analysé ===")
    print(f"Email      : {email}")
    print(f"Need types : {need_type}")
    print(f"Score      : {score}")
    print(f"Priority   : {priority}")
    print(f"Segment    : {segment}")
    print(f"Reasons    : {reasons}")
    print("====================\n")

    return {
        "score": score,
        "priority": priority,
        "segment": segment,
        "reason": reason.capitalize() + "."
    }

#Changement du def score pour la gestion d'erreur et l'envoie d'un message propre et clair

@app.route("/score", methods=["POST"])
def score():
    try:
        #Ajout d'une vérification de header pour sécurité
        auth_header = request.headers.get("Authorization")
        expected_header = f"Bearer {API_TOKEN}"

        if auth_header != expected_header:
            print("Accès refusé : token invalide ou absent")

            return jsonify({
                "success": False,
                "error" : "Unauthorized"
            }), 401

        data = request.get_json() or {}

        print("\n=== Donnée reçues ===")
        print(data)

        result = score_lead(data)

        return jsonify({
            "success": True,
            **result
        }), 200
    
    except Exception as e:
        print("\n=== ERREUR API ===")
        print(str(e))
        print("==================\n")

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    # Adaptation de Flask au port Cloud pour utilisation de Render
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug = False)