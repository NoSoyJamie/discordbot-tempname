#init.py

#imports all the shit, loads the vars, sets intents and whatever other config is needed

import os
import math
import random
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import Bot
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DEFAULT_PREFIX')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix={PREFIX}, intents=intents)
bot = commands.Bot(command_prefix={PREFIX}, intents=intents)