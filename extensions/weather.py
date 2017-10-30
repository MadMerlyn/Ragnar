import pyowm
import json
from discord.ext import commands as viking
from functools import partial

with open('config/config.json') as cfg:
    config = json.load(cfg)

owm_api_key = config['owm_api_key']


class Weather:
    def __init__(self, viking):
        self.viking = viking

    @viking.command()
    async def forecast(self, ctx, *, name):
        """*forecast <location>

        A command that will return the forecast of a specified location.
        """

        owm = pyowm.OWM(owm_api_key)

        observation = await self.viking.loop.run_in_executor(None, partial(owm.weather_at_place, name))
        weather = await self.viking.loop.run_in_executor(None, partial(observation.get_weather))
        location = await self.viking.loop.run_in_executor(None, partial(observation.get_location))
        get_temperature = await self.viking.loop.run_in_executor(None, partial(weather.get_temperature, unit='celsius'))
        get_wind = await self.viking.loop.run_in_executor(None, partial(weather.get_wind))

        await ctx.send('**Location:** {}'.format(location.get_name()))
        await ctx.send('**Temperature:** {}'.format(get_temperature['temp']) + u'\N{DEGREE SIGN}C')
        await ctx.send('**Humidity:** {}'.format(weather.get_humidity()) + '%')
        await ctx.send('**Wind Speed:** {}'.format(get_wind['speed']) + ' m/s')
        await ctx.send('**Description:** {}'.format(weather.get_detailed_status()))


def setup(viking):
    viking.add_cog(Weather(viking))
