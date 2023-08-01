import discord
import json


with open('config.json', 'r') as jsonFile:
    config = json.load(jsonFile)


bot = discord.Bot(activity=discord.Game('approaching D̵̶̞͍̯̦͔͉̣̞̥̭̙̖̦̟͈̤̜͇͓̟͔͍͍̯͔̖̙͓̯̰͔͔͔̭͕͙̝͍̀͗̿̊̆̀͑̈̌́̄̇̓̊̿̾̉͑̓̄̉̀͑͆͋̐̓̿̏̏̽͛̇̉̅̓̍̚҈͎̥̖͇̖͚̣̦̞͍̦̩̥̞̪̫̝͆̓̓̒̏̃̆͗͐̃̎̀͐̓̃͐̈́̑̍̀̐́̚ͅ҈̯͍͈̩̞̣̳͖͚͈̦͖̝̟͎͎͍͓̰̤̯͔͐͒̉̔̋̔́̓̍͂̎͑̔̍̃͌͊͐̀̈̎ͅ0̸̪͎̰̥̪̣̬͚̙͕̮̮̱͉͈̬̪͙̣͍̱̫̘͆̄̄̅̓̍͗͒̈͆͌̋̑̒͒̌̀̌̌͑̈ͅ҉̵̷̰̥͓̰̙̲̘̭̤͕͔͍̖̟͍̦͇̬̥̘͓͇̤̱̖̮̮̪̞̬̗̖͇̯̖̟̖̘͉͙̰̣̮̲̖̲̬̳̩͖̱̩͓̥̦̞̯̔̓͗͐̎̎̎̑̈̀̒̃͛͂̎͊̅̿̿̽̒͂̿̌̀͗͑̏͊͂̇͐͑͛̈́̌͋̔̀̅̅̋̏̈̆̌ͅǍ̷̸̷̴̜̖̫͙͍̳̣͔̞͙͖͎̲͖̳̪̠̖̩̯͍̘͉͉̜͇̯͙̦̦͖͈̥̭̰̤̲̜̞̘̤̦̗̠͖̯̥̝̗̦̳̲̲̤̣͚̥̦͚͇͚͌̎̇̇́̎͆̉͑̌̍̎̅̇̽͆̂̄̒̔͋̂̂̎̏̽͐͂̋͑̔̿͒͂̏̂̇̉̀̅̉͒͆͛̄̌́͋͛̉̒́͋̀͗̋̓͆̄͐̐̿͌̌̓͆̿͂̑̊͊̆͌̚̚ͅͅͅ4̶̴̷̵͎̗̟̥̣̥͎̬̰̩̜͍̳̠̜͕̤̠̩͖̳̝͍̗̙͔̣͉͈͓̦̞̣̬̠̰̗̩̜͙̟̝̞̙͓͇͇͕̱͉͔̝̖̘͉͇̥̳͖̝̙̙̉͑̌̓̓̓̿͆̋̑́̂́̅̔̓̂͌̈́̍̊̿͗͋͐̌͑̅͊͑̍̆̐͐̿̃̒̄̽͌̓͑̆̎̂̈́̓̅̍̒̑̆̆̉̆̄͑͒̚̚ͅD̷͙̬̯̬̰̠͕̪͙͈͎̰͔̍̿̓͊̍̿͐̒̊̾͆̂̋̿̽͊͊͒͗̃͊ͯ̚҈̷̸͈̩̜̩͖͓̭̙͍̟͍͎̳͓͇̜̘͍̬̘̥͇͎̩̭̘̝͓̰̳͖̦̙͕͍̥̥̭̣̱͖͖̭͎̝͚̘̝̝͕̗̳̪͗̈́͆̌͗̾͒͑̾̀͒̓̉̅̓̃͐̄̈́̌̈̊̀̽̀̒̄͆̊͒͌͗̂̆́͆́̀͆̄̌̓̔̌̋̍̎̃͋͑̓͑̓̐̑̀́̒̚̚ͅͅͅ0҈͇̭̥̯̣͈̝̟̮͍͓͇̜̜̪̝̓͐͛̑̒̿̋͌͗͆̈̌̀̀̽ͤ̚̚̚҉͓͈̬͔͇͙͔̠̤͎̠͉̠̯͙̟͙͈̠̝̑̔͆͒̒̅͊͌̐͑͑̋̅̄͛̆̐́̈̂̍̉̓̇ͤ҈̴̖͎̠̲̣̫̲͚̲̠̮͉̗̗̤͕̠̤̮͇̯̙͔̬̤̗̖̟̫̜̗̙͓̪̯͖͈̲̅͛̀̃͗͛̃̆̿̅̾̔͗̃̑̊̓̊̓͛́͊̊̊̀͋͋̈́̆̔̚ͅ9̷̵̵͕͇̱̯͍̝̝̝̤̲͕̖̬̯͕̫͓͈̯̮̖͇͔͖̯̥̙̝̣̪̖̲͇̘͎͙̬̟̬͙̦̖͖̫͚͉̦̞͉̯̫̦̯̞̖̪͒̀̾́͑̏͊̋̔̀̄̈̂ͦ͑̑́͑̉̐͒̑̂̉̅̏̑͆̽̒͋̅̉́̽̽̍̑̑͌̚Ã̵̟̞͉̣͕̱͉͔̘͈̳̏̆̍̂̎͐̽́̂̃̀͌̀̒̒͑̏̐͋̾̄̋ͅ'))
bot.load_extension("voice")
bot.load_extension("RCON")


@bot.event
async def on_ready():
    print(f"{bot.user} запущен!")


@bot.slash_command(name='close', description='Выключает бота')
async def close(ctx):
    if ctx.author.id == 396961790778540032:
        print("Выключение...")
        await ctx.respond('Команда выполнена! Выключаюсь...')
        await bot.close()
    else:
        await ctx.respond('Команда не была выполнена! Вы не `lexonixeo`')


bot.run(config['bot_token'])
