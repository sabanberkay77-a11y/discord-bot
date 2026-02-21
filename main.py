import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, amount: int):
    if amount <= 0:
        await ctx.send("❌ Geçerli sayı gir.")
        return

    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"✅ {amount} mesaj silindi.")
    await msg.delete(delay=3)

bot.run(TOKEN)
