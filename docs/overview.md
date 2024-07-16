# Conti Platform: A Platform for Organizations Hacking the Planet
---

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
- 
## 2.2 Dashboard / UI:
### UI Tech Stack
- [Litestar HTMX Integration](https://docs.litestar.dev/2/usage/htmx.html) 
- [HTMX](https://htmx.org/) 
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html) 
- [Pure CSS](https://purecss.io/)


## 2.3 Storage:
- [Document Storage](docs/storage/documents.md)
- [Database](docs/storage/database.md)

## 2.4 AI/ML
### AI/ML Tech Stack
- [Fabric](https://github.com/danielmiessler/fabric)

## 2.5 Data Ingestion
### Data Ingestion Tech Stack
- Docker based scripts
- Project Discovery Tools
- [Network Scanning](docs/data_ingestion/network_scanning.md)



# 3. Practices, Goals & Considerations:
---

## 3.1 Goals:
- **Privacy & Security**: The main goal of this platform is to provide a secure platform for organizations to conduct offensive operations. This means that the platform should be secure, and should not leak information about the organization using it.
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

- [OnionCat](https://www.onioncat.org/): This is a VPN service that is designed to be easy to use and set up. It is designed to be self hosted & operate over `Tor` & `I2P`
- [HeadScale](https://headscale.net/) / [Tailscale](https://tailscale.com): This is a VPN service that is designed to be easy to use and set up. It is designed to be self hosted

#### Service Exposure
Hidden Services:
-  [Tor Hidden Services](https://www.torproject.org/docs/tor-onion-service.html.en) are a great way to expose services to the internet without exposing your IP address. This is a great way to expose the UI to the internet without exposing your IP address. 
