#Vatsal Savani
#Random Image Uploader Discord Bot
#A discord bot that retrieves and sends a random image based of a search term given with a command


import discord, random, os
from discord.ext.commands import Bot
from discord.ext import commands

#Setting up connection
Client = discord.Client()
botPrefix = '>'
client = commands.Bot(command_prefix = botPrefix)

#Do the following things once bot is ready
@client.event	
async def on_ready () :
	print('Bot Online!')
	print('Name : {}'.format(client.user.name))
	print('ID : {}'.format(client.user.id))




images  = [[], []]

#Gets all images from a directory named ImagePool and the categories within it.
for file in os.listdir('.\ImagePool/') :
	images[0].append(file)
	images[1].append(os.listdir('./ImagePool/'+ file))


@client.command(pass_context = True)
async def randompic (ctx, search: str) :

	if search == 'list' :
		await client.say('Categories are : ')
		for p in images[0] :
			await client.say(p)
	else :
		#Uploads random image if search term is part of imagepool categories
		if search in images[0] :
			CindexNum = images[0].index(search)
			category = search
			imageName = images[1][CindexNum][random.randint(0, len(images[1][CindexNum]) - 1)]

		#If search term is not found, it uploads a random image from all
		else :	
			await client.say ('Sorry no such category, showing random image!')
			CindexNum = random.randint(0, len(images[0]))
			category = images[0][CindexNum]
			imageName = images[1][int(CindexNum)][random.randint(0, len(images[1][CindexNum]) - 1)]

		sendimage = "./ImagePool/" + category + '/' + imageName
		print(sendimage)
		await client.send_file(ctx.message.channel, sendimage)


#Client Token (Discord App Token)
client.run('XXX')
