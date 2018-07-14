import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import time
from bs4 import BeautifulSoup
import json
import string

BOT_PREFIX = ("!", "!!")
TOKEN = "your discord token"
IP = 'your server ip'
PW = 'your i3d server password'
KEY = 'your rcon key'
PORT = 'your server port'

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

@client.command()
async def help():
        await client.say("Hello! I'm the Miscreated Manager, a discord tool for server renters and their staff!\nHere's what i can do!\n\n**!status** - Check some real-time status from server!\n\n**!sun** - Change the weather straight to a sunny sky!\n\n**!rain** - Change the weather straight to a rainy day!\n\n**!day** - Changes the ingame clock to 9AM\n\n**!night** - Change the ingame clock to Midnight!\n\n**!say (message)** - Sends an Admin Message to the game. *!say Hello Survivors!*\n\n**!whitelist (SteamID)** - Adds such number to the Whitelist database. *!Whitelist 123123*\n\n**!remove** - Removes someone from the Whitelist database. *!remove 123123*\n\n**!weather** - Changes the weather to a specific number/pattern!\n\n1-Clear Sky\n2-Light Rain\n3-Heavy Rain and Storm\n4-Heavy Storm\n5-Tornado Storm\n6-Tornado Rain and Thunder\n7-Light Fog\n8-Medium Fog\n9-Heavy Fog\n10-The Mist\n11-Rainbow\n12-Half Rainbow\n13-Rad Storm\n14-Nuclear Winter\n\n*!weather 13*\n\n**!kick** - Kick someone from the server, based on their SteamID *!kick 123123*!\n\n**!ban** - Ban someone from the server, based on their SteamID *!ban 123123*\n\n**!unban** - Lifts the ban someone from the server, based on their SteamID *!unban 123123*\n\n**!restart** - restart the server after X seconds. *!restart 60*")

@client.command(pass_context=True)
async def status():

    payload = { 'ip': IP,'key': KEY, 'password': PW, 'port': PORT}
    r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py?command=status", params=payload)

    ctx = r.text
    ctx = ctx.replace("Server Status:", '')
    str = ctx.replace("name:", '')
    ctx = ctx.replace("gamerules: Miscreated", '')
    ctx = ctx.replace("next ", '')
    ctx = ctx.replace("in", '')
    ctx = ctx.replace("pg", 'Ping')
    ctx = ctx.replace("steam:", 'SteamID:')
    ctx = ctx.replace("name:", 'User:')
    ctx = ctx.replace("round time remag: 0:00", '')
    ctx = ctx.replace('ip: Server50009', '')
    ctx = ctx.replace('version: 0.1.1.1972', '')
    ctx = ctx.replace('level: Multiplayer/islands', '')
    ctx = ctx.replace('round time remaining: 0:00', '')
    ctx = ctx.replace('uptime:', 'Online for:')
    ctx = ctx.replace('players:', 'How many Players Online:')
    ctx = ctx.replace('time:', 'Ingame Clock:')
    ctx = ctx.replace('restart :', 'Remaining Time until Restart:')

    await client.say(ctx)

@client.command()
async def sun():
        payload = { 'ip': IP,'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py?command=wm_startPattern+1", params=payload)
        await client.say("Sun is shining!")

@client.command()
async def rain():
        payload = {'ip': IP,'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py?command=wm_startPattern+3", params=payload)
        await client.say("Rain is pouring!")

@client.command()
async def day():
        payload = {'ip': IP,'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py?command=wm_forceTime+9", params=payload)
        await client.say("9AM it is!")

@client.command()
async def night():
        payload = {'ip': IP,'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get("http://servers.miscreatedgame.com/api/rcon_client.py?command=wm_forceTime+24", params=payload)
        await client.say("Midnight it is!")


@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
    r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=sv_say+Admin+Message:{0}'.format(str(mesg)),params=payload)
    await client.say("Message sent : "+str(mesg))

@client.command(pass_context = True)
async def whitelist(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=mis_whitelist_add+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : "+str(mesg) + " added to the whitelist!")

@client.command(pass_context=True)
async def remove(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=mis_whitelist_remove+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : " + str(mesg) + " removed from the Whitelist!")

@client.command(pass_context=True)
async def weather(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=wm_startPattern+{0}'.format(str(mesg)),params=payload)
        await client.say("Weather " + str(mesg) + " applied!")

@client.command(pass_context=True)
async def kick(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=mis_kick+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : " + str(mesg) + " kicked from the game!")

@client.command(pass_context=True)
async def ban(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=mis_ban_steamid+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : " + str(mesg) + " banned from the game!")

@client.command(pass_context=True)
async def unban(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=mis_ban_remove+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : " + str(mesg) + " unbanned from the game!")

@client.command(pass_context=True)
async def restart(ctx, *args):
        mesg = ' '.join(args)
        payload = {'ip': IP, 'key': KEY, 'password': PW, 'port': PORT}
        r = requests.get('http://servers.miscreatedgame.com/api/rcon_client.py?command=do_shutdown+{0}'.format(str(mesg)),params=payload)
        await client.say("SteamID : " + str(mesg) + " unbanned from the game!")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="SevenProxies' Bot"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers i am online:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)