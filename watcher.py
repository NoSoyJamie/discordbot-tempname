#watcher.py

#watches events and outputs to terminal

from init import *

##outputs to terminal when user joins server
@bot.event
async def on_member_join(member):
	print(f'MEMBER JOIN: 	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')
##automatically sends user a message on server join
#	await member.create_dm()
#	await member.dm_channel.send(
#		f'BARK BARK BARK BARK BARK'
#	)

##outputs to terminal when user leaves server
@bot.event
async def on_member_remove(member):
	print(f'MEMBER LEAVE:	USER:		{member}\n		USER ID:	<@!{member.id}>\n		GUILD:		{member.guild.name}\n		GUILD ID:	{member.guild.id}\n')

##outputs to terminal when bot is invited to new server
@bot.event
async def on_guild_join(guild):
	print(f'SERVER JOIN:	GUILD:		{guild.name}\n		GUILD ID:	{guild.id}\n		OWNER:		{guild.owner}\n		OWNER ID:	<@!{guild.owner_id}>\n')

#init the above as listeners

def setup(bot):
	bot.add_listener(on_member_join)

def setup(bot):
	bot.add_listener(on_member_remove)

def setup(bot):
	bot.add_listener(on_guild_join)