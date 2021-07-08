#main.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(
		f'{client.user.name} has connected to to Discord!'
	)

@client.event
async def on_member_join(member):
	print(f'{member.name} has joined the guild!')
	await member.create_dm()
	await member.dm_channel.send(
		f'BARK BARK BARK BARK BARK'
	)

@client.event
async def on_member_remove(member):
	print(f'{member.name} has left the guild!')

client.run(TOKEN)
