from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
import html2text

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

# Define a mensagem personalizada aqui:
MENSAGEM_PERSONALIZADA = "https://bit.ly/jogar_agoraa"

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    mensagem = event.message
    plain_text_message = html2text.html2text(mensagem.message)
    for i in TO:
        mensagem_completa = f"{plain_text_message}\n\n{MENSAGEM_PERSONALIZADA}"
        try:
            await BotzHubUser.send_message(
                i,
                mensagem_completa
            )
        except Exception as e:
            print(e)


print("Bot has started.")
BotzHubUser.run_until_disconnected()
