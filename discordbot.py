from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(f'{PREFIX}help'):
        msg1 = "안녕하세요. 저는 Lol4j 전용 bot 입니다. 사용가능한 명령어는 아래와 같습니다."
        msg2 = "/진영 : 블루/레드 중 랜덤으로 진영 선택"

        await message.channel.send(msg1)
        await message.channel.send(msg2)

    if message.content.startswith(f'{PREFIX}진영'):

        lanes = ['블루', '레드']
        index = random.randrange(0, len(lanes))

        await message.channel.send(lanes[index])


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.", e)