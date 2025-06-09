from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

CALENDLY_TOKEN = "Bearer eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzQ5NDY3NzExLCJqdGkiOiJmOGZiMDg1OS1jMTljLTRkYmItYmU5Ny0yNTA1NjQ5YjM1YmMiLCJ1c2VyX3V1aWQiOiJlMDg5ZmEzZC1lZTNiLTQ3NjItODU2OC1mYzhhNDk0MjdmZTgifQ.DAd_7_DcwPrReBDcJSh7eqgH-Is5174Be4QLd7UwwsI6RfPFsYsknpjOqFJCVVs1ybHmHculj8phCP0FhITvbQ"

headers = {
    "Authorization": CALENDLY_TOKEN,
    "Content-Type": "application/json"
}

@app.route("/api/event-types", methods=["GET"])
def get_event_types():
    # 1. Aflăm user-ul curent
    user_resp = requests.get("https://api.calendly.com/users/me", headers=headers)
    if user_resp.status_code != 200:
        return jsonify({"error": "Nu s-a putut obține user-ul"}), 400

    user_uri = user_resp.json()["resource"]["uri"]

    # 2. Luăm lista event types
    events_resp = requests.get(f"https://api.calendly.com/event_types?user={user_uri}", headers=headers)
    if events_resp.status_code != 200:
        return jsonify({"error": "Nu s-au putut obține tipurile de întâlniri"}), 400

    event_types = events_resp.json()["collection"]
    simplified = [
        {"name": e["name"], "uri": e["uri"], "duration": e.get("duration", "N/A")}
        for e in event_types
    ]

    return jsonify(simplified)
