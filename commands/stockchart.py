# stockchart.py

import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt

class StockChart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockchart', help='Get a chart of the stock price for a given ticker symbol')
    async def stockchart(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            hist = ticker_data.history(period="1y")
            plt.plot(hist.index, hist['Close'])
            plt.title(f"Stock Price Chart for {ticker}")
            plt.xlabel("Date")
            plt.ylabel("Price ($)")
            plt.savefig("stock_chart.png")
            file = discord.File("stock_chart.png", filename="stock_chart.png")
            embed = discord.Embed(title=f"Stock Price Chart for {ticker}", description="", color=0x00FF00)
            embed.set_author(name="Chart", icon_url="https://cdn.discordapp.com/attachments/1252205992943288331/1252214544198140035/14504-chart-increasing.gif?ex=6671672c&is=667015ac&hm=43f236c29a335ab80c2bafebfe8d75557208a93e5b1792ebcc54d1013ae27894&")
            embed.set_image(url="attachment://stock_chart.png")
            await ctx.reply(file=file, embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

    @stockchart.error
    async def stockchart_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockChart(bot))  # Await the addition of cog properly

