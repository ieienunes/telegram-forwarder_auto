from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

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

import re
from urlextract import URLExtract

extractor = URLExtract()

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            # extrair links da mensagem
            links = extractor.find_urls(event.message.message)
            
            # substituir o link antigo pelo novo
            for link in links:
                if "https://fwd.cx/HMY5zeG8hZYa" in link: # substituir pelo link antigo desejado
                    new_link = "https://fwd.cx/lmBBuPRNuDaQ" # substituir pelo novo link desejado
                    event.message.message = event.message.message.replace(link, new_link)
            
            # enviar a mensagem com o link substituído
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
