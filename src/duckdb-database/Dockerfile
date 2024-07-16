FROM debian:stable

# Add any additional setup steps or commands here
CMD ["apt-get", "update", "&&", "apt-get", "install", "wget", "unzip", "-y"]
CMD ["wget", "https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip"]

CMD ["/bin/bash"]