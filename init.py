#init.py

#imports all the shit, loads the vars, sets intents and whatever other config is needed

#TODO make a database schema to store vars in different files, per server (folder) > per user (file). Store slots_weight in file alongside other relevant vars

import os
import math
import random
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import bot


from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DEFAULT_PREFIX')
DB_FOLDER = os.getenv('DATABASE_FOLDER')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

#client = commands.Bot(command_prefix={PREFIX}, intents=intents)
bot = commands.Bot(command_prefix={PREFIX}, intents=intents)

##when ready, initalizes the bot
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('Discord version: ',discord.__version__)
	print('------')
	for guild in bot.guilds:
		if os.path.isdir(f"{DB_FOLDER}/{guild.id}"):
#			print('Discovered known server, skipping...')
			pass
		else:
#			print('Discovered unknown server, creating db entry...')
			os.mkdir(f"{DB_FOLDER}/{guild.id}")
	print('INIT SUCCESFUL\n')

