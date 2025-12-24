# demo.py

from client import ZabbixClient

client = ZabbixClient(environment="dev")

# Get existing hostgroups
hosts = client.host.get()

print(hosts)