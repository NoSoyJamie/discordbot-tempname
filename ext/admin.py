#admin.py

#admin commands, this is where you got your kick, ban, role state, whatever

from init import *

class administration(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

##Ramsay, sic @user
##kicks mentioned user, tagging them in the process
	@commands.command(name='kick', help='kicks a user')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member, *, reason = None):
		await ctx.send(f'<@!{user.id}> BARK BARK BARK BARK')
		await user.kick()

#kills the bot
	@commands.command(name='kill', help='Calls `exit()` in python, only the owner can use this.')
	@commands.is_owner()
	async def kill(self, ctx):
		await ctx.send('Bark.', file=discord.File('assets\kill.jpg'))
		exit()

def setup(bot):
	bot.add_cog(administration(bot))