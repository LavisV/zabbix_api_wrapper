from client import ZabbixClient

zapi = ZabbixClient(environment="prod")

slas = zapi.sla.getsli(slaid=3, period_from=1735708800, period_to=1735795200)

print(slas)