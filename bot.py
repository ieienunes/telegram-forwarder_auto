from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
import markdown
import asyncio
from telethon.tl.functions.messages import DeleteMessagesRequest 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("ATIVANDO...")

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

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM, pattern=r'(?i)(?!.*✅✅✅ GREEN ✅✅✅)'))
async def sender_bH(event):
    message = event.message
    # substituir textos específicos antes de encaminhar a mensagem
    if 'Penalty Shoot-Out' in message.text:
        message.text = message.text.replace('Penalty Shoot-Out', 'ROBO VIP')
        
    if '✅ OPORTUNIDADE IDENTIFICADA' in message.text:
        message.text = message.text.replace('✅ OPORTUNIDADE IDENTIFICADA', '**✅ ENTRADA CONFIRMADA**')
    if '' in message.text:
        message.text = message.text.replace('', '')
    if '' in message.text:
        message.text = message.text.replace('', '')
    if '' in message.text:
        message.text = message.text.replace('', '')
    
    
    
    # Loop over the target chats
    for i in TO:
        try:
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
            original_message.text = original_message.text.replace("https://realsbet.com/casino/game/1292733", "https://estrelabet.com/ptb/games/casino/detail/normal/9611")
            
            # Forward the modified message to the target chat
            await BotzHubUser.send_message(i, original_message)
            
            
        except Exception as e:
            print(e)


print("BOT INICIADO.")
BotzHubUser.run_until_disconnected()
