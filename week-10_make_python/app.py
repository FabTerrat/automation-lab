from flask import Flask, request, jsonify

app = Flask(__name__)

def is_professional_email(email: str) -> bool:
    free_domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    domain = email.lower().split("@")[-1] if "@" in email else ""
    return domain not in free_domains and domain != ""

def score_lead(data: dict) -> dict:
    score = 0
    reasons = []

    budget = data.get("budget_range", "")
    urgency = data.get("urgency", "")
    need_type = data.get("need_type", "")
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

    score += budget_scores.get(budget, 0)
    if budget_scores.get(budget, 0) >= 25:
        reasons.append("budget élevé")

    score += urgency_scores.get(urgency, 0)
    if urgency == "High":
        reasons.append("urgence forte")

    score += need_scores.get(need_type, 0)
    if need_type == "Automation":
        reasons.append("besoin orienté automatisation")
    
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

    return {
        "score": score,
        "priority": priority,
        "segment": segment,
        "reason": reason.capitalize() + "."
    }

@app.route("/score", methods=["POST"])
def score():
    data = request.get_json() or {}
    result = score_lead(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)