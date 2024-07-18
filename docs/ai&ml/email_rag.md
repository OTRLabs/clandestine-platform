


In the field of AI/ML, we will leverage the high-quality prompts provided by Fabric to create Ollama Model Files. These files will be finely tuned for specific tasks, ensuring optimal performance and accuracy. By utilizing Fabric's prompts, we can train our models to excel in various domains and achieve the desired outcomes.



Email RAG | A non traditional approach to RAGS

Rather than the standard approach most RAG user interfaces follow, in that they mimic the look and feel of instant messaging applications, the email RAG is exactly what it sounds like. a RAG interface designed primarily to emulate the experience of sending a work email

The expectation is longer turnaround times but more detailed responses. This is because we are using offline AI, and must work with budget hardware. This way, it is less off-putting that the response is so slow. 

The goal is that the email agent would be able to assist you with research using LLM agents, similar to that of langchain. 

It will break the process down into 

data sources used for context include: 

- attached documents
- search engines
- Internal knowledge, documents, etc

Ideally, you would be able to send emails to this system which would reply with high quality results. I want to cite my sources, provide additional reading and more. 

## design:

- postfix docker container, exposed via Tor
- Salmon to SMTP interactions
- Ollama for data analysis and summarization
- Outlines
- Access via:
    - Whonix / Tails / Torsocks + Thunderbird
    - Official web UI (comes later)