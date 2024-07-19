
# Clandestine Platform

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-1.0.0-yellow)

## Table of Contents

- [Clandestine Platform](#clandestine-platform)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
    - [Backend](#backend)
    - [Dashboard / UI](#dashboard--ui)
    - [Storage](#storage)
    - [AI/ML](#aiml)
    - [Data Ingestion](#data-ingestion)
    - [Networking Software](#networking-software)
  - [Practices, Goals \& Considerations](#practices-goals--considerations)
    - [Goals](#goals)
    - [Privacy \& Security](#privacy--security)
      - [Networking Practices](#networking-practices)
      - [Secure Access / Ingress Points \& Egress Points](#secure-access--ingress-points--egress-points)
      - [Service Exposure](#service-exposure)
      - [Private/Anonymous Internet Browsing / Scanning](#privateanonymous-internet-browsing--scanning)
  - [Third-Party Services](#third-party-services)
    - [Cloud Providers](#cloud-providers)
    - [Crypto Swaps](#crypto-swaps)
  - [Dashboard / UI](#dashboard--ui-1)
    - [Tech Stack](#tech-stack-1)
    - [Requirements / Goals / Plans / Ideas](#requirements--goals--plans--ideas)
    - [Dashboard Design \& Development](#dashboard-design--development)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Contact](#contact)

## Introduction

The **Clandestine Platform** is a proof-of-concept framework designed for organizations to conduct offensive cybersecurity operations, focusing on attribution evasion and anonymity preservation. It aims to assist security researchers, penetration testers, and cybersecurity professionals in understanding and defending against threat actors by replicating their capabilities.

## Features

- **Centralized Intranet Platform**: Based on the [MITRE ATT&CK Framework](https://attack.mitre.com).
- **Privacy and Security**: Built for secure and discreet collaboration.
- **Advanced Analytics**: Integrates AI/ML for enhanced operational insights.
- **Mix Networks**: Uses Tor, I2P, and other networks to protect operators.
- **Lightweight UI**: Optimized for speed and performance using Pure CSS and HTMX.

## Tech Stack

### Backend

- [Litestar](https://litestar.dev)
- [DuckDB](https://duckdb.org/)
- [Docker](https://docker.com)

### Dashboard / UI

- [Litestar Vite Integration](https://github.com/cofin/litestar-vite)
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html)
- [Svelte](https://svelte.dev)
- [Shadcn UI Componenets Ported to Svelte](https://shadcn-svelte.com/)
- [Tailwind CSS](https://tailwindcss.com/)

### Storage

- [Document Storage](docs/storage/documents.md)
- [Database](docs/storage/database.md)
- [Go-Git](https://github.com/go-git/go-git)

### AI/ML

- [Fabric](https://github.com/danielmiessler/fabric)
- [Ollama](https://ollama.com)
- [HuggingFace](https://huggingface.co)

### Data Ingestion

- Docker-based scripts
- [Project Discovery](https://projectdiscovery.io) Tools
- [Network Scanning](docs/data_ingestion/network_scanning.md)

### Networking Software

- [OnionCat](https://github.com/rahra/onioncat)
- [CoreDNS](https://coredns.io/)

## Practices, Goals & Considerations

### Goals

- **Privacy & Security**: Ensure a secure platform for offensive operations and reconnaissance.
- **Ease of Use**: Simple and intuitive interface for ease of use.
- **Discreet Collaboration**: Secure and private collaboration features.

### Privacy & Security

#### Networking Practices

- Avoid exposing the dashboard UI to the public internet.
- Utilize mix networks and proxychains for secure access.
- Use Docker containers for isolation.

#### Secure Access / Ingress Points & Egress Points

- **OnionCat**: VPN over Tor and I2P.
- **HeadScale / Tailscale**: Easy-to-use VPN services.

#### Service Exposure

- **Tor Hidden Services**: Expose services without revealing IP addresses.
- **Yggdrasil Services**: Decentralized networking.

#### Private/Anonymous Internet Browsing / Scanning

- **Mix Networks**: Use as first hop in proxychains.
  - Torsocks
  - Nym Mixnet
  - Arti
  - Lokinet

- **Networking Tools**:
  - Proxychains
  - Wireguard
  - SSHuttle
  - Docker Containers (e.g., Tor-Privoxy)

## Third-Party Services

### Cloud Providers

- [Sporestack](docs/3rd_party_services/sporestack.md) for hosting

### Crypto Swaps

- [Wizard Swap](https://wizardswap.io) for crypto swaps

## Dashboard / UI

### Tech Stack

- [Vite](https://vitejs.dev/)
- [Litestar Vite Integration](https://github.com/cofin/litestar-vite)
- [Svelte](https://svelte.dev/)
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html)
- [Shadcn UI - Svelte Port](https://shadcn-svelte.com/)
- [Tor Hidden Services](https://tpo.pages.torproject.net/onion-services/portal/apps/web/)

### Requirements / Goals / Plans / Ideas

- Minimize HTML view sizes for efficient delivery over Tor.
- Focus on reactivity using Svelte components.
- Implement secure JavaScript practices.

### Dashboard Design & Development

- **Real-Time Data**: Use Litestar Websockets.
- **Component-Oriented**: Break views into Svelte components.
- **Optimized Performance**: Lightweight and efficient components.

## Setup and Installation

**To Do**

1. **Access the Application**:
    - The application should now be running and accessible through the specified network setup.

## Usage

- **Accessing the Dashboard**:
    - Authenticate at the root route.
    - Use the vertical navigation bar for application functionality.
    - Use the horizontal navigation bar for platform settings and management.

- **Data Ingestion and Analysis**:
    - Follow guidelines in the [documentation](docs/overview.md) for detailed usage instructions.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.


## Contact

For more information, issues, or feedback, please contact us at [cammclain@skiff.com](mailto:cammclain@skiff.com).

