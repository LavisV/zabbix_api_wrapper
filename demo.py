# demo.py

from client import ZabbixClient

client = ZabbixClient(environment="dev")

# Get existing hostgroups
hostgroups = client.host_group.get()
print(hostgroups)