import aiohttp
import json
import random
from discord.ext import commands as viking

with open('config/config.json') as cfg:
    config = json.load(cfg)

giphy_api_key = config['giphy_api_key']


class Giphy:
    def __init__(self, viking):
        self.viking = viking

    @viking.command()
    async def gif(self, ctx):
        """*gif

        A command that will return a random .gif.
        """

        params = {
            'api_key': giphy_api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.giphy.com/v1/gifs/random', params=params) as response:
                data = await response.json()
                await ctx.send(data['data']['image_original_url'])

    @viking.command()
    async def search(self, ctx, *, query):
        """*search <query>

        A command that will return a random .gif that matches the search query.
        """

        params = {
            'api_key': giphy_api_key,
            'q': query,
            'limit': '100',
            'offset': '0',
            'rating': 'R',
            'lang': 'en'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.giphy.com/v1/gifs/search', params=params) as response:
                data = await response.json()
                values = [v for results in data['data']
                          for k, v in results.items() if k == 'url']

                url = random.choice(values)
                await ctx.send(url)

    @viking.command()
    async def trending(self, ctx):
        """*trending

        A command that will return a random .gif from the trending page of Giphy.
        """

        params = {
            'api_key': giphy_api_key,
            'limit': '100',
            'rating': 'R',
        }

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.giphy.com/v1/gifs/trending', params=params) as response:
                data = await response.json()
                values = [v for results in data['data']
                          for k, v in results.items() if k == 'url']
                url = random.choice(values)
                await ctx.send(url)


def setup(viking):
    viking.add_cog(Giphy(viking))
