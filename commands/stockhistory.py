# Command to fetch historical stock data and display a chart
import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
import io

class StockHistory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockhistory', help='Show historical stock price chart for a given ticker symbol')
    async def stock_history(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            hist = ticker_data.history(period="1y")  # Adjust period as needed
            plt.figure(figsize=(10, 6))
            plt.plot(hist.index, hist['Close'])
            plt.title(f"Stock Price History for {ticker}")
            plt.xlabel("Date")
            plt.ylabel("Price ($)")
            plt.grid(True)
            
            # Save plot to a BytesIO object
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            
            file = discord.File(buf, filename=f"{ticker}_history.png")
            embed = discord.Embed(title=f"Historical Stock Price Chart for {ticker}", description="", color=0x0088FF)
            embed.set_image(url=f"attachment://{ticker}_history.png")
            
            await ctx.reply(file=file, embed=embed)
            
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            await ctx.reply(embed=embed)

    @stock_history.error
    async def stock_history_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockHistory(bot))
