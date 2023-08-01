from gtts import gTTS
import asyncio
import random
import discord
import time
import requests
import hashlib
from discord.ext import commands
from discord import Option
from discord.ext import tasks
import json


def get_joke():
    with open('config.json', 'r') as jsonFile:
        config = json.load(jsonFile)
    with open('jokes.txt', 'r', encoding='utf8') as file:
        jokes = file.readlines()

    query = 'pid=' + config["joke_pid"] + '&method=getRandItem&uts=' + str(int(time.time()))
    signature = hashlib.md5((query + config["joke_key"]).encode())
    url = 'http://anecdotica.ru/api?' + query + '&hash=' + signature.hexdigest()
    result = requests.get(url).json()
    if result['result']['error'] != 0:
        final_joke = jokes[random.randint(0, len(jokes) - 1)]
        return final_joke.replace('\\n', '\n')
    else:
        final_joke = requests.get(url).json()['item']['text'].replace("\n","\\n").replace("\r","\\n").replace("\\n\\n","\\n")
        if final_joke not in jokes:
            with open('jokes.txt', 'a', encoding="utf8") as f:
                f.writelines(f"\n{final_joke}")
        return final_joke.replace('\\n', '\n')


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.joke.start()

    @commands.slash_command(name='connect', description='Подключиться к голосовому каналу')
    async def connect(self, ctx):
        if ctx.guild.id == 1129436257693470842:
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
            await ctx.respond('Подключение успешно!')
        else:
            await ctx.respond('К сожалению, бот работает только на сервере FunCraft(')

    @commands.slash_command(name='knsh')
    async def knsh(self, ctx):
        if ctx.author.id == 786902643188432908 or ctx.author.id == 396961790778540032:
            secretSound = discord.FFmpegPCMAudio(f"sounds/secret.mp3")
            for vc in self.client.voice_clients:
                while vc.is_playing():
                    await asyncio.sleep(10)
                else:
                    vc.play(secretSound)
                    print(f"voice-knsh: {str(ctx.author)}")

    @commands.slash_command(name='say', description='Сказать в голосовой канал')
    async def say(self, ctx, text: Option(str, description='Сообщение', required=True)):
        with open('config.json', 'r') as jsonFile:
            config = json.load(jsonFile)
        i = config['voice_sound_count']

        if len(text) <= 1970:
            await ctx.respond(f'Скоро скажу данное сообщение: {text}')
        else:
            await ctx.respond(f'Скоро скажу данное сообщение: {text[:1967]}...')
        for vc in self.client.voice_clients:
            while vc.is_playing():
                await asyncio.sleep(10)
            else:
                obj = gTTS(text=text, lang='ru', slow=False)
                obj.save(f"sounds/{i}.mp3")
                textSound = discord.FFmpegPCMAudio(f"sounds/{i}.mp3")
                vc.play(textSound)
                print(f"voice-say: {str(ctx.author)}: {text}")

        config['voice_sound_count'] += 1
        with open('config.json', 'w') as jsonFile:
            json.dump(config, jsonFile, indent=4)

    @commands.slash_command(name='disconnect', description='Отключиться от голосового канала')
    async def disconnect(self, ctx):
        for vc in self.client.voice_clients:
            if vc.guild == ctx.guild:
                await vc.disconnect()
        await ctx.respond('Отключение произошло успешно!')

    @tasks.loop(seconds=120)
    async def joke(self):
        with open('config.json', 'r') as jsonFile:
            config = json.load(jsonFile)
        i = config['voice_sound_count']

        for vc in self.client.voice_clients:
            while vc.is_playing():
                await asyncio.sleep(10)
            else:
                if random.randint(0, 9) == 0:
                    secretSound = discord.FFmpegPCMAudio(source=f"sounds/secret.mp3")
                    print("voice-task: Секретный звук")
                    vc.play(secretSound)
                else:
                    joke = get_joke().replace('\n', ' ')
                    text = f"Внимание! Шутка!\n{joke}\nФить-ха!"
                    obj = gTTS(text=text, lang='ru', slow=False)
                    obj.save(f"sounds/{i}.mp3")
                    jokeSound = discord.FFmpegPCMAudio(source=f"sounds/{i}.mp3")
                    print(f"voice-task: Анекдот: \"{joke}\"")
                    vc.play(jokeSound)

        config['voice_sound_count'] += 1
        with open('config.json', 'w') as jsonFile:
            json.dump(config, jsonFile, indent=4)


def setup(client):
    client.add_cog(Voice(client))