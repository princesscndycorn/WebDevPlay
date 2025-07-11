# WebDevFun
Basic Webdev fun w/ Containers


# Into

This is a basic FastAPI, Celery & Redis. It's missing NGINX, i'll add that later. Going to be using as a "API", where the remote workers talk to REDIS via SSH. 

Currently, Celery workers connect will fail unless you change "ssl_cert_reqs" to "none". Not recommended since it's not secure. If you have an offical SSL Cert, you will not need to do this. But this fails due to it being a self signed cert.

# Generate Certs

In the redis folder in the app, run the following to generate some certs. Again this is just for testing, you really should use official certs, not self signed certificates. 

```
openssl req -x509 -nodes -newkey rsa:4096 \
  -keyout redis.key \
  -out redis.crt \
  -days 365 \
  -config redis_san.cnf \
  -extensions v3_req
```

