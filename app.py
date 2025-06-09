from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Tokenul tău de autentificare de la Calendly
CALENDLY_TOKEN = os.getenv("CALENDLY_TOKEN") or "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzQ5NDY3NzExLCJqdGkiOiJmOGZiMDg1OS1jMTljLTRkYmItYmU5Ny0yNTA1NjQ5YjM1YmMiLCJ1c2VyX3V1aWQiOiJlMDg5ZmEzZC1lZTNiLTQ3NjItODU2OC1mYzhhNDk0MjdmZTgifQ.DAd_7_DcwPrReBDcJSh7eqgH-Is5174Be4QLd7UwwsI6RfPFsYsknpjOqFJCVVs1ybHmHculj8phCP0FhITvbQ" 
EVENT_TYPE_URI = "https://api.calendly.com/event_types/fb6f416b-ea8a-4049-80d8-d924fd0d57e1"

@app.route("/api/create-booking", methods=["POST"])
def create_booking():
    try:
        data = request.json

        name = data.get("name")
        email = data.get("email")
        datetime = data.get("datetime")

        if not all([name, email, datetime]):
            return jsonify({"error": "Missing required fields"}), 400

        payload = {
            "invitee": {
                "email": email,
                "name": name
            },
            "event_type": EVENT_TYPE_URI,
            "start_time": datetime
        }

        headers = {
            "Authorization": CALENDLY_TOKEN,
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.calendly.com/scheduled_events", json=payload, headers=headers)

        if response.status_code in [200, 201]:
            booking_data = response.json()
            return jsonify({
                "status": "success",
                "confirmation_url": booking_data.get("resource", {}).get("uri"),
                "message": "Întâlnirea a fost programată cu succes!"
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Calendly API error: {response.text}"
            }), response.status_code

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render setează portul în variabila de mediu PORT
    app.run(host="0.0.0.0", port=port)

