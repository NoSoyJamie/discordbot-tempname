#error.py

#this file will handle all errors, hopefully

from init import *

class error_handle(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

##checks for permission to run a command, relies on discord permission for auth
#	@bot.event
#	async def on_command_error(self, ctx, error):
#		if isinstance(error, commands.MissingPermissions):
#			await ctx.send(f'I\'m afraid I cant let you do that, <@!{ctx.message.author.id}>.')
#			print(f'KICK FAILURE:	USER:	<@!{ctx.message.author.id}>\n')
#			return
#		raise error

##generic error checker, logs error, without message
#	@bot.event
#	async def on_error(self, event, *args, **kwargs):
#		with open('err.log', 'a') as f:
#			if event == 'on_message':
#				f.write(f'Unhandled message: {args[0]}\n')
#				print(f'Unhandled Message\n')
#			else:
#				raise

#init the above as listeners

def setup(bot):
	bot.add_cog(error_handle(bot))