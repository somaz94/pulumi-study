from pulumi_gcp import compute
from utils import Utils
import pulumi

class CDN:

    @staticmethod
    def create_managed_ssl_certificate(domains):
        return compute.ManagedSslCertificate(Utils.resource_name('ssl-cert'),
            name=Utils.resource_name('ssl-cert'),
            managed={
                'domains': domains
            }
        )
    
    @staticmethod
    def create_backend_bucket(bucket, dependencies=[]):
        backend_bucket_name = bucket.name.apply(lambda n: n.replace('.', '-') + '-backend')
        return compute.BackendBucket(Utils.resource_name('backend-bucket'),
            name=backend_bucket_name,
            bucket_name=bucket.name,
            enable_cdn=True,
            opts=pulumi.ResourceOptions(depends_on=dependencies)
        )

    @staticmethod
    def create_url_map(backend_bucket):
        return compute.URLMap(Utils.resource_name('url-map'),
            name=Utils.resource_name('url-map'),
            default_service=backend_bucket.self_link,
        )

    @staticmethod
    def create_global_address():
        return compute.GlobalAddress(Utils.resource_name('global-address'),
            name=Utils.resource_name('global-address')
        )

    @staticmethod
    def create_https_proxy(url_map, ssl_certificates):
        return compute.TargetHttpsProxy(Utils.resource_name('https-proxy'),
            name=Utils.resource_name('https-proxy'),
            url_map=url_map.self_link,
            ssl_certificates=[ssl_certificates.self_link]
        )

    @staticmethod
    def create_global_forwarding_rule(https_proxy, ip_address):
        return compute.GlobalForwardingRule(Utils.resource_name('https-forwarding-rule'),
            name=Utils.resource_name('https-forwarding-rule'),
            target=https_proxy.self_link,
            port_range="443",
            ip_address=ip_address
        )
