#error.py

#this file will handle all errors, hopefully

from init import *

##checks for permission to run a command, relies on discord permission for auth
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