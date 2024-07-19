# Use the official Redis image as the base image
FROM redis:latest

# Set a non-root user for better security
RUN groupadd -r redis && useradd -r -g redis redis
USER redis

# Add any additional configuration or setup commands here

# Set the entrypoint to run Redis server
ENTRYPOINT ["redis-server"]