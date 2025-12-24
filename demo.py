# demo.py

from client import ZabbixClient

client = ZabbixClient(environment="dev")

# Simple get query
hosts = client.host.get()
servers = {
    "name": [],
    "hostid": []
}

for host in hosts["result"]:
    if "server" in host["name"].lower():
        servers["name"].append(host["name"])
        servers["hostid"].append(host["hostid"])

print(servers["name"])
print(servers["hostid"])