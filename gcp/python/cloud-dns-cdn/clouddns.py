from pulumi_gcp import dns
from utils import Utils

class CloudDNS:

    @staticmethod
    def create_managed_zone():
        return dns.ManagedZone(Utils.resource_name('managed-zone'),
            name=Utils.resource_name('managed-zone'),
            dns_name='gcp.somaz.link.',
            description='Managed by Pulumi',
        )
    
    @staticmethod
    def create_a_record(managed_zone, ip_address):
        return dns.RecordSet(Utils.resource_name('a-record'),
            name='web.gcp.somaz.link.',
            type='A',
            ttl=300,
            managed_zone=managed_zone.name,
            rrdatas=[ip_address],
        )
