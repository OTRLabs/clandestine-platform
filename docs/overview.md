# Conti Platform: A Platform for Organizations Hacking the Planet
---

## Introduction

This project is an attempt at building what could be looked at as Google Workspace, but the assumes the following:
- your workflow is, in some way related to `offensive security`
- evading `attribution` is a **priority** for your `operation(s)`.

### what are the considerations you have to make when creating applications for this field

On one hand, I want to say “chill I am a one man show, do not expect this application to be Fort Knox.”. And on some level that is true, please assume that this application, like any other has vulnerabilities. But I do want to make this application as secure as possible, and I do want to make it so that it is not a liability to use.



# 2. Tech Stack:

The app is built around [Litestar](https://litestar.dev) as the backend & main "logic handler", which functions as the “glue” of the application. It allows the database to talk to the UI & the UI to deploy containerized scripts & applications 

---

## Backend:

### Backend Tech Stack
- [Litestar](https://litestar.dev) 
- [DuckDB](https://duckdb.org/) (For user storage)


## Dashboard / UI:

### UI Tech Stack

- [Litestar HTMX Integration](https://docs.litestar.dev/2/usage/htmx.html) 
- [HTMX](https://htmx.org/) 
- [Jinja2 Templates](https://docs.litestar.dev/2/reference/contrib/jinja.html) 
- [Pure CSS](https://purecss.io/)

### Dashboard Description:

The `UI` is designed to be lightweight in terms of size. The goal is to make the delivery of the `UI` when fetching `HTML`/`HTMX` from the server a *fast* and *efficient* process.

#### Dashboard Components:

We are going to focus on making our HTMX based UI very “component oriented” similar to React. This is because we want to give each element of the application the attention to detail it needs to make the application feel like a “modern application”.

I did not know this until recently but these components have a sort of set of “standards”. Like how you expect a context menu to pop up when you right click. There are just behaviors that are considered “best practices” to implement. 

Dividing the application into HTMX/Jinja template based components, where each component of the UI is a .html.j2 file that contains a specific element or specific set of elements in a set state that can be called to render that state on the users browser, as this allows us to pay much more attention to each section of the UI and implement proper functionality to make for the best user experience. The end goal is to reduce the amount of “janky” experiences in the client side, where things behave in unexpected and unsettling ways on the client side.

It can be expected that this application will be compatible with the Tor browser though there are some caveats. The main issue is that to use the UI, your Tor browser must have client side scripting enabled. This means that it is incompatible with the “safest settings” on Tor Browser. This means that you may risk deanon if someone runs JS on your browser, so if you want to use Tor it is best to use a host that routes all traffic through Tor like whonix / tails / qubes.




## Storage:

- [Document Storage](docs/storage/documents.md)
- [Database](docs/storage/database.md)

## AI/ML

In the field of AI/ML, we will leverage the high-quality prompts provided by Fabric to create Ollama Model Files. These files will be finely tuned for specific tasks, ensuring optimal performance and accuracy. By utilizing Fabric's prompts, we can train our models to excel in various domains and achieve the desired outcomes.
### AI/ML Tech Stack
- [Fabric](https://github.com/danielmiessler/fabric): A 
# Privacy & Security:

## AI Privacy

TL;DR: we will self host open source models. There is just no reason to use 3rd party APIs, where these tokens add up. If you want to use faster LLMs maybe we will offer a cloud platform 

I am going to have Ollama be the standard choice. The open source nature + model files for building highly optimized models is great! This combined with fabric will make for effective chat, analysis and summarization 

We will use hugging face for decision making if it comes to that
### Networking Practices

Generally speaking, we do not want to expose our operations to the internet at large.
That is why it is heavily advised that you do not expose your dashboard UI to the internet, whether it be with a tunnel like Cloudflared, or port forwarding or something. Generally speaking the assumption is that you want to obfuscate the fact that you are using this offensive Huly platform, on top of the fact that it’s just best practices not to expose services unnecessarily 

That being said:
- we still have to access the UI somehow
- Our network scanning systems still have to be able to reach said network to scan
- Our AI/ML systems still have to be able to reach the internet to download models, and preform searches.
- Basically, we need to be exposed sometimes, but we want to do it "right"

#### UI Access
I have a few ideas on how to access the UI:
- HeadScale / Tailscale: This is a VPN service that is designed to be easy to use and set up. It is designed to be self hosted
- Tor Hidden Service: Need to do more research, and testing to see how well this works. This is less than ideal, so will be optional at most

#### Network Scanning
- OpenVPN Profiles + Chained Connections: This is a method of chaining VPN connections together to make it harder to trace back to the source. This is a bit more advanced, and will require some testing to see how well it works
- Torsocks + Proxychains: This is a method of chaining connections together using the Tor network. This would work by passing proxychains configs to the network scanning container, and then using torsocks to route the traffic through the tor network, then out of an "exit proxy" so that you do not have a low rating.
- Rotating API Keys: This is a method of rotating API keys to avoid rate limiting. This is done by providing multiple of the same type of credential to the network scanning container, and then rotating through them as needed.