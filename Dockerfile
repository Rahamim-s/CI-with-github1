# Utiliser une image de base avec Python
FROM python:3.8

# Copier les fichiers de votre application dans l'image Docker
COPY . /app

# Définir le répertoire de travail dans l'image
WORKDIR /app

# Installer les dépendances nécessaires
RUN pip install -r requirements.txt

# Exposer le port sur lequel votre application Flask fonctionne (par défaut 5000)
EXPOSE 5000

# Commande pour démarrer votre application Flask
CMD ["python", "app.py"]
