FROM nixos/nix:latest

# Install necessary packages
RUN nix-env -iA nixpkgs.nixUnstable

# Copy NixOS configuration files
COPY configuration.nix /etc/nixos/configuration.nix
COPY hardware-configuration.nix /etc/nixos/hardware-configuration.nix

# Set up NixOS
RUN nixos-rebuild switch

# Expose only port 2222 for SSH
EXPOSE 2222

# Set the entry point
CMD ["/usr/bin/nixos-enter"]
