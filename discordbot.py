from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@client.event
async def on_message(message) #for tatsumaki
    if "credits reset in" in message.content():
        m = "今日の分のdailyは使用済みです。翌朝９時の日付リセットをお待ちくださいっ。"
        await message.channel.send(m)
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃあ')

    
bot.run(token)
