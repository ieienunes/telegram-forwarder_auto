from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
import re

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    # Encontre a mensagem na qual você deseja substituir o link
    message = event.message.message

    # Substitua "APOSTE AQUI" pelo link desejado
    link = "https://bit.ly/jogar_agoraa"
    message_with_link = re.sub("APOSTE AQUI", f'<a href="{link}">APOSTE AQUI</a>', message)

    # Encaminhe a mensagem com o link para todos os chats TO
    for i in TO:
        try:
            await BotzHubUser.send_message(i, message_with_link)
        except Exception as e:
            print(e)


print("Bot has started.")
BotzHubUser.run_until_disconnected()
