from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CALENDLY_TOKEN = eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzQ5NDY3NzExLCJqdGkiOiJmOGZiMDg1OS1jMTljLTRkYmItYmU5Ny0yNTA1NjQ5YjM1YmMiLCJ1c2VyX3V1aWQiOiJlMDg5ZmEzZC1lZTNiLTQ3NjItODU2OC1mYzhhNDk0MjdmZTgifQ.DAd_7_DcwPrReBDcJSh7eqgH-Is5174Be4QLd7UwwsI6RfPFsYsknpjOqFJCVVs1ybHmHculj8phCP0FhITvbQ
EVENT_TYPE = "https://calendly.com/emanuel-istrate-kw/30min"

@app.route("/api/create-booking", methods=["POST"])
def create_booking():
    data = request.json
    name = data["name"]
    email = data["email"]
    datetime = data["datetime"]

    # Aici ar trebui să folosești scheduling link sau verifici sloturi
    # Exemplu de răspuns generic (de test)
    return jsonify({
        "status": "success",
        "confirmation_url": "https://calendly.com/YOUR_USERNAME"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
