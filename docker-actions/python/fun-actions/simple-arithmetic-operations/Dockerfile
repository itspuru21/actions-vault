FROM python:3.11-slim

WORKDIR /app

# Copy the python script into the container
COPY main.py /app/main.py

# Execute the script when the container starts
ENTRYPOINT ["python", "/app/main.py"]