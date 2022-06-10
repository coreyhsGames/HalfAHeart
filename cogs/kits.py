import nextcord, time
from nextcord.ext import commands

class kits(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def klist(self, ctx):
        kitlist_embed = nextcord.Embed(title="List of Available Kits in OGUHC", description=f"There are currently 11 available in OGUHC, you can use `.hkinfo (kit name)` for information about that kit.", color=0xf54242)
        kitlist_embed.add_field(name="List of Available Kits", value="• Miner (miner)\n• Warrior (warrior)\n• Knight (knight)\n• Healer (healer)\n• Meat Lover (meatlover)\n• Sniper (sniper)\n• Tank (tank)\n• Energix (energix)\n• Rookie (rookie)\n• Baseball Player (baseballplayer)\n• Pyro (pyro)", inline=False)
        kitlist_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitlist_embed)

    @commands.group(invoke_without_command=True)
    async def kinfo(self, ctx):
        await ctx.reply("Use this command to get information about kits. To get the list of the kits, use `.hklist`. Also, the command will not work if it is uppercase, it has to be lowercase.")
    
    @kinfo.command(name='miner')
    async def miner_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Miner Kit Information", description=f"• Enchanted Stone Pickaxe (Unbreaking 1, Efficiency 1)\n• 14 Bread", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='warrior')
    async def warrior_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Warrior Kit Information", description=f"• Enchanted Stone Axe (Unbreaking 1, Efficiency 1)\n• 14 Oak Logs", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='knight')
    async def knight_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Knight Kit Information", description=f"• Enchanted Gold Chestplate (Unbreaking 1, Fire Protection 3)\n• Enchanted Gold Helmet (Unbreaking 1, Fire Protection 3)\n• 1 Speed Potion (3 Minutes)", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='healer')
    async def healer_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Healer Kit Information", description=f"• Stone Sword\n• 2 Instant Health Potions", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='meatlover')
    async def meat_lover_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Meat Lover Kit Information", description=f"• 10 Steak/Cooked Beef\n• 6 Cooked Porkchhops\n• Gold Boots", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='sniper')
    async def sniper_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Sniper Kit Information", description=f"• Enchanted Bow (Unbreaking 1, Power 2)\n• 24 Arrows\n• Gold Helmet", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='tank')
    async def tank_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Tank Kit Information", description=f"• Iron Chestplate\n• Enchanted Wooden Axe (Sharpness 2, Unbreaking 1)", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='energix')
    async def energix_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Energix Kit Information", description=f"• Iron Chestplate\n• Enchanted Wooden Axe (Sharpness 2, Unbreaking 1)", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='rookie')
    async def rookie_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Rookie Kit Information", description=f"• Full Leather Armor\n• 16 Oak Planks\n • 4 Steak/Cooked Beef", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='baseballplayer')
    async def baseball_player_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Baseball Player Kit Information", description=f"• Enchanted Wooden Sword (Knockback 2, Sharpness 1, Unbreaking 1)\n• Iron Helmet", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @kinfo.command(name='pyro')
    async def pyro_kinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Pyro Kit Information", description=f"• 1 Fire Resistance Potion (8 Minutes)\n• Flint and Steel", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)
        
def setup(client):
    client.add_cog(kits(client))