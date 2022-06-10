import nextcord, json
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from pymongo import MongoClient

class database(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    with open("./config.json") as file:
        config = json.load(file)
        
    cluster = MongoClient(config['mongo-db-url'])
    
    global uhc_collection
    uhc_collection = cluster["uhc"]["database"]
    
    @has_permissions(administrator=True)
    @commands.command()
    async def adduser(self, ctx, user: nextcord.Member = None):
        if user is None:
            await ctx.reply("Please mention a user to add to the database! ❌")
            return

        user_id = user.id
        
        check = uhc_collection.find_one({"id": user_id})
        
        if check is None:
            insert = {"id": user_id, "name": user.name, "wins": 0, "kills": 0, "games_played": 0}
            
            uhc_collection.insert_one(insert)
            
            await ctx.reply(f"{user.mention} has been added to the database! ✅")
            return
        else:
            await ctx.reply(f"{user.mention} already exists in the database! ❌")
            return

    @has_permissions(administrator=True)
    @commands.command()
    async def removeuser(self, ctx, user: nextcord.Member = None):
        if user is None:
            await ctx.reply("Please mention a user to remove from the database! ❌")
            return

        user_id = user.id
        
        check = uhc_collection.find_one({"id": user_id})
        
        if check is None:
            await ctx.reply(f"{user.mention} does not exist in the database! ❌")
            return
        else:
            uhc_collection.delete_one({"id": user_id})

            await ctx.reply(f"{user.mention} has been removed from the database! ✅")
            return

    @has_permissions(administrator=True)
    @commands.command()
    async def updateuser(self, ctx, user: nextcord.Member = None):
        if user is None:
            await ctx.reply("Please mention a user to remove from the database! ❌")
            return

        user_id = user.id
        
        check = uhc_collection.find_one({"id": user_id})
        
        if check is None:
            await ctx.reply(f"{user.mention} does not exist in the database! ❌")
            return
        else:
            uhc_collection.delete_one({"id": user_id})

            await ctx.reply(f"{user.mention} has been updated to the database! ✅")
            return
            
    @has_permissions(administrator=True)
    @commands.command()
    async def setwins(self, ctx, user: nextcord.Member = None, *, wins: int = None):
        if user is None:
            await ctx.reply("Please mention a user, so I can find that user in the database! ❌")
            return

        user_id = user.id

        check = uhc_collection.find_one({"id": user_id})

        if check is None:
            await ctx.reply("This user doesn't not exist in the database! ❌\nPlease use `.hadduser` command to add that user!")
            return
        
        if wins is None:
            await ctx.reply("Please set an amount for how many wins this user should have! ❌")
            return

        else:
            uhc_collection.update_one({"id": user_id}, {"$set":{"wins": wins}})

            await ctx.reply(f"Updated {user.mention} wins to {wins}. ✅")
            return

    @has_permissions(administrator=True)
    @commands.command()
    async def setkills(self, ctx, user: nextcord.Member = None, *, kills: int = None):
        if user is None:
            await ctx.reply("Please mention a user, so I can find that user in the database! ❌")
            return

        user_id = user.id

        check = uhc_collection.find_one({"id": user_id})

        if check is None:
            await ctx.reply("This user doesn't not exist in the database! ❌\nPlease use `.hadduser` command to add that user!")
            return
        
        if kills is None:
            await ctx.reply("Please set an amount for how many kills this user should have! ❌")
            return

        else:
            uhc_collection.update_one({"id": user_id}, {"$set":{"kills": kills}})

            await ctx.reply(f"Updated {user.mention} kills to {kills}. ✅")
            return

    @has_permissions(administrator=True)
    @commands.command()
    async def setgamesplayed(self, ctx, user: nextcord.Member = None, *, games_played: int = None):
        if user is None:
            await ctx.reply("Please mention a user, so I can find that user in the database! ❌")
            return

        user_id = user.id

        check = uhc_collection.find_one({"id": user_id})

        if check is None:
            await ctx.reply("This user doesn't not exist in the database! ❌\nPlease use `.hadduser` command to add that user!")
            return
        
        if games_played is None:
            await ctx.reply("Please set an amount for how many games played this user should have! ❌")
            return

        else:
            uhc_collection.update_one({"id": user_id}, {"$set":{"games_played": games_played}})

            await ctx.reply(f"Updated {user.mention} games played to {games_played}. ✅")
            return

    @commands.command(aliases=['top', 'lb'])
    async def leaderboard(self, ctx, num_of_players: int = 5):
        if num_of_players > 20:
            await ctx.reply("In order to make the message not too long, you can only see the top 20 people in the server. ❌")
            return

        rankings = uhc_collection.find().sort("wins", -1)
        i = 1
        embed = nextcord.Embed(title="OGUHC Leaderboard", description=f"Displays the best players (top {num_of_players}) in OGUHC, by most wins.", color=0xf54242)
        embed.set_footer(text="HalfAHeart | OGUHC.joinjava.net")
        for x in rankings:
            try:
                temp = ctx.guild.get_member(x["id"])
                temp_wins = x["wins"]
                temp_kills = x["kills"]
                temp_games_played = x["games_played"]

                if i == 1:
                    i = "🥇"
                    embed.add_field(name=f"{i}: {temp.name}", value=f"👑 **Wins:** {temp_wins} | 🗡 **Kills:** {temp_kills} | 🗓️ **Games Played:** {temp_games_played}", inline=False)
                    i = 2
                elif i == 2:
                    i = "🥈"
                    embed.add_field(name=f"{i}: {temp.name}", value=f"👑 **Wins:** {temp_wins} | 🗡 **Kills:** {temp_kills} | 🗓️ **Games Played:** {temp_games_played}", inline=False)
                    i = 3
                elif i == 3: 
                    i = "🥉"
                    embed.add_field(name=f"{i}: {temp.name}", value=f"👑 **Wins:** {temp_wins} | 🗡 **Kills:** {temp_kills} | 🗓️ **Games Played:** {temp_games_played}", inline=False)
                    i = 4
                else:
                    if i == 4:
                        i = 4
                        embed.add_field(name=f"{i}: {temp.name}", value=f"👑 **Wins:** {temp_wins} | 🗡 **Kills:** {temp_kills} | 🗓️ **Games Played:** {temp_games_played}", inline=False)
                        i += 1
                    else:
                        embed.add_field(name=f"{i}: {temp.name}", value=f"👑 **Wins:** {temp_wins} | 🗡 **Kills:** {temp_kills} | 🗓️ **Games Played:** {temp_games_played}", inline=False)
                        i += 1
            except:
                pass
            if i == num_of_players + 1:
                break
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(database(client))