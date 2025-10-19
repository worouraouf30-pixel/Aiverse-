import requests, os

BASE_URL = os.getenv("AIVERSE_URL", "https://aiverse-backend.onrender.com")
BACKEND_SECRET = os.getenv("BACKEND_SECRET", "PASTE_A_STRONG_RANDOM_SECRET_HERE")

url = f"{BASE_URL}/generer"
payload = {"prompt": "Écris un message court d'encouragement pour Création.", "api_key": BACKEND_SECRET}
resp = requests.post(url, json=payload, timeout=20)
print("Status:", resp.status_code)
print("Réponse:", resp.text)
