#fun.py

#random useless commands, use this to expiriment I guess?

from init import *

##responds to *knock knock* with random.choice(dog_words)
##this is fucking terrible, redo this, use 'bark' xrandom amount of times instead of this dog_words list shit
#@bot.event
#async def on_message(message):
#	await bot.process_commands(message)
#	if message.content == '*knock knock*' and message.author != bot.user:
#		dog_words = ['BARK', 'BARK BARK', 'BARK BARK BARK', 'BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK BARK']
#		response = random.choice(dog_words)
#		await message.channel.send(response)
#		print(f'MESSAGE SEND:	{response}\n')
#		return
#	elif message.content == 'test': #???
#		raise discord.DiscordException

class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

##Ramsay, sit
	@commands.command()
	async def sit(self, ctx):
		await ctx.reply(f'I refuse, <@!{ctx.author.id}>')
		print(f'COMMAND CALLED: 	COMMAND:	sit\n			USER:		{ctx.author}')

##Ramsay, shit
	@commands.command()
	async def shit(self, ctx):
		await ctx.send(file=discord.File('assets\BRAP.mp3'))
		print(f'COMMAND CALLED: 	COMMAND:	shit\n			USER:		{ctx.author}')

#init the above as commands

#def setup(bot):
#	bot.add_listener(on_message)

def setup(bot):
	bot.add_cog(fun(bot))