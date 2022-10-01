#!/usr/bin/env python3
import discord
import os
from logger import Logger

log = Logger().logger

intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False

BOT_TOKEN = os.environ['PULSE_BOT_TOKEN']

#bot = commands.Bot(command_prefix='!')

client = discord.Client(intents=intents)

async def role_selector_embed():
    embed = discord.Embed(
        title="Channel Role Selector",
        type="rich",
        description="Select the reaction emoji below to access other channels.",
        color=discord.Color.blue()
        )
    embed.add_field(
        name="Serious",
        value="😩 - News and Politics",
        inline=True
        )
    embed.add_field(
        name="Un-Serious",
        value="😆 - Tech, Images, Food, Music",
        inline=True
        )
    embed.add_field(
        name="Games",
        value="🎮 - Gaming",
        inline=True
        )
    embed.add_field(
        name="Twitter - US News",
        value=":flag_us: - AP and ABC News Twitter",
        inline=True
        )
    return embed

@client.event
async def on_ready():
    channel = client.get_channel(1025568270612451328)
    deleted = await channel.purge()
    text = "Select your feed role"
    rs_embed = await role_selector_embed()
    message = await channel.send(embed=rs_embed)
    await message.add_reaction('😩')
    await message.add_reaction('😆')
    await message.add_reaction("🎮")
    await message.add_reaction("🇺🇸")
    log.info("Role Selector Channel Setup Complete")

@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(1025568270612451328)
    if reaction.message.channel.id != channel.id:
        return
    if str(reaction.emoji) == '😆':
        role = discord.utils.get(user.guild.roles, name="serious")
        await user.add_roles(role)
        log.info(f'Assigned {user} the serious role')
    if str(reaction.emoji) == '😩':
        role = discord.utils.get(user.guild.roles, name="unserious")
        await user.add_roles(role)  
        log.info(f'Assigned {user} the unserious role')  
    if reaction.emoji == "🎮":
        role = discord.utils.get(user.guild.roles, name="games")
        await user.add_roles(role)
        log.info(f'Assigned {user} the games role')
    if reaction.emoji == "🇺🇸":
        role = discord.utils.get(user.guild.roles, name="us-news")
        await user.add_roles(role)
        log.info(f'Assigned {user} the us-news role')

@client.event
async def on_reaction_remove(reaction, user):
    channel = client.get_channel(1025568270612451328)
    if reaction.message.channel.id != channel.id:
        return
    if str(reaction.emoji) == '😆':
        role = discord.utils.get(user.guild.roles, name="serious")
        await user.remove_roles(role)
        log.info(f'Removed the serious role from {user}')
    if str(reaction.emoji) == '😩':
        role = discord.utils.get(user.guild.roles, name="unserious")
        await user.remove_roles(role)
        log.info(f'Removed the unserious role from {user}') 
    if str(reaction.emoji) == "🎮":
        role = discord.utils.get(user.guild.roles, name="games")
        await user.remove_roles(role)
        log.info(f'Removed the games role from {user}')
    if reaction.emoji == "🇺🇸":
        role = discord.utils.get(user.guild.roles, name="us-news")
        await user.remove_roles(role)   
        log.info(f'Removed the us-news role from {user}')   

if __name__ == "__main__":
    client.run(BOT_TOKEN)