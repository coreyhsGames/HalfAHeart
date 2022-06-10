import nextcord, time
from nextcord.ext import commands

class uhc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def uhcinfo(self, ctx):
        await ctx.reply("Use this command to get information about OGUHC. To get the list of the settings, use `.huhcinfo list`. Also, the command will not work if it is uppercase, it has to be lowercase.")
    
    @uhcinfo.command(name='list')
    async def uhclist(self, ctx):
        kitlist_embed = nextcord.Embed(title="List of OGUHC Information Settings", description=f"Use `.huhcinfo (setting name)` for more information about that setting.", color=0xf54242)
        kitlist_embed.add_field(name="List of OGUHC Settings", value="• Simplified (simple)\n• Grace Period (graceperiod)\n• World Size (worldsize)\n• The Nether (nether)\n• Kits (kits)\n• Game Length (gamelength)\n• Border (border)\n• Apple Drops (apples)\n• Difficulty (difficulty)\n• Version (version)", inline=False)
        kitlist_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitlist_embed)

    @uhcinfo.command(name='simple')
    async def simple_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Simplified OGUHC Information", description=f"Simplified OGUHC settings information.", color=0xf54242)
        kitinfo_embed.add_field(name="Grace Period:", value="**Time:** 15 minutes", inline=True)
        kitinfo_embed.add_field(name="World Size:", value="**World Size:** 750 (+750x, -750x, +750z, -750z)", inline=True)
        kitinfo_embed.add_field(name="The Nether:", value="❌ Disabled", inline=True)
        kitinfo_embed.add_field(name="The End:", value="❌ Disabled", inline=True)
        kitinfo_embed.add_field(name="Kits:", value="**Number of Kits:** 11 Kits", inline=True)
        kitinfo_embed.add_field(name="Game Length:", value="**Game Length:** 45 minutes _(excluding deathmatch)_", inline=True)
        kitinfo_embed.add_field(name="Border:", value="**Time till Shrink:** 20 minutes\n**End Size:** 200 (+200x, -200x, +200z, -200z)\n**Time to Shrink:** 5 minutes", inline=True)
        kitinfo_embed.add_field(name="Apple Drops:", value="**Chance to Drop:** 2% (2x more likely than normal)\n**Type of Leaves:** ✅ All\n**Shears:** ✅ Enabled", inline=True)
        kitinfo_embed.add_field(name="Difficulty:", value="Hard", inline=True)
        kitinfo_embed.add_field(name="Version:", value="**Versions Supported:** 1.9 to 1.18.2", inline=True)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='graceperiod')
    async def grace_period_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Grace Period Information", description=f"Currently the Grace Period before PVP is enabled is 15 minutes at the start of game.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='worldsize')
    async def world_size_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="World Size Information", description=f"Currently the starting World Size is 750, which is +750x, -750x, +750z, -750z to be exact.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='nether')
    async def knight_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="The Nether Information", description=f"Currently The Nether is disabled, but possibly in the future, it could be re-enabled.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='kits')
    async def kits_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Kit Information", description=f"There are currently 11 available in OGUHC, you can use `.hkinfo (kit name)` for information about that kit.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='gamelength')
    async def game_length_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Game Length Information", description=f"Currently the game length is 45 minutes, this is when deathmatch starts, and that doesn't end till one player or team is left.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='border')
    async def border_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Border Information", description=f"The border starts to shrink 20 minutes into the game and shrinks to 200 world size (+200x, -200x, +200z, -200z). The time it takes the border to shrink is 5 minutes.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='apples')
    async def apple_drops_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Apple Drop Information", description=f"Currently apples are x2 more likely to drop, and they drop from any type of leaves. You can also use shears to get apples.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='difficulty')
    async def difficulty_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Difficulty Information", description=f"Because this is UHC (ultra hardcore), the difficulty is set to hard.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)

    @uhcinfo.command(name='version')
    async def version_uhcinfo(self, ctx):
        kitinfo_embed = nextcord.Embed(title="Version Information", description=f"You can play OGUHC on 1.9 to 1.18.2, 1.19 will probably not be supported for awhile.", color=0xf54242)
        kitinfo_embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        await ctx.reply(embed=kitinfo_embed)
        
def setup(client):
    client.add_cog(uhc(client))