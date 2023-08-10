import json
import cryptocode
from discord.ext import commands
from discord import Option
from mctools import RCONClient
from discord.ext import tasks


class RCON(commands.Cog):
    def __init__(self, client):
        with open('config.json', 'r') as jsonFile:
            config = json.load(jsonFile)
        self.rcon = RCONClient(config['rcon_host'], port=config['rcon_port'])
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.check_status.start()

    @commands.slash_command(name='cmd', description='Отправляет команду на сервер')
    async def cmd(self, ctx, command: Option(str, description='Команда', required=True)):
        with open('config.json', 'r') as jsonFile:
            config = json.load(jsonFile)

        if ctx.author.id == 396961790778540032 or ctx.author.id == 785775906521350174:
            print(f"rcon-cmd: {ctx.author}: {command}")
            try:
                password = cryptocode.decrypt(config['rсоn_раsswоrd'], config['wth'][:-1])
                self.rcon.login(password)
                response = self.rcon.command(command).replace("[0m", "")
                self.rcon.stop()
                await ctx.respond(f"Команда выполнена! Результат:\n> {response}")
            except Exception as e:
                await ctx.respond(f"Команда не была выполнена! Попробуйте позже\n> {e}")
        else:
            await ctx.respond('Тебе нельзя использовать консоль, сорян')

    @tasks.loop(minutes=5)
    async def check_status(self):
        with open('config.json', 'r') as jsonFile:
            config = json.load(jsonFile)
        server_status = config['status_server']

        try:
            password = cryptocode.decrypt(config['rсоn_раsswоrd'], config['wth'][1:-1])
            self.rcon.login(password)
            self.rcon.command("save-all")
            self.rcon.stop()
            if server_status == 'offline':
                print("rcon-task: Сервер онлайн!")
                config['status_server'] = 'online'
                await self.client.get_channel(config['status_channel']).send('Сервер онлайн!')
        except Exception as e:
            print(e)
            if server_status == 'online':
                print("rcon-task: Сервер оффлайн!")
                config['status_server'] = 'offline'
                await self.client.get_channel(config['status_channel']).send('Сервер оффлайн(')
        finally:
            with open('config.json', 'w') as jsonFile:
                json.dump(config, jsonFile, indent=4)


def setup(client):
    client.add_cog(RCON(client))