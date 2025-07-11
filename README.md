# WebDevFun
Basic Webdev fun w/ Containers


# Into

This is a basic FastAPI, Celery & Redis. It's missing NGINX, i'll add that later. Going to be using as a "API", where the remote workers talk to REDIS via SSH. 

Currently, Celery workers connect will fail unless you change "ssl_cert_reqs" to "none". Not recommended since it's not secure. If you have an offical SSL Cert, you will not need to do this. But this fails due to it being a self signed cert.