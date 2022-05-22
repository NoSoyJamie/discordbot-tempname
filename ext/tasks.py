#tasks.py

#any and all scheduled tasks

from init import *

class scheduled(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.index = 0
#		self.pfp_auto_change.start()

#	def cog_unload(self):
#		self.pfp_auto_change.cancel()

#	@tasks.loop(minutes=15)
#	async def pfp_auto_change(self):
#		pfp_path = random.choice(os.listdir('assets/pfp/'))
#		with open('assets/pfp/'+pfp_path, "rb") as pfp:
#			image = discord.File(pfp)
#			await bot.user.edit(password=None, avatar=pfp.read())
#			print(f'Changed pfp to {pfp_path}')
#
#	@pfp_auto_change.before_loop
#	async def before_printer(self):
#		print('Waiting until bot is ready to start ')
#		await self.bot.wait_until_ready()

def setup(bot):
	bot.add_cog(scheduled(bot))
