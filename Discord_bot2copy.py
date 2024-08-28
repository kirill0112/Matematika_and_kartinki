import discord
import os
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def sum(ctx, a, b):
    await ctx.send(int(a) + int(b))
@bot.command()
async def difference(ctx, a, b):
    await ctx.send(int(a) - int(b))
@bot.command()    
async def degree(ctx, a, b):
    await ctx.send(int(a) ** int(b))
@bot.command()    
async def multiplication(ctx, a, b):
    await ctx.send(int(a) * int(b))
@bot.command()
async def podeli(ctx, a, b):
    await ctx.send(int(a) / int(b))
@bot.command()
async def meme(ctx):
    images = os.listdir('Images')
    with open('Images/' + random.choice(images), "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("Token")