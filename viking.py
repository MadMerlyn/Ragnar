import json
from discord.ext import commands

with open('config/config.json') as cfg:
    config = json.load(cfg)

prefix = config['command_prefix']
token = config['token']

extensions = (
    'extensions.basic',
    'extensions.discord',
    'extensions.games',
    'extensions.giphy',
    'extensions.leagueoflegends',
    'extensions.mongodb',
    'extensions.mysql',
    'extensions.weather'
)

viking = commands.Bot(prefix)


def main():
    @viking.event
    async def on_ready():
        """A function that is called when the client is
        done preparing data received from Discord.
        """

        print('Username: {}'.format(viking.user.name))
        print('User ID: {}'.format(viking.user.id))

    for extension in extensions:
        try:
            viking.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    viking.run(token)


if __name__ == '__main__':
    main()
