import discord
import random
import os
import requests
from discord.ext import commands
import time
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
print('aaaa')
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    

@bot.command()
async def mem(ctx):
    img_name = os.listdir('abcd')
    with open(f'abcd/{random.choice(img_name)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def info(ctx):
    await ctx.send('ддя начала тебе надо пройти краткую теорию по команде #teo,затем посмотреть мемы по команде #mem, и наконец пройти викторину по команде #quiz')


@bot.command()
async def teo(ctx):
    await ctx.send('в 18 веке в европе началась промышленная революция')
    time.sleep(3)
    await ctx.send('в последствии чего появились фабрики и заводы')
    time.sleep(3)
    await ctx.send('с этого момента началась эта история в большим маштабе')
    time.sleep(3)
    await ctx.send('конечно, до этого момента тоже был мусор')
    time.sleep(3)
    await ctx.send('но в сравнении до и после это земля и небо')
    time.sleep(3)
    await ctx.send('в это время на земле 8 миллиардов человек')
    time.sleep(3)
    await ctx.send('и львиная доля из них мусорят до 400 кг в год')
    time.sleep(3)
    await ctx.send('есть органические и химические отходы')
    time.sleep(3)
    await ctx.send('если органические отходы быстро разлагаются')
    time.sleep(3)
    await ctx.send('то химическии нет')
    time.sleep(3)
    await ctx.send('помимо этого в возду выходит газ')
    time.sleep(3)
    await ctx.send('из-за чего над Антарктидой появилась озоновая дыра')
    time.sleep(3)
    await ctx.send('озоновая дыра - дыра в озоновом слое земли')
    time.sleep(3)
    await ctx.send('поэтому тают ледники и появляется потоп')

@bot.command()
async def quiz(ctx):
    await ctx.send('вопрос 1     В каком веке случилась промышленная революция? ответ пиши в виде #q question_number answer')

@bot.command()
async def q(ctx,question_number:int, answer:str):
    if question_number == 1 and answer == '18':
        await ctx.send('верно.Сколько кг в среднем мусорит человек в год?')
    elif question_number == 2 and answer == '400':
        await ctx.send('верно.огрызок органический отход?')
    elif question_number == 3 and answer == 'да':
        await ctx.send('верно.над чем была озоновая дыра? (пиши в именительном падеже с маленькой буквы)')
    elif question_number == 4 and answer == 'антарктида':
        await ctx.send('верно.это был последний вопрос')
    else:
        await ctx.send('не верный ответ или не вернo заполнение')
    
bot.run("TOKEN")
