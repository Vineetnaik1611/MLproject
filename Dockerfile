# Use a lightweight Python image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements
COPY . /app

# Install dependencies
RUN apt update -y && apt install awscli -y

RUN pip install-r requirements.txt
# Command to run the Flask app
CMD ["python3", "app.py"]
