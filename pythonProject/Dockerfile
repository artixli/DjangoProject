# Utiliser une image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port que Django utilise (par défaut 8000)
EXPOSE 8000

RUN pip install --upgrade pip

# Définir la commande de démarrage de l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
