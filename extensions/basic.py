import aiohttp
import random
from discord.ext import commands as viking
from bs4 import BeautifulSoup


class Basic:
    def __init__(self, viking):
        self.viking = viking

    @viking.command()
    async def coinflip(self, ctx):
        """*coinflip

        A command that will flip a coin, and choose "Heads" or "Tails".
        """

        choices = ('Heads!', 'Tails!')
        await ctx.send(random.choice(choices))

    @viking.command()
    async def echo(self, ctx, *, message):
        """*echo <message>

        A command that will use to text-to-speech to repeat the author's message.
        """

        await ctx.send(message, tts=True)

    @viking.command()
    async def eightball(self, ctx, *, question):
        """*eightball <question>

        A command that will answer the author's question.
        """

        choices = (
            'Absolutely!',
            'Without a doubt.',
            'Most likely.',
            'Yes.',
            'Maybe.',
            'Perhaps.',
            'Nope.',
            'Very doubtful.',
            'Absolutely not.',
            'It is unlikely.'
        )
        await ctx.send(random.choice(choices))

    @viking.command()
    async def facts(self, ctx):
        """*facts

        A command that will provide the author with a random fact.
        """

        async with aiohttp.ClientSession() as session:
            async with session.get('http://www.unkno.com/') as response:
                soup = BeautifulSoup(await response.text(), "html.parser")
                facts = soup.find('div', attrs={'id': 'content'})

                for fact in facts:
                    fact = fact.strip()
                    await ctx.send(fact)

    @viking.command()
    async def hello(self, ctx):
        """*hello

        A command that will respond with a random greeting.
        """

        choices = ('Hey!', 'Hello!', 'Hi!', 'Hallo!', 'Bonjour!', 'Hola!')
        await ctx.send(random.choice(choices))

    @viking.command()
    async def quotes(self, ctx):
        """*quotes

        A command that will return a random quotation.
        """

        params = {'method': 'getQuote', 'lang': 'en', 'format': 'json'}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.forismatic.com/api/1.0/', params=params) as response:
                quotes = await response.json()
                await ctx.send('{} - {}'.format(quotes['quoteText'], quotes['quoteAuthor']))

    @viking.command()
    async def repeat(self, ctx, amount: int, *, message):
        """*repeat <amount> <message>

        A command that will repeat a message a specified amount of times.
        """

        if amount > 5:
            await ctx.send('Please use a number less than or equal to five.')
        else:
            for i in range(amount):
                await ctx.send(message)

    @viking.command()
    async def reverse(self, ctx, *, message):
        """*reverse <message>

        A command that will reverse the words in an author's message.
        """

        sentence = message.split()
        await ctx.send(' '.join(reversed(sentence)))


def setup(viking):
    viking.add_cog(Basic(viking))
