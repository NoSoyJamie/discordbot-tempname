#main.py

import os
import math
import random
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
		f'READY\n'
	)

@client.event
async def on_member_join(member):
	print(f'MEMBER JOIN: 	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')
	await member.create_dm()
	await member.dm_channel.send(
		f'BARK BARK BARK BARK BARK'
	)

@client.event
async def on_member_remove(member):
	print(f'MEMBER LEAVE:	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')

@client.event
async def on_guild_join(guild):
	print(f'SERVER JOIN:	GUILD:		{guild.name}\n		GUILD ID:	{guild.id}\n		OWNER:		{guild.owner}\n		OWNER ID:	<@!{guild.owner_id}>\n')

client.run(TOKEN)
