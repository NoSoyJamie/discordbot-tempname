#piderman.py

from init import *

class spiderman(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='picture', help='Gets you a picture of spiderman! (5% chance to kick frog)')
	async def picture(self, ctx):
		frog = ctx.guild.get_member(426759102668996618)
		print(f'COMMAND:      picture  \nUSER:	{ctx.author}\n\n')
		if random.random() < 0.05:
			await ctx.send(f'What is this damn amphibian creature doing on my desk!')
			try:
				await frog.kick()
			except AttributeError:
				pass
			await asyncio.sleep(2)
			await ctx.send(f'Alright, that should take care of that. Here\'s that picture of spiderman you asked for. ')
		spiderman_path = random.choice(os.listdir('assets/spiderman/'))
		with open('assets/spiderman/'+spiderman_path, "rb") as spiderman_pic:
			image = discord.File(spiderman_pic)
			await ctx.send(file=image)


#init the above as commands

def setup(bot):
	bot.add_cog(spiderman(bot))
