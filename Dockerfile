FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD sh -c "sleep 5  && uvicorn app.main:app  --host 0.0.0.0  --port 8000"
