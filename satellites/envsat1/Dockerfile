FROM python:3.10-slim

WORKDIR /app/satellites/envsat1

COPY ././requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY telemetry.py .

CMD ["python", "telemetry.py"]
