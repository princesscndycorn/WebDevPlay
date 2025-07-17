# WebDevFun
Basic Webdev fun w/ Containers


# Into

This is a basic FastAPI, Celery & Redis. It's missing NGINX, i'll add that later. Going to be using as a "API", where the remote workers talk to REDIS via SSH. 

Currently, Celery workers connect will fail unless you change "ssl_cert_reqs" to "none". Not recommended since it's not secure. If you have an offical SSL Cert, you will not need to do this. But this fails due to it being a self signed cert.

This simulates running a worker on a seperate network then the redis.

# Generate Certs

In the redis folder in the app, run the following to generate some certs. Again this is just for testing, you really should use official certs, not self signed certificates. Create a Certificate Authority (CA) (if you don’t already have one)

```
openssl genrsa -out ca.key 4096

openssl req -x509 -new -nodes -key ca.key \
  -sha256 -days 1825 \
  -out ca.crt \
  -subj "/C=US/ST=State/L=City/O=YourOrg/CN=MyRedisTestCA"

openssl genrsa -out redis.key 4096

openssl req -new -key redis.key -out redis.csr \
  -subj "/C=US/ST=State/L=City/O=YourOrg/CN=redis-server"

openssl x509 -req -in redis.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out redis.crt -days 365 -sha256

openssl genrsa -out client.key 4096

openssl req -new -key client.key -out client.csr \
  -subj "/C=US/ST=State/L=City/O=YourOrg/CN=myclient"

openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out client.crt -days 365 -sha256
```


# Example Sans Configuration 

```
[ req ]
default_bits       = 4096
prompt             = no
default_md         = sha256
req_extensions     = v3_req
distinguished_name = dn

[ dn ]
C = US
ST = State
L = City
O = YourOrg
CN = redis-server

[ v3_req ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = redis-server
IP.1 = 127.0.0.1


openssl req -new -key redis.key -out redis.csr -config redis_san.cnf
openssl x509 -req -in redis.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out redis.crt -days 365 -sha256 -extensions v3_req -extfile redis_san.cnf

```


# Openrand hex

```
openssl rand -hex 32
```

# Testing 

```
redis-cli -h host.docker.internal -p 6380
```

