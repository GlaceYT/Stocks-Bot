# stockprice.py
import discord
from discord.ext import commands
import yfinance as yf

class StockPrice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockprice', help='Get the current stock price of a given ticker symbol')
    async def stockprice(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            info = ticker_data.info
            if 'egularMarketPrice' in info:
                price = info['regularMarketPrice']
            elif 'currentPrice' in info:
                price = info['currentPrice']
            else:
                embed = discord.Embed(title=f"Error: Unable to retrieve current stock price for {ticker}", description="", color=0xFF0000)
                embed.set_author(name="Author Name", icon_url="Author Icon URL")
                await ctx.reply(embed=embed)
                return
            embed = discord.Embed(title=f"Price for {ticker}", description=f"The current stock price of {ticker} is **${price:.2f}**", color=0x00FF00)
            embed.set_author(name="Price Data", icon_url="https://cdn.discordapp.com/attachments/1252159749525471275/1252200237934706788/51662-matrix.gif?ex=667159d9&is=66700859&hm=44cd79252d52edc57a7dea71e7a0e5eb65b010fa1e0a18dc69f00654b44c0aab&")
            await ctx.reply(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            embed.set_author(name="Author Name", icon_url="Author Icon URL")
            await ctx.reply(embed=embed)

    @stockprice.error
    async def stockprice_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            embed.set_author(name="Author Name", icon_url="Author Icon URL")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            embed.set_author(name="Author Name", icon_url="Author Icon URL")
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockPrice(bot))