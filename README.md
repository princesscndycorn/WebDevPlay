# WebDevFun
Basic Webdev fun w/ Containers


# Into

This is a basic FastAPI, Celery & Redis. It's missing NGINX, i'll add that later. Going to be using as a "API", where the remote workers talk to REDIS via SSH. 

Currently, Celery workers connect will fail unless you change "ssl_cert_reqs" to "none". Not recommended since it's not secure. If you have an offical SSL Cert, you will not need to do this. But this fails due to it being a self signed cert.

# Generate Certs

In the redis folder in the app, run the following to generate some certs. Again this is just for testing, you really should use official certs, not self signed certificates. Create a Certificate Authority (CA) (if you don’t already have one)

```
openssl req -x509 -nodes -newkey rsa:4096 \
  -keyout redis.key \
  -out redis.crt \
  -days 365 \
  -config redis_san.cnf \
  -extensions v3_req
```

# Adding Clinet Certs to validate Connected CLients

Create a private key and CSR for a client

```
openssl genrsa -out client.key 4096

openssl req -new -key client.key -out client.csr \
  -subj "/C=US/ST=State/L=City/O=YourOrg/CN=myclient"
```

# Sign Clinet CA with current CA

Sign the CSR with your CA to produce a client cert

```
openssl x509 -req -in client.csr -CA redis.crt -CAkey redis.key \
  -CAcreateserial -out client.crt -days 365 -sha256
```

