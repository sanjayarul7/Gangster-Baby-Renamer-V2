import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7603382668:AAHN8FcS90sDaTdN9IHLGu_AKs9R4TcQNs0")

API_ID = int(os.environ.get("API_ID", "22928570"))

API_HASH = os.environ.get("API_HASH", "60bb37bddecb48c27c3e86906a077603")

STRING = os.environ.get("STRING", "BQGFzVUAxsUqrhGS1aBnjwQbO0ucEFP75lvhObyrZegzX8jmZrCInu-pSrTu97qEuqej1DD2zd2w7VoNP2-rdU57HPNXfXvQChJztWUFJygOUXnFqhLHIEuOgI9sC91wZxwWwrC1grOyw66y1E9ubWxgbo9kZsSyhpgnihsRCkFBFTCvd3X-yAt6JyMLUWpZVl_daD99g59Orso9duK7EYKvDrK_pY34jAvL5yud7tfYgt0CrPjWDBK6o0zyv3O1xlAhagXAPwQW50wZfVbVzGedhBB5I_oTdPJsh5MuEaNRT5dQS7SuBf0F08AAYQPfZgAAaxTnOtjcIwr8pGWKkUeogRoiHAAAAAB3zmrgAA")



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
