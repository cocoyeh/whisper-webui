FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Gradio app file
COPY app.py .

EXPOSE 7860

# Set the command to run the app
CMD ["python", "app.py"]


