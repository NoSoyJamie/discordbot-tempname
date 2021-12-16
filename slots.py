#slots.py

from init import *

#TODO make a database schema to store vars in different files, per server (folder) > per user (file). Store slots_weight in file alongside other relevant vars
@commands.command(name='slots', help='WIP, slots command, say !slots wheel_amount weight to generate a shitty array.')
async def slot_machine(ctx, wheel_amount: int, weight: float):
	print(f'COMMAND CALLED: 	COMMAND:	slots\n			USER:		{ctx.author}		WHEELS:		{wheel_amount}\n')
	wheel = []
	for i in range(wheel_amount):
		num = round(random.random(),2)
		wheel.append(num)
	wheel_weight = [round(x * weight,2) for x in wheel]
	await ctx.send(f'Your values are: {wheel}. \nWith {weight} weight applied, rounded to 2 places they\'re {wheel_weight}.')

#init the above as commands

def setup(bot):
	bot.add_command(slot_machine)