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
            message = event.message
            original_message = None
            # Check if the message is forwarded
            if message.forward:
                # Get the original message
                original_message = await message.get_reply_message()
            # Otherwise, the message is not forwarded
            else:
                # The original message is the same as the message received
                original_message = message
            
            # Modify the original message to include the new link
            original_message.text = original_message.text.replace("https://fwd.cx/HMY5zeG8hZYa", "https://bit.ly/jogar_agoraa")
            
            # Forward the modified message to the target chat
            await BotzHubUser.send_message(i, original_message)
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
