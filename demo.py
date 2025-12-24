# demo.py

from client import ZabbixClient

client = ZabbixClient(environment="dev")

# Simple get query
hosts = client.host.get()
tklab_hosts = {
    "name": [],
    "hostid": []
}

for host in hosts["result"]:
    if "tklab" in host["name"].lower():
        tklab_hosts["name"].append(host["name"])
        tklab_hosts["hostid"].append(host["hostid"])

print(tklab_hosts["name"])
print(tklab_hosts["hostid"])

api_info = client.apiinfo.version()
print(api_info)