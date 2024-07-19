FROM rustscan/rustscan:2.1.1

# Set a non-root user for running the container
RUN adduser --disabled-password --gecos '' rustscan_user
USER rustscan_user

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    iptables \
    && rm -rf /var/lib/apt/lists/*

# Configure iptables to restrict network access
RUN iptables -P INPUT DROP && iptables -P FORWARD DROP && iptables -P OUTPUT DROP

# Set the entrypoint command
ENTRYPOINT ["rustscan"]

# documenation: https://github.com/RustScan/RustScan/wiki/Installation-Guide

# need to load proxies from the database