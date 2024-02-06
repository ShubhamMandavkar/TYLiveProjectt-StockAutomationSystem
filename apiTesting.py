from telethon import TelegramClient
from apiDetails import apiId, apiHashId

# The first parameter is the .session file name (absolute paths allowed)

client = TelegramClient('MySession', apiId, apiHashId)
with client:
        client.loop.run_until_complete(client.send_message('Me', 'This is testing message'))

