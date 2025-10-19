# 🚀 AIVERSE Backend - Version Française

## Étapes pour déployer sur Render

1. Crée un compte sur [Render.com](https://render.com)
2. Clique sur **New > Web Service**
3. Connecte ton GitHub ou importe le fichier ZIP.
4. Configure les variables d'environnement :
   - `OPENAI_API_KEY` = ta clé OpenAI
   - `BACKEND_SECRET` = une clé secrète forte
5. Render installera automatiquement les dépendances (`pip install -r requirements.txt`)
6. Démarre automatiquement via `gunicorn main:app` (défini dans Procfile)

## Test local
```bash
pip install -r requirements.txt
python main.py
```
Puis visite http://localhost:8080/

## Test distant
```bash
python test_request.py
```

AIVERSE est maintenant en ligne ! 🔵
