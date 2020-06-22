import discord, os
from misc import misc
from discord.ext import commands, tasks
import random


miscFunctions = misc()
client = commands.Bot(command_prefix = "?", case_insensitive=True)
client.remove_command('help')

#Confirming bot is ready
@client.event
async def on_ready():
    print ('Bot is ready.')

#Error handling for if a valid command is not given
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That is not a valid command. Type in ?help to see all the commands')

#Flip a coin
@client.command()
async def coin(ctx):
    await ctx.send('```' + miscFunctions.randomCoin() + '```')

#Roll a dice
@client.command()
async def dice(ctx):
    await ctx.send('```' + miscFunctions.randomDice() + '```')

#Roast londa
@client.command()
async def londa(ctx):

    value = miscFunctions.londaQuotes()
    if (str(value[0]) == 'String'):
        await ctx.send('```' + value[1] + '```')
    elif (str(value[0]) == 'Picture'):
        embed = discord.Embed()
        embed.set_image(url = value[1])
        await ctx.send(embed=embed)

@client.command()
async def callout(ctx, target: discord.Member, *, reason):
    await ctx.send(target.mention + ' has been called out for ' + '_**```' + str(reason) + '```**_')

@callout.error
async def calloutError(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You forgot to mention somebody or give a reason to call them out. Check ?help for a list of commands and how to use them')

@client.command()
async def calloutall(ctx):
    pass

@calloutall.error
async def calloutallError(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You forgot to mention somebody. Check ?help for a list of commands and how to use them')

@client.command()
async def tanyo(ctx):
    pass

# @client.command()
# async def github(ctx):
#     await ctx.send(miscFunctions.githubTest())

#Fucking worst command
@client.command()
async def quitter(ctx):
    await ctx.send('```' + str(miscFunctions.quitter()) + ' days since quitting```')

#Get the list of commands
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed()

    embed.add_field(name ='?coin', value = 'Flip a coin', inline = False)
    embed.add_field(name ='?dice', value = 'Roll a dice', inline = False)
    embed.add_field(name ='?londa', value = 'Returns a quote', inline = False)
    embed.add_field(name ='?callout', value = 'Calls your target out. Needs a target mention and a reason', inline = False)

    await author.send(embed=embed)

client.run(os.environ['DISCORD_TOKEN'])