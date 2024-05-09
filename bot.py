import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7032781845:AAEPQF-Ynv6FDVAUo68ZJXqOnw1V9rp-kTw")

API_ID = int(os.environ.get("API_ID", "25848289"))

API_HASH = os.environ.get("API_HASH", "88cf2c17c7a2bd21f4204c89c648dd40")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
