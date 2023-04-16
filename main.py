import discord
import download

URL = "Video or Audio URL"
TOKEN = "Discord Token"
VOICE_CHANNEL = "voice channel"


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        channel = client.get_channel(VOICE_CHANNEL)
        voice_client = await channel.connect()

        voice_client.play(discord.FFmpegPCMAudio(download.load(
            URL
        )))


intents = discord.Intents.all()

client = MyClient(intents=intents)

client.run(TOKEN)
