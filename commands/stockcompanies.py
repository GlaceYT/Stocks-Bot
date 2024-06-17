# stockcompanies.py
import discord
from discord.ext import commands

class StockCompanies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockcompanies', help='List popular stock companies and their ticker symbols')
    async def stockcompanies(self, ctx):
        companies = {
            "Apple Inc.": "AAPL",
            "Google (Alphabet Inc.)": "GOOGL",
            "Microsoft Corporation": "MSFT",
            "Amazon.com, Inc.": "AMZN",
            "Facebook (Meta Platforms Inc.)": "FB",
            "Tesla, Inc.": "TSLA",
            "NVIDIA Corporation": "NVDA",
            "JPMorgan Chase & Co.": "JPM",
            "Visa Inc.": "V",
            "Johnson & Johnson": "JNJ"
        }
        embed = discord.Embed(title="Popular Stock Companies", description="", color=0x00FF00)
        for company, ticker in companies.items():
            embed.add_field(name=company, value=ticker, inline=False)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockCompanies(bot))