FROM python:3.11-slim
WORKDIR /app
COPY . /app/ 

RUN pip install --default-timeout=100 --no-cache-dir -r ./requirements.txt
# CMD source .venv/bin/activate
CMD ["adk", "api_server", "--host=0.0.0.0", "--port=8000", "/app/agents"]

EXPOSE 8000