# Use the official Debian 12 slim image as the base image
FROM debian:12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install any necessary dependencies
RUN apt-get update && apt-get install -y curl

# Download and install Ollama server
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set the command to run when the container starts
CMD ["ollama-server"]