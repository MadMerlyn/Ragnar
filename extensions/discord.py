import discord
from discord.ext import commands as viking


class Discord:
    def __init__(self, viking):
        self.viking = viking

    @viking.command()
    @viking.has_any_role('Administrator', 'Moderator')
    async def clear(self, ctx, amount: int):
        """*clear <amount>

        A command that will clear a specified amount of messages from a text channel.
        """

        deleted = await ctx.channel.purge(limit=amount+1)
        await ctx.send('I have cleared {} messages.'.format(len(deleted)-1), delete_after=3.0)

    @viking.command()
    async def joined(self, ctx, *, member: discord.Member):
        """*joined <member>

        A command that will return the date of when a specified Discord member joined the server.
        """

        date = member.joined_at.strftime('%B %d, %Y')
        await ctx.send('{} joined this server on {}.'.format(member.name, date))

    @viking.command()
    async def members(self, ctx):
        """*members

        A command that will return the total number of Discord members in the server.
        """

        await ctx.send('There are {} members in this server.'.format(ctx.guild.member_count))

    @viking.command()
    async def owner(self, ctx):
        """*owner

        A command that will mention the owner of the Discord server.
        """
        
        await ctx.send('{}'.format(ctx.guild.owner.mention))

    @viking.command()
    @viking.has_any_role('Administrator', 'Moderator')
    async def purge(self, ctx):
        """*purge

        A command that will purge all messages from a text channel.
        """

        await ctx.channel.purge()


def setup(viking):
    viking.add_cog(Discord(viking))
