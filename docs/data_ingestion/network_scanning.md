

# Network Scanning
- OpenVPN Profiles + Chained Connections: This is a method of chaining VPN connections together to make it harder to trace back to the source. This is a bit more advanced, and will require some testing to see how well it works
- Torsocks + Proxychains: This is a method of chaining connections together using the Tor network. This would work by passing proxychains configs to the network scanning container, and then using torsocks to route the traffic through the tor network, then out of an "exit proxy" so that you do not have a low rating.
- Rotating API Keys: This is a method of rotating API keys to avoid rate limiting. This is done by providing multiple of the same type of credential to the network scanning container, and then rotating through them as needed.