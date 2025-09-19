import os
import ssl

broker_url = os.environ.get("BROKER_URL")
result_backend = os.environ.get("BROKER_URL")

# # SSL config (can be None, True, or dict)
# broker_use_ssl = {
#     "ssl_cert_reqs": ssl.CERT_NONE,   # was 'none' in your snippet
#     "ssl_ca_certs": "/app/redis.crt",
#     "ssl_certfile": "/app/client.crt",
#     "ssl_keyfile": "/app/client.key",
# }
