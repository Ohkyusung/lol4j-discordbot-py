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
        msg1 = "안녕하세요. 저는 Lol4j 전용 bot 입니다. 현재 사용가능한 명령어는 아래와 같습니다."
        msg2 = "$진영 : 블루 혹은 레드 진영 중에서 랜덤으로 진영 선택"

        await message.channel.send(msg1)
        await message.channel.send(msg2)

    if message.content.startswith(f'{PREFIX}진영'):

        sender_name = message.content.replace(f'{PREFIX}진영', '')

        lanes = ["https://i.namu.wiki/i/-OlrrdE1BOHPVNrUTFMrll0FbUPMUAPimjuALz-ES874TNlOt9eCvq0kyQudfufIFMGJj8kqcjD6vRHaV8ipyESYgtDsh_e_BhS97YjpsLNjZW0VVKegM5APoD5yyxp3wui0_PwrOUAhHdMHFzLd9A.webp", 
                 "https://i.namu.wiki/i/OOeoWDX7g0D5sdD5hL80GQDn4IybHqH6hZfpiJV3stj65NSEW8QElQzng4VQ--J5PhHql_SdT0K81cgKSFkIEBtYcLLNaSxxTSwtB8ftEasHiinFQNgmPtnn0bBTzChLpGAF5F21Mh438ujjv-8YTQ.webp"]
        index = random.randrange(0, len(lanes))

        embed = discord.Embed(title=sender_name + " 님의 랜덤 진영 뽑기", description="", color=0x62c1cc)
        embed.set_thumbnail(url=lanes[index])

        await message.channel.send(embed=embed)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.", e)