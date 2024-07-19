FROM debian:12-slim

# Install Python and development tools
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip build-essential

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the entrypoint command
CMD [ "python3", "app.py" ]