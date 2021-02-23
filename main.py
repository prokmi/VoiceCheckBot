import os
import discord

TOKEN = os.environ['DISCORD_KEY']

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        members = await member.guild.fetch_members().flatten()
        for nomember in members:
            if member.name == "Prokmi" and (nomember.name == "Wolo" or nomember.name == "Prokmi"):
                if not nomember.dm_channel:
                    await nomember.create_dm()
                await nomember.dm_channel.send(f"Prokmi se připojil na voice! "
                                               f"Přijď za ním, až se ti to bude hodit. :slight_smile:")

client.run(TOKEN)
