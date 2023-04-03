#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("24697766", default=None, cast=int)
API_HASH = config("1ce7de6596c962c77701f642ac6703c5", default=None)
SESSION = config("1AZWarzUBuxWwA4ptjBQjYXPYnY5El83KkF7Nwml8sLnDIu_pe-hR-Slm3YNSR8NBOMKlpT0gdNTJDV69wI3_m7vs5CFeFw3ugi4PVj-15QHpdR4QycQefeRPdUOXz-zQtf5puQXF2LP4u0VS8CkVNG-2P2gLjaoJJMthrsA08Jnhp3eKI5NPo2b-OB9PYEdrW57ZN8sFgMWD-oXwtF1HdHgt4PZ67BJPTAq63oHE63GpuF3gULMIAd2uQXTAtqeAbkcLDXX_dJP2Gz99u1e6F225eArKBrNxdA2HF2kX-k_32bMloJliPy0BeOE8vQgdNUYkr9RmO0mt3tjiX0o71wjSN-MgMI0=")
FROM_ = config("-1001691258104")
TO_ = config("-1001513912951")

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
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
