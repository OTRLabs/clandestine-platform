FROM debian:stable
RUN apt-get update && apt-get install wget unzip -y \
	&& wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip \
	&& unzip duckdb_cli-linux-amd64.zip \
	&& chmod +x duckdb \
	&& mv duckdb /usr/local/bin

CMD ["/bin/bash", "&&" "/usr/local/bin/duckdb"]