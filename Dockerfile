FROM python:3.10-slim
WORKDIR /app
COPY analizador.py /app/analizador.py
CMD ["python", "analizador.py"]