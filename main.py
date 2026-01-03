import os
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv

load_dotenv()   # 👈 THIS IS THE MISSING LINK

app = Flask(__name__)

def create_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    client = create_client()
    if not client:
        return jsonify({"reply": "API key missing"}), 500

    prompt = request.json.get("message")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(port=8080, debug=True)
