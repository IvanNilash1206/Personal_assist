# backend/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY backend/ /app
RUN pip install --upgrade pip
# we'll add requirements.txt and other steps later
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
