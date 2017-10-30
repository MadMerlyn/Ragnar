import discord
import json
import mysql.connector
from discord.ext import commands as viking

with open('config/database.json') as config:
    database = json.load(config)


class MySQL:
    def __init__(self, viking):
        self.viking = viking

    def connect(self):
        self.connection = mysql.connector.connect(**database)
        self.cursor = self.connection.cursor(buffered=True)

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def query_users(self):
        self.cursor.execute("SELECT discord_id FROM users")
        self.existing_users = ', '.join(
            [str(users[0]) for users in self.cursor])

    @viking.command()
    async def get(self, ctx, *, member: discord.Member):
        """*get <member>

        A command that will return a Discord member's MySQL database entries.
        """

        self.connect()
        self.query_users()

        if member in ctx.guild.members:
            if str(member.id) in self.existing_users:
                user_id = self.cursor.execute(
                    "SELECT id FROM users WHERE discord_id=%s", (member.id,))
                user_id = ', '.join([str(row[0]) for row in self.cursor])
                entries = self.cursor.execute(
                    "SELECT body FROM entries WHERE user_id=%s", (user_id,))
                entries = ', '.join([str(row[0]) for row in self.cursor])

                await ctx.send('**{}\'s Entries**: {}'.format(member.name, entries))

            if str(member.id) not in self.existing_users:
                await ctx.send('{} is not a member of the database or has not stored an entry.'.format(member.name))

        self.disconnect()

    @viking.command()
    async def register(self, ctx):
        """*register

        A command that will register the author of the message in the MySQL database.
        """

        self.connect()
        self.query_users()
        discord_id = str(ctx.message.author.id)

        if discord_id in self.existing_users:
            await ctx.send('You are already a registered member in the Viking database.')
        else:
            self.cursor.execute(
                "INSERT INTO users (discord_id) VALUES (%s)", (discord_id,))
            self.connection.commit()
            await ctx.send('You are now registered in the Viking database.')

        self.disconnect()

    @viking.command()
    async def save(self, ctx, *, entry):
        """*save <entry>

        A command that will save an entry to the MySQL database.
        """

        self.connect()
        self.query_users()
        discord_id = str(ctx.message.author.id)

        if discord_id in self.existing_users:
            user_id = self.cursor.execute(
                "SELECT id FROM users WHERE discord_id=%s", (discord_id,))
            user_id = ', '.join([str(row[0]) for row in self.cursor])

            self.cursor.execute(
                "INSERT INTO entries (user_id, body) VALUES (%s, %s)", (user_id, entry,))
            self.connection.commit()
            await ctx.send('You have successfully saved this entry in the Viking database.')
        else:
            await ctx.send('Please use ***register** to register an account before using this command.')

        self.disconnect()

    @viking.command()
    async def users(self, ctx):
        """*users

        A command that will return all registered Discord members in the MySQL database.
        """

        self.connect()
        self.query_users()

        users = ', '.join(sorted([member.name for member in ctx.guild.members if str(
            member.id) in self.existing_users]))
        await ctx.send('**Viking Database:** {}'.format(users))

        self.disconnect()


def setup(viking):
    viking.add_cog(MySQL(viking))
