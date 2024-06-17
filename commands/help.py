# commands/help.py
from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shelp')
    async def help_command(self, ctx):
        embed = discord.Embed(
            description="Welcome to Stocks Bot! This bot provides financial information and market updates.\n\n Use the following commands to interact with the bot:",
            color=discord.Color.blue()
        )
        embed.add_field(name="!stockinfo ", value="- Provides detailed information about the given stock attribute", inline=False)
        embed.add_field(name="!stockchart", value="- Get the stock chart", inline=False)
        embed.add_field(name="!stockprice ", value="- Shows the current stock price of the given attribute", inline=False)
        embed.add_field(name="!stockoptions ", value="- Shows the current stock options", inline=False)
        embed.add_field(name="!stockrecommend ", value="- Shows the current stock recommendations", inline=False)
        embed.add_field(name="!stockdividend ", value="- Get the stock dividend value", inline=False)
        embed.add_field(name="!stocknews", value="- Displays the latest market news", inline=False)
        embed.add_field(name="!stockcompanies", value="- Displays the top companies news", inline=False)

        # Adding a thumbnail image
        embed.set_thumbnail(url="https://example.com/thumbnail.jpg")

        # Adding an image
        embed.set_image(url="https://cdn.discordapp.com/attachments/1252159749525471275/1252180345697079366/STOCKS_1.png?ex=66714752&is=666ff5d2&hm=a91bae5dd2538b4e0eb7b1455ae09202ac556a9852da496055a0f254c7ff7e8e&")

        embed.set_author(name="List of Avaiable Commands", url="https://discord.gg/xQF9f9yUEM", icon_url="https://cdn.discordapp.com/attachments/1230824451990622299/1252165467842416680/1667-yellow-gears.gif?ex=66713977&is=666fe7f7&hm=524061f98a2e86e94b3cc829d7b0a5fbb3c328b79f05456ae5b96095ec57d405&")
        embed.set_footer(text="Stocks Bot By Vivek Chowdary", icon_url="https://cdn.discordapp.com/attachments/1230824451990622299/1236794583732457473/7828-verify-ak.gif?ex=6670ad37&is=666f5bb7&hm=6c77e687ebe1c047fe15a1f4feccf2a352e153033582e5f9e678e567eeb3c483&")
    
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
