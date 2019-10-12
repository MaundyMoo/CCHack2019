from discord.ext import commands
from datetime import  datetime
import webparser, discord

class binCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message):
        await ctx.send(message)

    @commands.command()
    async def bindicate(self, ctx, *, address = ""):
        print("Address: ", address)
        data = webparser.parse_address(address)
        embed = discord.Embed(title=("Bin Days for " + datetime.now().strftime("%B %Y")) + " in " + address)
        for i in range(0, len(data)):
            embed.add_field(name=data[i][0] + " " + data[i][1], value=data[i][2])
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(binCog(bot))
