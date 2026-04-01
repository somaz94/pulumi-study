from pulumi_gcp import dns
from config import DNS_DOMAIN, WEB_DOMAIN
from utils import Utils

class CloudDNS:

    @staticmethod
    def create_managed_zone():
        return dns.ManagedZone(Utils.resource_name('managed-zone'),
            name=Utils.resource_name('managed-zone'),
            dns_name=f'{DNS_DOMAIN}.',
            description='Managed by Pulumi',
        )
    
    @staticmethod
    def create_a_record(managed_zone, ip_address):
        return dns.RecordSet(Utils.resource_name('a-record'),
            name=f'{WEB_DOMAIN}.',
            type='A',
            ttl=300,
            managed_zone=managed_zone.name,
            rrdatas=[ip_address],
        )
