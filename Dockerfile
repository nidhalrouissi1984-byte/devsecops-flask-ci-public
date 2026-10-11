# Image de base depuis ECR Public (evite les limites de telechargement Docker Hub)
FROM public.ecr.aws/docker/library/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependances d'abord (meilleur cache Docker)
# requirements.lock : versions figees + empreintes SHA-256 (genere avec pip-compile)
# --only-binary :all: : uniquement des wheels, aucun script setup.py execute
# --require-hashes    : pip refuse tout paquet dont l'empreinte ne correspond pas
COPY requirements.lock .
RUN pip install --no-cache-dir --only-binary :all: --require-hashes -r requirements.lock

# On copie uniquement le code utile, pas tout le depot
COPY app.py .

# Execution avec un utilisateur non-root
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 5000

# Serveur de production (le serveur Flask de dev n'est pas fait pour ECS)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
