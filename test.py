from client import ZabbixClient

zapi = ZabbixClient(environment="prod")

slas = zapi.sla.getsli(slaid=3, period_from=1767225600, period_to=1767311999)

print(slas)