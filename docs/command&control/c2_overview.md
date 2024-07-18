# Command & Control Systems

So, this aspect of the conti platform is what I am most interested in, as I believe that if I implement this properly, developing implants for specific purposes (I am thinking in Zig?), will be fun and more achievable 

In terms of inspiration, there are many open source C2 platforms I have played around with, and though I don’t think our codebases will be remotely comparable, I am taking HEAVY inspiration.

I think analyzing my thoughts on existing C2 systems is not only important for credit & attribution, but I think it gives my project some additional depth, and kinda allows you to see where my head is at when designing the conti platforms C2 systems

Also, I list pro’s and con’s for the project. These are subjective, in relation to how well something meshes with our project goals

For example, I say “React” is a Con for Mythic. That is obviously not a critique of the developer or the project. It is just an acknowledgment of what I seek to do differently 

All of these projects are extremely impressive 

## Inspirational Projects & Research

### Starkiller / Empire

Honestly an awesome project. 

- I like the graph based GUI that is paywalled. I love canvas + node based visualization for operations. Like Maltego or open BAS
- Excellent controls over the listeners from the web UI via a form. Being able to just open up a new port is awesome
- Wide variety of stagers and another great menu

### Mythic

My biggest praise of Mythic and something I seek to replicate in conti platform is its effort to serve as a base framework for implant development 

With some frameworks, you are seemingly expected to use the built in open source implants, or work within the predetermined parameters of how the implants work a framework

For example, if I wanted to develop an implant for starkiller / empire which is written in Rust, my options compared to the C#, Iron python, etc documentation BC Security has makes developing somewhat opinionated. 

I see the value in starkiller’s abilities within its realm, but I would rather focus on providing a wide array of supported protocols for implant C2 listeners & communication methods allowing for developers to create highly specialized and specific implants for tailed access operations

I think the fact that mythic has such a wide variety of agents, and really a large ecosystem with a surprisingly wide and continuously growing list of **community driven integrations** 

I would like to further analyze what they did that made so many devs want to use them as their platform. I do not think my conti platform will be as widely appealing to general pen testers, as I think the Tor dashboard is a serious downside for many but I want to make a point to foster community when I can 

- documentation was on point
- Effective use of JSON configs to specify implant information to ensure proper compatibility and representation in the UI
- Uses docker-compose for deployment. Hypothetically can be used across multiple hosts but I have not tried yet.
- Use of git to install modules
- Cool micro service architecture communication via MQTT
- Cool cli tool

**Mythic downsides**

- I could just be dumb but why does it launch every time I boot my laptop lol
- react for UI. Too heavy for our use case.

### Caldera

URL: [https://caldera.mitre.org](https://caldera.mitre.org/)

Caldera is a piece of art from The MITRE Corporation. 

**pros**:

- heavy focus on automation
- Integrations with external services (Open BAS is the big one that comes to mind)
- Generally, I assume a large amount of high quality research went into developing this platform.
- Plugin system

### SILENTTRINITY

So, confession: 

I never really used this project. 

However I did read a LOT about it

Some things I like:

- ability to connect multiple servers
- bring your own interpreter model for implants
- The use of DSL for implants for a variety of benefits

### Havoc

similar to starkiller, I am a huge fan of the node graph / canvas to visualize operations, infected hosts, etc

## Takeaways:

One of the biggest things we want to improve on is isolation & distancing operators from directly interacting with the target 

### Listeners:

We really want to make sure we support a very wide range of protocols for communications between the implants running on infected hosts, and the actual container running the listener

one thing that is incredibly important is that we are not running the listener service container in a way that can potentially expose the rest of our operations. 

generally speaking they should be acting as a super stealthy reverse proxy, which just routes traffic back to the database in the most secure, anonymous & sanitized way possible.

Protocols we intend to support:

- HTTP(s)
- HTTP over tor
- web socket
- DNS
- Noise
- SSH

Potential protocols:

- XMPP
- Telegram bot (HTTPS)
- Telemetry
- MQTT
- NATS
- Tox

We want to enforce strict authentication using litestar guards & maybe JWTs

We do not want a situation where blue team is able to send malicious requests that go directly into the database. 

If we want to add any listener functionality we will need to make sure the agent communications are somewhat standardized 

### Database & Data Storage