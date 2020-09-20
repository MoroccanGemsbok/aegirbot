import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.') #Aegirbot command prefix


#Tells you when Aegirbot is ready to rock and roll
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Aegir Life'))
    print('Aegirbot is ready.')


#Ping command to find latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Fuck off! {round(client.latency * 1000)}ms')


#Pic of Aegir command
@client.command()
async def pic(ctx):
    pictures = ['https://imgur.com/F2UhyI4',
                'https://imgur.com/51YfC6m',
                'https://imgur.com/Y3cWAFA',
                'https://imgur.com/b9ab84N',
                'https://imgur.com/m9yolDG',
                'https://imgur.com/s0nv6IX',
                'https://imgur.com/yD18plG',
                'https://imgur.com/tXn7zcy',
                'https://imgur.com/wVuJ48N',
                'https://imgur.com/weompm7',
                'https://imgur.com/syvTjFn',
                'https://imgur.com/mJT8N67',
                'https://imgur.com/JDwI3nm',
                'https://imgur.com/IuTbaFo',
                'https://imgur.com/XI3UYQv',
                'https://imgur.com/td9PrSW',
                'https://imgur.com/iCw7FEf',
                'https://imgur.com/zplmtyR',
                'https://imgur.com/V1qhyu3',
                'https://imgur.com/F47qXHj',
                'https://imgur.com/5GwZILV',
                'https://imgur.com/V0toia5',
                'https://imgur.com/95ZNol8',
                'https://imgur.com/fMeaI8k',
                'https://imgur.com/UMCyooO',
                'https://imgur.com/Lmka6IP',
                'https://imgur.com/jxboPQq',
                'https://imgur.com/RDCEtV1',
                'https://imgur.com/QEljUxX']

    await ctx.send(f'{random.choice(pictures)}'.format(ctx))


#Aegir StopStopStop Comment
@client.command()
async def aegir(ctx):
    await ctx.send(f'Stop stop stop. Its actually over.')


#Aegir Shut up Comment
@client.command()
async def shutup(ctx):
    await ctx.send(f'Shut up. Please shut up.')
    await ctx.send(f'https://imgur.com/JgfEmNu')


#say command
@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


#weirdchamp
@client.command()
async def weirdchamp(ctx):
    await ctx.send(f'https://imgur.com/qK1PD1T')


#When you say aegir the bot does :at:
@client.event
async def on_message(message):
    await client.process_commands(message)
    truemessage = message.content.lower() #converts message to all lowercase

    if 'aegir' in truemessage:
        await message.add_reaction(':at:699437200672292935')


'''
@client.event
async def on_message(message):
    aegir1 = 'aegir'  # Word that you want to check in a string
    aegir2 = 'Aegir'
    aegir3 = 'AEGIR'

    if aegir1 in message.content:
        await message.add_reaction(':at:699437200672292935')
    elif aegir2 in message.content:
        await message.add_reaction(':at:699437200672292935')
    elif aegir3 in message.content:
        await message.add_reaction(':at:699437200672292935')
'''

client.run('NzUyMTkxNTk2MjE2MzIwMTAw.X1UDAw.5isGbIFuEo0bsFeOB0mGv4Uxo_s')
