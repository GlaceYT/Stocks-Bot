# stocknews.py
import discord
from discord.ext import commands
import yfinance as yf

class StockNews(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stocknews', help='Get the latest news for a given ticker symbol')
    async def stocknews(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            news = ticker_data.news
            embed = discord.Embed(title=f"Latest News for {ticker}", description="", color=0x00FF00)
            embed.set_author(name="News", icon_url="https://cdn.discordapp.com/attachments/1230824451990622299/1236625364764065822/playlist.gif?ex=6670b85e&is=666f66de&hm=b991be45f823a8bc6ebabe9a4ba49fd61fd15a6f674c45003fee360012ed65a8&")
            for article in news:
                embed.add_field(name=article['title'], value=article['publisher'], inline=False)
            await ctx.reply(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

    @stocknews.error
    async def stocknews_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockNews(bot))