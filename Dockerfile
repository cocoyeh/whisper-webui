FROM python:3.9-slim

RUN apt-get update -qq && apt-get install ffmpeg -y

# Create a working directory
WORKDIR /app
# Copy requirements file
COPY requirements.txt .
EXPOSE 7860

# Install dependencies
RUN pip install -r requirements.txt
# Gradio app file
COPY app.py .

# Environment variables
ENV GUNICORN_CMD_ARGS="--limit-request-line 0 --limit-request-field_size 0"

# Set the command to run the app
CMD ["python", "app.py"]

