from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Înlocuiește cu tokenul tău real (păstrează Bearer!)
CALENDLY_TOKEN = "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzQ5NDY3NzExLCJqdGkiOiJmOGZiMDg1OS1jMTljLTRkYmItYmU5Ny0yNTA1NjQ5YjM1YmMiLCJ1c2VyX3V1aWQiOiJlMDg5ZmEzZC1lZTNiLTQ3NjItODU2OC1mYzhhNDk0MjdmZTgifQ.DAd_7_DcwPrReBDcJSh7eqgH-Is5174Be4QLd7UwwsI6RfPFsYsknpjOqFJCVVs1ybHmHculj8phCP0FhITvbQ"
EVENT_TYPE_URI = "https://api.calendly.com/event_types/fb6f416b-ea8a-4049-80d8-d924fd0d57e1"

headers = {
    "Authorization": CALENDLY_TOKEN,
    "Content-Type": "application/json"
}

@app.route("/")
def index():
    return "✅ Serverul este activ!"

@app.route("/api/create-booking", methods=["POST"])
def create_booking():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    datetime = data.get("datetime")  # format ISO 8601 ex: 2025-06-11T14:00:00Z

    if not all([name, email, datetime]):
        return jsonify({"status": "error", "message": "Lipsesc datele necesare (name/email/datetime)"}), 400

    payload = {
        "event_type": EVENT_TYPE_URI,
        "invitee": {
            "email": email,
            "name": name
        },
        "start_time": datetime
    }

    response = requests.post("https://api.calendly.com/scheduled_events", headers=headers, json=payload)

    if response.status_code == 201:
        result = response.json()["resource"]
        return jsonify({
            "status": "success",
            "confirmation_url": result.get("uri"),
            "message": "✅ Programarea a fost creată cu succes!"
        })

    return jsonify({"status": "error", "details": response.text}), 400

# ✅ Config pentru Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

