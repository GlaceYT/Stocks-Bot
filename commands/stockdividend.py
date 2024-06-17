# stockdividend.py
import discord
from discord.ext import commands
import yfinance as yf
import pandas as pd

class StockDividend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockdividend', help='Get dividend information for a given ticker symbol')
    async def stock_dividend(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            dividends = ticker_data.dividends

            if dividends.empty:
                await ctx.reply(f'No dividend data found for {ticker}')
                return

            latest_dividend_date = dividends.index[0].strftime('%Y-%m-%d')
            latest_dividend_amount = dividends.iloc[0]
            
            embed = discord.Embed(title=f"Dividend Information for {ticker}", color=0x0088FF)
            embed.add_field(name="Recent Dividend Date", value=latest_dividend_date)
            embed.add_field(name="Amount", value=f"${latest_dividend_amount:.2f}", inline=False)
            
            await ctx.reply(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            await ctx.reply(embed=embed)

    @stock_dividend.error
    async def stock_dividend_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            await ctx.reply(embed=embed)
async def setup(bot):
    await bot.add_cog(StockDividend(bot))
