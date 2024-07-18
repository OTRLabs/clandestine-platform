# Conti Platform: A Platform for Organizations Hacking the Planet
---

The goal of the conti platform is to focus on providing a centralized “intranet” like platform based around the mitre Att&ck framework

It’s primary purpose is to provide an “off the record” location for collaboration & development of an offensive organization’s capabilities.

The main goal is to be a hub of intelligence for an organizations operations. Ideally you would be able to pour data into this platform and it would be able to provide advanced insights & analysis of your situation(s)

The application will work primarily as a monolith Litestar application with additional containers for external services such as:

It is built to be accessed via Tor & other “dark net”/mix networks to protect operators, and minimize likelihood of detection. The goal is to have conti system exist as a hub, outside of the Standard internet. I anm hesitant to use the word intranet, but in a sense, it is an internal network of tools and generally make efforts to obfuscate activities & collaboration, only exposing yourself on your terms and never directly. 

In addition to these “mix networks”, we also intend to use:

- proxychains
- OpenVPN configurations
- Docker containers to isolate the environment
- And much more.

Generally speaking the application has sacrificed speed for anonymity, however this does not mean we do not make efforts to follow best practices and implement our systems in a way that acknowledges our limitations and seeks to work around them. 

- One minor example is that we are choosing to use Pure-CSS for our UI styling, as this is extremely lightweight and can reduce page refresh times especially when accessing the UI over Tor
- we use HTMX
- We will use the email based RAG system that, while responses take longer, the replies are much more refined and informative. This is to account for the long wait times of using local AI on budget hardware

# 1. Introduction
---
This project is an attempt at building what could be looked at as `Google Workspace`, but the assumes the following:
- your workflow is, in some way related to `offensive security`
- evading `attribution` is a **priority** for your `operation(s)`.
- secure & discreet collaboration is a **priority** for your `operation(s)`.
- you want to use `AI/ML` to make your `operation(s)` more effective.
### what are the considerations you have to make when creating applications for this field

On one hand, I want to say “chill I am a one man show, do not expect this application to be Fort Knox.”. And on some level that is true, please assume that this application, like any other has vulnerabilities. But I do want to make this application as secure as possible, and I do want to make it so that it is not a liability to use.



# 2. Tech Stack & Features:
---
## 2.1 Backend:
### Backend Tech Stack
- [Litestar](https://litestar.dev) 
- [DuckDB](https://duckdb.org/) (For user storage)
- [Docker](https://docker.com)

## 2.2 Dashboard / UI:
### UI Tech Stack
- [Litestar HTMX Integration](https://docs.litestar.dev/2/usage/htmx.html) 
- [HTMX](https://htmx.org/) 
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html) 
- [Pure CSS](https://purecss.io/)


## 2.3 Storage:
- [**Document Storage**](docs/storage/documents.md)
- [**Database**](docs/storage/database.md)
- [**Go-Git**]([https://](https://github.com/go-git/go-git))
## 2.4 AI/ML
### AI/ML Tech Stack
- [Fabric](https://github.com/danielmiessler/fabric)
- [Ollama](https://ollama.com)
- [HuggingFace](https://huggingface.co)
  
## 2.5 Data Ingestion
### Data Ingestion Tech Stack
- Docker based scripts
- [Project Discovery](https://projectdiscovery.io) Tools
- [Network Scanning](docs/data_ingestion/network_scanning.md)

## 2.6 Networking Software
- [OnionCat](https://github.com/rahra/onioncat)
- [CoreDNS](https://coredns.io/)


# 3. Practices, Goals & Considerations:
---

## 3.1 Goals:
- **Privacy & Security**: The main goal of this platform is to provide a secure platform for organizations to conduct offensive operations, preform recon & develop their capabilities.. This means that the platform should be secure, and should not leak information about the organization using it.
- **Ease of Use**: The platform should be easy to use, and should not require a lot of technical knowledge to use. This means that the platform should be user friendly, and should have a simple and intuitive interface. 


## 3.2 Privacy & Security:

### Networking Practices

Generally speaking, we do not want to expose our operations to the internet at large.
That is why it is heavily advised that you do not expose your dashboard UI to the internet, whether it be with a tunnel like Cloudflared, or port forwarding or something. Generally speaking the assumption is that you want to obfuscate the fact that you are using this offensive Huly platform, on top of the fact that it’s just best practices not to expose services unnecessarily 

That being said:
- we still have to access the UI somehow
- Our network scanning systems still have to be able to reach said network to scan
- Our AI/ML systems still have to be able to reach the internet to download models, and preform searches.
- Basically, we need to be exposed sometimes, but we want to do it "right"

#### Secure Access / Ingress Points & Eggress Points
I have a few ideas on how to access the UI:

- [**OnionCat**](https://www.onioncat.org/): This is a VPN service that is designed to be easy to use and set up. It is designed to be self hosted & operate over `Tor` & `I2P`
- [**HeadScale**](https://headscale.net/) / [Tailscale](https://tailscale.com): This is a VPN service that is designed to be easy to use and set up. It is designed to be self hosted

#### Service Exposure
Hidden Services:
-  [**Tor Hidden Services**](https://www.torproject.org/docs/tor-onion-service.html.en) are a great way to expose services to the internet without exposing your IP address. This is a great way to expose the UI to the internet without exposing your IP address. 
- [**Yggdrasil Services**](https://yggdrasil-network.github.io/services.html)
- [**I2P**](https://geti2p.net/en/)


#### Private/Anonymous Internet Browsing / Scanning
##### Mix Networks
All [Mix-Nets](https://en.wikipedia.org/wiki/Mix_network) are accessible as `SOCKS proxies` & are intended to be used as the **first hop** in [proxychains](https://github.com/rofl0r/proxychains-ng)
- [**Torsocks**](https://gitlab.torproject.org/tpo/core/torsocks)
- [**Nym Mixnet**](https://nymtech.net/)
- [**Arti**](https://arti.torproject.org/)
- [**Lokinet**](https://lokinet.org/)

##### Networking Tools
- [**Proxychains**](https://github.com/rofl0r/proxychains-ng)
- [**Wireguard**](https://www.wireguard.com/)
- [**SSHuttle**](https://github.com/sshuttle/sshuttle)
- [**Docker Containers**](https://hub.docker.com) for isolation
  -  [dockage/Tor-Privoxy](https://github.com/dockage/tor-privoxy)
- [**Honeyd**](https://honeyd.org)

# 3rd party services

It is basically a standard for most productivity tools to integrate with your other productivity tools. Our tech ecosystem is built on 3rd party dependencies. 
With this reality it was inevitable that we would either need or want to integrate with some sort of 3rd party service or API.
Rather than being excessively limited, and not including anything, or choosing random services for seemingly arbitrary reasons, we will attempt to include any service which offers:
- a `Tor Hidden Service` `HTTP API`
- Accepts `XMR` (may settle for `BTC` sometimes)

generally speaking, if both of these statements are true about the service, we are happy to integrate it with conti platform.

These services will be optional, and the platform will be useful even without paying

we will have a wallet management system within the app but users maintain full control over their wallet. 

Rather than risk users violating services acceptable use policy, the wallets are used to execute functions within the automations preformed by the application 

## Services:
### Cloud providers 

- [**sporestack**](docs/3rd_party_services/sporestack.md) for hosting

### Crypto Swaps
- [**Wizard Swap**](https://wizardswap.io) for crypto swaps

**Need to find proxy provider with `API`**