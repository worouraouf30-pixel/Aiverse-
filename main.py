from flask import Flask, request, jsonify
import openai, os
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BACKEND_SECRET = os.getenv("BACKEND_SECRET")

openai.api_key = OPENAI_API_KEY

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('X-API-KEY') or (request.json or {}).get('api_key')
        if not BACKEND_SECRET:
            return jsonify({"erreur": "BACKEND_SECRET non configurée sur le serveur"}), 500
        if not key or key != BACKEND_SECRET:
            return jsonify({"erreur": "Clé API invalide ou manquante"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/", methods=["GET"])
def home():
    return "🚀 AIVERSE Backend sécurisé fonctionne !"

@app.route("/generer", methods=["POST"])
@require_api_key
def generer():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"erreur": "Le champ 'prompt' est requis."}), 400
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": prompt}],
            max_tokens=500
        )
        text = completion["choices"][0]["message"]["content"]
        return jsonify({"reponse": text})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
