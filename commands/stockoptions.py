import discord
from discord.ext import commands
import yfinance as yf

class StockOptions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockoptions', help='Get options chain data for a given ticker symbol')
    async def stock_options(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            options = ticker_data.options
            
            if not options:
                await ctx.reply(f'No options chain data found for {ticker}')
                return
            
            options_str = "\n".join(options[:10])  # Displaying first 10 options
            
            embed = discord.Embed(title=f"Options Chain for {ticker}", description=options_str, color=0x0088FF)
            await ctx.reply(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            await ctx.reply(embed=embed)

    @stock_options.error
    async def stock_options_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockOptions(bot))
