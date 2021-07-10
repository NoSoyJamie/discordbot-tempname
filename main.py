#main.py

import os
import math
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='Ramsay, ')

@bot.command()
async def sit(ctx):
	await ctx.send('Fuck you, I do what I want.')
	print(f'COMMAND CALLED: 	COMMAND:	sit\n			USER:		{ctx.author}')

@bot.command()
async def shit(ctx):
	await ctx.send(file=discord.File('BRAP.mp3'))
	print(f'COMMAND CALLED: 	COMMAND:	shit\n			USER:		{ctx.author}')

@bot.event
async def on_ready():
	print(
		f'READY\n'
	)



@bot.event
async def on_member_join(member):
	print(f'MEMBER JOIN: 	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')
#	await member.create_dm()
#	await member.dm_channel.send(
#		f'BARK BARK BARK BARK BARK'
#	)

@bot.event
async def on_member_remove(member):
	print(f'MEMBER LEAVE:	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')

@bot.event
async def on_guild_join(guild):
	print(f'SERVER JOIN:	GUILD:		{guild.name}\n		GUILD ID:	{guild.id}\n		OWNER:		{guild.owner}\n		OWNER ID:	<@!{guild.owner_id}>\n')

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.content == '*knock knock*' and message.author != bot.user:
		dog_words = ['BARK', 'BARK BARK', 'BARK BARK BARK', 'BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK BARK']
		response = random.choice(dog_words)
		await message.channel.send(response)
		print(f'MESSAGE SEND:	{response}\n')
		return
	elif message.content == 'test':
		raise discord.DiscordException

@bot.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}\n')
			print(f'Unhandled Message\n')
		else:
			raise

bot.run(TOKEN)
