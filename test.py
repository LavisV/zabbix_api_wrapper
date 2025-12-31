from client import ZabbixClient

zapi = ZabbixClient(environment="prod")

users = zapi.users.get(selectMedias="extend")

for user in users["result"]:
    for media in user["medias"]:
        email = media["sendto"][0]
        print(f"[{user['userid']}] - "
              f"{user['name']} "
              f"{user['surname']}: "
              f"{email}")

other_users = zapi.users.get()              