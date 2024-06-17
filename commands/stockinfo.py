# stockinfo.py
import discord
from discord.ext import commands
import yfinance as yf

class StockInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockinfo', help='Get information about a given ticker symbol')
    async def stockinfo(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            info = ticker_data.info
            
            embed = discord.Embed(title=f"Information for {ticker}", description="", color=0x00FF00)
            embed.set_author(name="Information", icon_url="https://cdn.discordapp.com/attachments/1252159749525471275/1252200464725049374/6335-settings-info.png?ex=66715a0f&is=6670088f&hm=637830902261fe362f0577141373ed62146c68efd99355e86f8b358a140312b1&")
            embed.add_field(name="Company Name", value=info.get('shortName', 'N/A'), inline=False)
            embed.add_field(name="Industry", value=info.get('industry', 'N/A'), inline=False)
            embed.add_field(name="Sector", value=info.get('sector', 'N/A'), inline=False)
            embed.add_field(name="Website", value=info.get('website', 'N/A'), inline=False)
            embed.add_field(name="Market Cap", value=info.get('marketCap', 'N/A'), inline=False)
            
            logo_url = info.get('logo_url')
            if logo_url:
                embed.set_thumbnail(url=logo_url)
            else:
                embed.set_thumbnail(url="https://example.com/default_logo.png")  # Replace with a default logo URL or empty string
            
            await ctx.reply(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

    @stockinfo.error
    async def stockinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            embed.set_author(name="Author Name")
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockInfo(bot))
