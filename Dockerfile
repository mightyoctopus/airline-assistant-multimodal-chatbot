# Use Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (including ffmpeg and any other useful tools)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gradio will use
EXPOSE 8080

# Run the Gradio app
CMD ["python", "main.py"]

