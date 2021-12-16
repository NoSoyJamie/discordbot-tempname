#main.py

from init import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DEFAULT_PREFIX')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix={PREFIX}, intents=intents)
bot = commands.Bot(command_prefix={PREFIX}, intents=intents)

##init bot
@bot.event
async def on_ready():
	print(f"READY\n")

##import slot extension
bot.load_extension("slots")

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

##responds to *knock knock* with random.choice(dog_words)
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

##checks for permission to run a command
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'<@!{ctx.message.author.id}> BARK BARK BARK BARK')
		print(f'KICK FAILURE:	USER:	<@!{ctx.message.author.id}>\n')
		return
	raise error

##generic error checker, logs error, without message
@bot.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}\n')
			print(f'Unhandled Message\n')
		else:
			raise

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

##Ramsay, sic @user
##kicks mentioned user, tagging them in the process
@bot.command(name='sic', help='kicks a user')
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member: discord.Member):
	await ctx.send('<@!{0.id}> BARK BARK BARK BARK'.format(member))
	await member.kick()

bot.run(TOKEN)
