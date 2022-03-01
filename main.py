import discord
import os    
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(' with ur mom'))
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-ping'):
    await message.channel.send('pong!')

  if message.content == '-invite':
    await message.channel.send('**dyrex bot doesnt have a server rn, but thanks for your interest!**')

  if message.content == '-balls':
    await message.channel.send('https://m.media-amazon.com/images/I/61Jigwd1kKL._AC_SX425_.jpg')

  if message.content == '-squid':
    await message.channel.send('GAMES⁉️')
  
  if message.content == 'khai is annoying':
    await message.channel.send('agreed')      
  


client.run(os.environ['TOKEN'])
