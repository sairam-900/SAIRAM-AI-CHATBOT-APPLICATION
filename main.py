import os
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv

# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()

app = Flask(__name__)

# =========================
# GEMINI CLIENT
# =========================
def create_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

# =========================
# ROUTES
# =========================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    client = create_client()
    if not client:
        return jsonify({"reply": "API key missing"}), 500

    data = request.get_json()
    prompt = data.get("message")

    if not prompt:
        return jsonify({"reply": "Message required"}), 400

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

# =========================
# RENDER ENTRY POINT (VERY IMPORTANT)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
