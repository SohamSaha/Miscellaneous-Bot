import discord
#from misc import misc
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = "?", case_insensitive=True)
client.remove_command('help')

#miscFunctions = misc()

@client.event
async def on_ready():
    print ('Bot is ready.')

# @client.event
# async def on_command_error(ctx,error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('That is not a valid command. Type in !help to see all the commands')

# @client.event
# async def coin(ctx):
#     await ctx.send('```' + miscFunctions.randomCoin() + '```')

# @client.event
# async def dice(ctx):
#     await ctx.send('```' + miscFunctions.randomDice() + '```')

# @client.command()
# async def londa(ctx):

#     value = miscFunctions.londaQuotes()
#     if (str(value[0]) == 'String'):
#         await ctx.send('```' + value[1] + '```')
#     elif (str(value[0]) == 'Picture'):
#         embed = discord.Embed()
#         embed.set_image(url = value[1])
#         await ctx.send(embed=embed)

# @client.command(pass_context=True)
# async def help(ctx):

#     author = ctx.message.author

#     embed = discord.Embed()

#     embed.add_field(name ='!coin', value = 'Flip a coin', inline = False)
#     embed.add_field(name ='!dice', value = 'Roll a dice', inline = False)
#     embed.add_field(name ='!londa', value = 'Returns a quote', inline = False)

#     await author.send(embed=embed)


client.run(miscFunctions.clientToken())