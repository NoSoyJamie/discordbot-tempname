#admin.py

#admin commands, this is where you got your kick, ban, role state, whatever

from init import *

##Ramsay, sic @user
##kicks mentioned user, tagging them in the process
@commands.command(name='sic', help='kicks a user')
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member: discord.Member):
	await ctx.send('<@!{0.id}> BARK BARK BARK BARK'.format(member))
	await member.kick()

#init the above as commands

def setup(bot):
	bot.add_command(kick)