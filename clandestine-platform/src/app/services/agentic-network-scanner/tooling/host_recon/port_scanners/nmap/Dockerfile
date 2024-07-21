FROM nixos/nix:21.05

# Install required packages
RUN nix-channel --add https://nixos.org/channels/nixos-21.05 nixos \
    && nix-channel --update \
    && nix-env -iA nixos.git nixos.curl nixos.gnupg nixos.gnutar nixos.gzip nixos.openssl nixos.sudo nixos.wget

# Copy NixOS configuration files
COPY configuration.nix /etc/nixos/configuration.nix
COPY hardware-configuration.nix /etc/nixos/hardware-configuration.nix

# Generate NixOS system configuration
RUN nixos-generate-config --root /mnt

# Create a non-root user
RUN useradd -m -s /bin/bash myuser

# Set the root password (optional)
RUN echo "root:your_password" | chpasswd

# Build and install NixOS
RUN nixos-install --no-root-passwd

# Set the entrypoint to boot into NixOS
ENTRYPOINT ["/nix/var/nix/profiles/system/bin/switch-to-configuration", "boot"]

# Expose any required ports
EXPOSE 22

# Switch to the non-root user
USER myuser

# Set the default command
CMD ["/usr/sbin/sshd", "-D"]