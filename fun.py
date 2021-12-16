#fun.py

#random useless commands, use this to expiriment I guess?

from init import *

##responds to *knock knock* with random.choice(dog_words)
##this is fucking terrible, redo this, use 'bark' xrandom amount of times instead of this dog_words list shit
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.content == '*knock knock*' and message.author != bot.user:
		dog_words = ['BARK', 'BARK BARK', 'BARK BARK BARK', 'BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK', 'BARK BARK BARK BARK BARK BARK']
		response = random.choice(dog_words)
		await message.channel.send(response)
		print(f'MESSAGE SEND:	{response}\n')
		return
	elif message.content == 'test': #???
		raise discord.DiscordException

##Ramsay, sit
@bot.command()
async def sit(ctx):
	await ctx.reply('No.')
	print(f'COMMAND CALLED: 	COMMAND:	sit\n			USER:		{ctx.author}')

##Ramsay, shit
@bot.command()
async def shit(ctx):
	await ctx.send(file=discord.File('BRAP.mp3'))
	print(f'COMMAND CALLED: 	COMMAND:	shit\n			USER:		{ctx.author}')