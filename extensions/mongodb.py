import discord
from discord.ext import commands as viking
from pymongo import MongoClient


class MongoDB:
    def __init__(self, viking):
        self.viking = viking

    def connect(self):
        self.client = MongoClient()
        self.database = self.client['viking']

    @viking.command()
    async def monget(self, ctx, *, member: discord.Member):
        """*monget <member>

        A command that will return a specified Discord member's Mongo database entries.
        """

        self.connect()

        if member in ctx.guild.members:
            cursor = self.database.entries.find({"discord_id": str(member.id)})
            entries = [user_id['entry'] for user_id in cursor if str(
                member.id) == user_id['discord_id']]

            if not entries:
                await ctx.send('{} does not have any entries in the database.'.format(member.name))
            else:
                await ctx.send(', '.join(entries))

    @viking.command()
    async def monquery(self, ctx, *, query):
        """*monquery <query>

        A command that will return Mongo database entries that match the search query.
        """

        self.connect()
        cursor = self.database.entries.find({"entry": {"$regex": query}})
        count = 0

        await ctx.send('Results for "**{}:**"'.format(query))

        for entry in cursor:
            count += 1
            await ctx.send('{}) {}'.format(count, entry['entry']))

    @viking.command()
    async def monsave(self, ctx, *, entry):
        """*monsave <entry>

        A command that will save an entry to the Mongo database.
        """

        self.connect()
        discord_id = str(ctx.message.author.id)

        self.database.entries.insert_one({
            "discord_id": discord_id,
            "entry": entry
        })

        await ctx.send('You have successfully saved this entry in the Viking database.')


def setup(viking):
    viking.add_cog(MongoDB(viking))
