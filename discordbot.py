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

    print(message)
    sender_name = message.author.nick

    # 봇이 스스로 보낸 메시지에는 응답하지 않음
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(f'{PREFIX}help'):

        # Embed 생성
        embed = discord.Embed(
            title="📖 Lol4j Bot 도움말 가이드 📖",
            description="사용 가능한 명령어 목록과 사용법은 다음과 같습니다:",
            color=0xdfff32  # 색상 설정
        )

        logo_image_url = "https://i.ibb.co/XLvq1zj/lol4j.png"
        embed.set_thumbnail(url=logo_image_url)

        # 명령어 가이드 추가
        embed.add_field(
            name="$랜덤대진표 [팀1] [팀2] [팀3] ...",
            value="입력된 팀 목록에서 랜덤으로 대진표를 생성합니다.\n예시: `$랜덤대진표 LG 테슬라 삼성 현대 롯데 기아`",
            inline=False
        )

        embed.add_field(
            name="$맵추첨",
            value="랜덤으로 스타크래프트 맵을 추첨하고 해당 맵의 이미지를 보여줍니다.",
            inline=False
        )

        embed.add_field(
            name="$진영추첨",
            value="랜덤으로 리그오브레전드 진영을 추첨하고 해당 진영의 이미지를 보여줍니다.",
            inline=False
        )

        embed.add_field(
            name="$help",
            value="이 도움말 가이드를 표시합니다.",
            inline=False
        )

        embed.add_field(
            name="소스코드 참고",
            value="https://github.com/Ohkyusung/lol4j-discordbot-py",
            inline=False
        )

        embed.add_field(
            name="대회공식 사이트",
            value="https://www.lol4j.com",
            inline=False
        )

        # 결과를 보내기
        await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}진영추첨'):

        # 맵 리스트 및 이미지 URL 딕셔너리
        lanes = {
            "블루(좌측)": "https://i.ibb.co/4VBbKQP/image.png",  # 블루 이미지 URL
            "레드(우측)": "https://i.ibb.co/r5J4Jhw/image.png",  # 레드 이미지 URL
        }

        lanes_color = {
            "블루(좌측)": 0x0000ff,  # 블루 색상
            "레드(우측)": 0xff0000,  # 레드 색상
        }
        
        # 랜덤 맵 선택
        chosen_lanes = random.choice(list(lanes.keys()))
        map_image_url = lanes[chosen_lanes]  # 선택된 맵의 이미지 URL
        chosen_lanes_color = lanes_color[chosen_lanes]

        # Embed 생성
        embed = discord.Embed(
            title="🌟 리그오브레전드 진영 추첨 🌟", 
            description=f"**{sender_name}**님의 진영은 **{chosen_lanes}**!!", 
            color=chosen_lanes_color  # 색상 설정
        )

        logo_image_url = "https://i.ibb.co/XLvq1zj/lol4j.png"
        embed.set_thumbnail(url=logo_image_url)

        # 대표 이미지 설정
        embed.set_image(url=map_image_url)
        
        # 결과를 보내기
        await message.channel.send(embed=embed)

    # 랜덤 대진표 생성
    if message.content.startswith('$랜덤대진표'):
        # 메시지에서 명령어와 팀을 분리
        parts = message.content.split()
        teams = parts[1:]  # 첫 번째 부분은 명령어이므로 제외

        # 팀 목록을 섞음
        shuffled_teams = list(teams)
        random.shuffle(shuffled_teams)

        # 대진표 생성
        matches = []
        for i in range(0, len(shuffled_teams) - 1, 2):
            match = f"{shuffled_teams[i]} ⚔️ {shuffled_teams[i + 1]}"
            matches.append(match)

        # 남는 팀이 있는지 확인
        if len(shuffled_teams) % 2 != 0:
            matches.append(f"{shuffled_teams[-1]} 매칭 안됨")

        # Embed 생성
        embed = discord.Embed(
            title="🌟 랜덤대진표 🌟",
            color=0xdfff32  # 색상 설정
        )
        
        # 매치 이미지 URL (온라인 이미지 경로)
        match_image_url = "https://i.ibb.co/6YcN4v1/Minimal-Modern-You-Are-Enough-Quote-Desktop-Wallpaper.png"  # 이 부분을 실제 이미지 URL로 변경하세요
        logo_image_url = "https://i.ibb.co/XLvq1zj/lol4j.png"

        # 썸네일 설정
        embed.set_thumbnail(url=logo_image_url)

        # 각 매치를 Embed에 추가
        for idx, match in enumerate(matches):
            embed.add_field(name=f"🏆 MATCH ROOM {idx + 1}", value=match, inline=False)

        # 대표 이미지 설정 (Embed의 하단에 큰 이미지 추가)
        embed.set_image(url=match_image_url)

        # Footer에 점수 규칙 추가
        embed.set_footer(text="🏅 승리 시 : +3점\n🏅 패배 시 : +1점\n🤷 상대팀 불참으로 몰수승 혹은 참가팀 홀수로 매칭 불가 시 : +0.5점\n⏰ 10분 지각 시 : -0.5점\n⏰ 15분 초과 지각 시 : -1점, 몰수패\n경기 후 반드시 경기결과 채널에 경기결과를 남겨주세요.")

        # 결과를 보내기
        await message.channel.send(embed=embed)

    # 스타크래프트 맵 추첨
    if message.content.startswith(f'{PREFIX}맵추첨'):
        # 맵 리스트 및 이미지 URL 딕셔너리
        maps = {
            "투혼": "https://i.ibb.co/FKzJVMN/image.png",  # 투혼 맵 이미지 URL
            "파이썬": "https://i.ibb.co/grDWWvN/image.png",  # 파이썬 맵 이미지 URL
            "신-단장의능선": "https://i.ibb.co/pfgdbw0/image.png"  # 신-단장의 능선 맵 이미지 URL
        }
        
        # 랜덤 맵 선택
        chosen_map = random.choice(list(maps.keys()))
        map_image_url = maps[chosen_map]  # 선택된 맵의 이미지 URL

        # Embed 생성
        embed = discord.Embed(
            title="🌟 스타크래프트 맵 추첨 🌟", 
            description=f"**{sender_name}**님께서 플레이 할 맵은 **{chosen_map}**!", 
            color=0xdfff32  # 색상 설정
        )

        logo_image_url = "https://i.ibb.co/XLvq1zj/lol4j.png"
        embed.set_thumbnail(url=logo_image_url)

        # 대표 이미지 설정
        embed.set_image(url=map_image_url)
        
        # 결과를 보내기
        await message.channel.send(embed=embed)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.", e)