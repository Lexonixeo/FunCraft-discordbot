import discord
import math
from datetime import datetime, timezone
from discord.ext import commands


class Voting(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channelIds = [1134182815337025628, 1129713156684529814]
        playerRole = discord.utils.get(message.guild.roles, id=1130377725585133620)
        if message.channel.id == 1130378298883575909 and playerRole not in message.author.roles\
                or message.channel.id in channelIds:
            await message.add_reaction("✅")
            await message.add_reaction("❌")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channelIds = [1134182815337025628, 1129713156684529814]
        message = reaction.message
        playerRole = discord.utils.get(message.guild.roles, id=1130377725585133620)
        if message.channel.id == 1130378298883575909:
            if playerRole not in message.author.roles and user.id != 1117791868646858925:
                await reaction.remove(user)
            else:
                yes, no = 0, 0
                for react in message.reactions:
                    if react == "✅":
                        yes = react.count
                    elif react == "❌":
                        no = react.count
                duration = datetime.now(timezone.utc) - message.created_at
                if (yes >= 1 + math.ceil(len(playerRole.members) / 2)) or (divmod(duration.seconds, 3600)[0] >= 2 and yes - no >= 7):
                    await message.add_reaction("☑️")
                    await message.author.add_roles(playerRole)
                    await self.client.get_channel(1135891623285375066).send(f'Игрок "{message.author}" был(а) принят(а)!')
                elif no >= 1 + math.ceil((len(playerRole.members) + 1) / 2):
                    await message.add_reaction("⛔")
                    await self.client.get_channel(1135891623285375066).send(
                        f'Игрок "{message.author}" не был(а) принят(а)!')
        elif message.channel.id in channelIds:
            yes, no = 0, 0
            for react in message.reactions:
                if react == "✅":
                    yes = react.count
                elif react == "❌":
                    no = react.count
            duration = datetime.now(timezone.utc) - message.created_at
            if (yes >= 1 + math.ceil(len(playerRole.members) / 2)) or (divmod(duration.seconds, 3600)[0] >= 2 and yes - no >= 5):
                await message.add_reaction("☑️")
                await self.client.get_channel(1135891623285375066).send(f'Идея "{str(message)}" была принята!')
            elif no >= 1 + math.ceil((len(playerRole.members) + 1) / 2):
                await message.add_reaction("⛔")
                await self.client.get_channel(1135891623285375066).send(f'Идея "{str(message)}" была отвергнута!')


def setup(client):
    client.add_cog(Voting(client))