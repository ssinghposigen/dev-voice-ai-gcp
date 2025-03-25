# Use a base image with Python >= 3.12 if available
FROM python:3.12-slim
# # Start with PyTorch base image which already includes CUDA support
# FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the model download script
COPY download_models.py .

# Run the model download script to cache models in the container
RUN python download_models.py

# Set the entrypoint
ENTRYPOINT [ "python3", "-m" ]
