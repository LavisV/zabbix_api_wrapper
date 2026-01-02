from client import ZabbixClient

zapi = ZabbixClient(environment="prod")

slas = zapi.sla.get(output="extend")

print(slas)