from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"

@app.route("/")
def home():
    return render_template("index.html")   # ✅ Show webpage

@app.route("/translate", methods=["POST"])
def translate_text():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
        Translate the following text into English.
        Output ONLY one professional sentence.
        Do NOT explain.
        Do NOT show multiple options.

        Text: "{text}"
        """

        response = model.generate_content(prompt)
        translated_text = response.text.strip()

        # Ensure only one clean line
        translated_text = translated_text.split("\n")[0]

        return jsonify({"translated_text": translated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run server properly
if __name__ == "__main__":
    app.run(debug=True)