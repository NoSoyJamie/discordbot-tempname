#main.py

from init import *

##import admin commands
bot.load_extension("ext.admin")
print(f'Loaded Module: admin\n')

##import error handler
bot.load_extension("ext.error")
print(f'Loaded Module: error\n')

##import watcher
bot.load_extension("ext.watcher")
print(f'Loaded Module: watcher\n')

##import slot extension
bot.load_extension("ext.slots")
print(f'Loaded Module: slots\n')

##import fun extension
bot.load_extension("ext.fun")
print(f'Loaded Module: fun\n')

##import test extension
bot.load_extension("ext.test")
print(f'Loaded Module: test\n')

##import ./ext/*.py as a cog

#for filename in os.listdir('./ext'):
#	if filename.endswith('.py'):
#		bot.load_extension(f'ext.{filename[:-3]}')
#		print(f'Loaded extesion {filename[:-3]}')
#	else:
#		print(f'Unable to load {filename[:-3]}')

bot.run(TOKEN)
