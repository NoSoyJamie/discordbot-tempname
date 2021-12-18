#slots.py

from init import *

class gambling(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

#WIP Slots command, will eventually use database
#values for user balance, emojis to use in wheels,
#and weighting for how often users will win
	@commands.command(name='slots', help='WIP')
	async def slot_machine(self, ctx, wheel_amount: int, weight: float):
		print(f'COMMAND CALLED: 	COMMAND:	slots\n			USER:		{ctx.author}		WHEELS:		{wheel_amount}\n')
		wheel = []
		for i in range(wheel_amount):
			num = round(random.random(),2)
			wheel.append(num)
		wheel_weight = [round(x * weight,2) for x in wheel]
		await ctx.send(f'Your values are: {wheel}. \n\nWith {weight} weight applied, rounded to 2 places they\'re {wheel_weight}.')

#init the above as commands

def setup(bot):
	bot.add_cog(gambling(bot))