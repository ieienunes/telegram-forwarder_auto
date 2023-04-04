from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
from bs4 import BeautifulSoup

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
    for i in TO:
        try:
            # Modifying link in the message
            soup = BeautifulSoup(event.message.raw_text, 'html.parser')
            link = soup.find_all('a')[0]
            link['href'] = 'https://bit.ly/jogar_agoraa'  # Replace with your desired link
            modified_text = str(soup)

            await BotzHubUser.send_message(
                i,
                modified_text
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
