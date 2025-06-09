from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Tokenul și URI-ul evenimentului pot fi puse mai târziu în variabile de mediu pentru securitate
CALENDLY_TOKEN = "Bearer INSERT_TOKEN_AICI"
EVENT_TYPE = "https://api.calendly.com/event_types/INSERT_EVENT_URI"

@app.route("/api/create-booking", methods=["POST"])
def create_booking():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    datetime = data.get("datetime")

    # Pentru început, doar returnăm un răspuns de test
    return jsonify({
        "status": "success",
        "confirmation_url": "https://calendly.com/nume-utilizator",
        "message": f"Am primit cererea pentru {name} la {datetime} cu emailul {email}"
    })

# Configurare corectă pentru Render (folosește portul din variabilele de mediu)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
