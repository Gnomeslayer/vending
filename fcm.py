from rustplus import FCMListener
from discord.ext import commands
import json

class FCM_COG(commands.Cog):
    def __init__(self, client):
        print("[Cog] FCM has been initiated")
        self.client = client
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.fcm_details = config['fcm_details']
        self.fcm = None
    
    
    
    @ commands.Cog.listener()
    async def on_ready(self):
        print("Establishing FCM Connection..")
        self.fcm = FCM(self.fcm_details).start()
        self.fcm.client = self.client
        print("FCM connection established.")

class FCM(FCMListener):
    
    client = None
    async def on_notification(self, obj, notification, data_message):
        print("On notifications triggered..")
        channel = self.client.get_channel(1128712915420205090)
        print("Retrieved channel...", channel)
        await channel.send(notification)
        print("Channel message sent!")

async def setup(client):
    await client.add_cog(FCM_COG(client))
