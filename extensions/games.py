import random
from discord.ext import commands as viking
from random import randint


class Games:
    def __init__(self, viking):
        self.viking = viking

    @viking.command()
    async def guess(self, ctx):
        """*guess

        A command that will play the Guessing Game with the author of the message.
        """

        async def play():
            try:
                await ctx.send('Lets play a game! You have to guess a number between 1 and 10.')
                guess = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
                answer = random.randint(1, 10)
                counter = 1

                while int(guess.content) != answer:
                    counter += 1
                    if int(guess.content) > answer:
                        await ctx.send('Your guess is too high! Try again.')
                        guess = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
                    else:
                        await ctx.send('Your guess is too low! Try again.')
                        guess = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
                else:
                    if counter <= 1:
                        await ctx.send('Congratulations! You got it on your first attempt!')
                    else:
                        await ctx.send('Congratulations! It took you **{}** tries to guess the correct answer.'.format(counter))
                    await gameover()
            except ValueError:
                await ctx.send('Please enter a number.')
                await play()

        async def gameover():
            await ctx.send('Do you want to play again? (Enter: **Yes** / **No**)')
            response = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
            response = response.content.lower()

            if response == 'yes':
                await play()
            elif response == 'no':
                await ctx.send('Thanks for playing!')
            else:
                await ctx.send('Invalid response.')
                await gameover()

        await play()

    @viking.command()
    async def rps(self, ctx):
        """*rps

        A command that will play Rock, Paper, Scissors with the author of the message.
        """

        async def play():
            await ctx.send('Lets play **Rock, Paper, Scissors**. Choose your weapon:')
            choices = ('rock', 'paper', 'scissors')
            computer = choices[randint(0, 2)]
            player = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
            player = player.content.lower()

            beats = {
                'rock': ['paper'],
                'paper': ['scissors'],
                'scissors': ['rock']
            }

            if computer and player in choices:
                if computer == player:
                    await ctx.send('**Tie!** You both chose **{}**.'.format(computer.title()))
                    await gameover()
                elif player in beats[computer]:
                    await ctx.send('**You win!** Viking chose: **{}** and you chose: **{}**.'.format(computer.title(), player.title()))
                    await gameover()
                else:
                    await ctx.send('**You lose!** Viking chose: **{}** and you chose: **{}**.'.format(computer.title(), player.title()))
                    await gameover()
            else:
                await ctx.send('Please choose a weapon.')
                await play()

        async def gameover():
            await ctx.send('Do you want to play again? (Enter: **Yes** / **No**)')
            response = await self.viking.wait_for('message', check=lambda message: message.author == ctx.author)
            response = response.content.lower()

            if response == 'yes':
                await play()
            elif response == 'no':
                await ctx.send('Thanks for playing!')
            else:
                await ctx.send('Invalid option!')
                await gameover()

        await play()


def setup(viking):
    viking.add_cog(Games(viking))
