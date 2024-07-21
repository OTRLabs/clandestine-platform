# /home/user/platform/clandestine-platform/src/app/services/agentic-network-scanner/environment_configs/nix/port_scanners/rustscan_env.nix

## This environment is designed to deploy a Podman container that performs Rustscan scans on a target network(s).
{ pkgs, ... }:

let
  # Install Proxychains4
  proxychains = pkgs.proxychains-ng;

  # Install Podman and its dependencies
  podman = pkgs.podman;
  podmanDeps = with pkgs; [
    btrfs-progs
    container-selinux
    conmon
    fuse-overlayfs
    libseccomp
    ostree
    runc
    slirp4netns
    uidmap
  ];

  # Install Rustscan
  rustscan = pkgs.rustscan;

  # Install Tor and Torsocks
  tor = pkgs.tor;
  torsocks = pkgs.torsocks;
in
{
  environment.systemPackages = [
    proxychains
    podman
    rustscan
    tor
    torsocks
  ] ++ podmanDeps;
}