from discord.ext import commands
from datetime import datetime
import webparser, discord, colourparser

class binCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.send(message)

    @commands.command()
    async def bindicate(self, ctx, *, address = ""):
        print("Address: ", address)
        data = webparser.parse_data(webparser.parse_address(address))
        if data != None:
            embed = discord.Embed(title=("Bin Days for " + datetime.now().strftime("%B %Y")) + " in " + address, color=discord.Colour(int(colourparser.parse_colour(data[0][2]), 16)))
            for i in range(0, len(data)):
                embed.add_field(name=data[i][0] + " " + data[i][1], value=data[i][2], inline=False)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send("No results found for address: " + address)


def setup(bot):
    bot.add_cog(binCog(bot))
