#main.py

from init import *

##import admin commands
bot.load_extension("admin")
print(f'Loaded Module: admin\n')

##import error handler
bot.load_extension("error")
print(f'Loaded Module: error\n')

##import watcher
bot.load_extension("watcher")
print(f'Loaded Module: watcher\n')

##import slot extension
bot.load_extension("slots")
print(f'Loaded Module: slots\n')

##import slot extension
bot.load_extension("fun")
print(f'Loaded Module: fun\n')

##init bot
@bot.event
async def on_ready():
	print(f'INIT SUCCESFUL\n')

bot.run(TOKEN)
