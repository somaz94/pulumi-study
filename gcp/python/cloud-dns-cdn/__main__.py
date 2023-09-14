# main.py
import pulumi
from clouddns import CloudDNS
from storage import Storage
from cdn import CDN

# DNS
managed_zone = CloudDNS.create_managed_zone()

# SSL certificate
domains = ['web.gcp.somaz.link']
ssl_certificate = CDN.create_managed_ssl_certificate(domains)

# Storage - Depends on DNS
bucket = Storage.create_bucket([managed_zone])
index_html = Storage.upload_static_website(bucket)

# CDN - Depends on Storage
backend_bucket = CDN.create_backend_bucket(bucket, [bucket])
url_map = CDN.create_url_map(backend_bucket)
Storage.set_bucket_public_access(bucket) 

# Global IP Address
global_address = CDN.create_global_address()

# HTTPS Proxy
https_proxy = CDN.create_https_proxy(url_map, ssl_certificate)

# Global Forwarding Rule
forwarding_rule = CDN.create_global_forwarding_rule(https_proxy, global_address.address)

# A Record - Pointing to the global IP address
a_record = CloudDNS.create_a_record(managed_zone, global_address.address)

# Export the DNS name servers and CDN URL
pulumi.export('name_servers', managed_zone.name_servers)
pulumi.export('cdn_url', url_map.self_link)
