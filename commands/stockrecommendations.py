import discord
from discord.ext import commands
import yfinance as yf
from datetime import datetime

class StockRecommendations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stockrecommend', help='Get stock recommendations for a given ticker symbol')
    async def stock_recommendations(self, ctx, ticker: str):
        try:
            ticker_data = yf.Ticker(ticker)
            recommendations = ticker_data.recommendations
            
            if recommendations.empty:
                await ctx.reply(f'No recommendations found for {ticker}')
                return
            
            # Get the latest recommendation
            latest_recommendation = recommendations.iloc[-1]
            
            # Convert recommendation date to datetime if it's not already
            recommendation_date = latest_recommendation.name
            if isinstance(recommendation_date, int):
                recommendation_date = datetime.utcfromtimestamp(recommendation_date).strftime('%Y-%m-%d')
            else:
                recommendation_date = recommendation_date.strftime('%Y-%m-%d')
            
            # Construct embed with recommendation information
            embed = discord.Embed(title=f"Recommendations for {ticker}", color=0x0088FF)
            embed.add_field(name="Date", value=recommendation_date, inline=False)
            embed.add_field(name="Action", value=latest_recommendation.get('To Grade', 'Not Available'), inline=False)
            embed.add_field(name="From", value=latest_recommendation.get('From Grade', 'Not Available'), inline=False)
            embed.add_field(name="Firm", value=latest_recommendation.get('Firm', 'Not Available'), inline=False)
            
            await ctx.reply(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error: {e}", color=0xFF0000)
            await ctx.reply(embed=embed)

    @stock_recommendations.error
    async def stock_recommendations_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description="Please provide a ticker symbol!", color=0xFF0000)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Error", description=f"Error: {error}", color=0xFF0000)
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(StockRecommendations(bot))
