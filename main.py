import nextcord, os, time, json
from nextcord.ext import commands, tasks

with open("./config.json") as file:
    config = json.load(file)

client = commands.Bot(command_prefix=[".h ",".h"], intents=nextcord.Intents.all())
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print(f"-----\nLogged in as: {client.user.name} : {client.user.id}\n-----\nMy current prefix is: .h\n-----")
    if not update_status.is_running():
        update_status.start()

@tasks.loop(seconds=300)
async def update_status():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"{len(set(client.get_all_members()))} Players Hearts!"))

@client.command()
async def ping(ctx):
    start_time = time.time()
    ping_embed = nextcord.Embed(title="Ping/Latency", description=f"Pong! 🏓 \nLatency: {round(client.latency * 1000)}ms", color=0xf54242)
    ping_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
    message = await ctx.reply(embed=ping_embed)
    end_time = time.time()
    edited_ping_embed = nextcord.Embed(title="Ping/Latency", description=f"Pong! 🏓 \nLatency: {round(client.latency * 1000)}ms\nResponse Time: {round((end_time - start_time) * 1000)}ms", color=0xf54242)
    edited_ping_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
    await message.edit(embed=edited_ping_embed)

@client.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CommandOnCooldown):
        print(error)
        await ctx.reply(f'Error: `{error}`')
        await ctx.message.add_reaction('❌')
    elif isinstance(error, commands.CommandOnCooldown):
        if round(error.retry_after) > 3600:
            em = nextcord.Embed(title=f"This command is on cooldown!",
                            description=f"Try again in {round(error.retry_after) // 3600} hours!", colour=0xBA55D3)
            await ctx.reply(embed=em)
        elif round(error.retry_after) < 3600:
            em = nextcord.Embed(title=f"This command is on cooldown!",
                            description=f"Try again in {round(error.retry_after) // 60} minutes!", colour=0xBA55D3)
            await ctx.reply(embed=em)
        elif round(error.retry_after) < 60:
            em = nextcord.Embed(title=f"This command is on cooldown!",
                            description=f"Try again in {round(error.retry_after)} seconds!", colour=0xBA55D3)
            await ctx.reply(embed=em)

client.run(config['token'])