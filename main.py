import os
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv
from PIL import Image
import PyPDF2
from io import BytesIO

# =========================
# LOAD ENV
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
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# CHAT (TEXT / IMAGE / FILE)
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    client = create_client()
    if not client:
        return jsonify({"reply": "❌ API key missing"}), 500

    message = request.form.get("message")
    image_file = request.files.get("image")
    file = request.files.get("file")

    # ---------- IMAGE ----------
    if image_file:
        image = Image.open(image_file.stream)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[image, "Describe this image"]
        )
        return jsonify({"reply": response.text})

    # ---------- FILE (PDF / TXT) ----------
    if file:
        text = ""

        if file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(BytesIO(file.read()))
            for page in reader.pages:
                text += page.extract_text() or ""

        elif file.filename.endswith(".txt"):
            text = file.read().decode("utf-8")

        else:
            return jsonify({"reply": "❌ Unsupported file type"}), 400

        prompt = f"Analyze the following content:\n{text[:6000]}"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"reply": response.text})

    # ---------- TEXT ----------
    if message:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return jsonify({"reply": response.text})

    return jsonify({"reply": "❌ No input provided"}), 400

# =========================
# RENDER ENTRY POINT
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
