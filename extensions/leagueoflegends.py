import aiohttp
import json
from discord.ext import commands as viking
from collections import Counter

with open('config/config.json') as cfg:
	config = json.load(cfg)

lol_api_key = config['lol_api_key']


class LeagueOfLegends:
	def __init__(self, viking):
		self.viking = viking

	@viking.command()
	async def live(self, ctx, *, summoner):
		"""*live <username>
		A command that will give an overview of everyone in your current game
		including: everyone's name, level, champion, rank and win/loss ratio"""

		params = {
			'api_key': lol_api_key,
		}

		async with aiohttp.ClientSession() as session:
			async with session.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summoner, params=params) as response:
				data = await response.json()
				summoner_id = str(data['id'])	

			async with session.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + summoner_id, params=params) as response:
				if response.status == 200:
					data = await response.json()
					await ctx.send(str.title('**Game Mode:** {}'.format(data['gameMode'])))

					for x in data['participants']:
						summoner_id = str(x['summonerId'])
						champion_id = str(x['championId'])
						summoner_name = str(x['summonerName'])
						
						async with session.get('http://ddragon.leagueoflegends.com/cdn/7.21.1/data/en_US/champion.json') as response:
							data = await response.json()

							for champion in data['data'].values():
								if champion_id == champion['key']:
									champion_name = '({}): '.format(champion['name'])

						async with session.get('https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/' + summoner_id, params=params) as response:
							data = await response.json()

							solo_ranked_players_list = []

							for i in data:					
								if 'RANKED_SOLO_5x5' in i['queueType']:
									solo_ranked_players = i['playerOrTeamName']
									solo_ranked_players_list.append(solo_ranked_players)
									tier = '{}'.format(i['tier'])
									rank = ' {}'.format(i['rank'])
									wins = int(i['wins'])
									losses = int(i['losses'])
									total_games = wins + losses
									win_loss_ratio = '[{:0.2f}%]'.format(
										wins / total_games * 100)
									league_points = ' [{} LP] '.format(i['leaguePoints'])
									player_name = '**{}** '.format(i['playerOrTeamName'])
									await ctx.send(player_name + champion_name + str.title(tier) + rank + league_points + win_loss_ratio)

							if summoner_name not in solo_ranked_players_list or not data:
								remaining_players = str(x['summonerName'])
								async with session.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + remaining_players, params=params) as response:
									data = await response.json()
								unranked_players = '**{}** '.format(x['summonerName'])
								summoner_level = 'Level {}'.format(data['summonerLevel'])
								tier = ' [{}]'.format('Unranked')
								await ctx.send(unranked_players + champion_name + summoner_level + tier)
				else:
					await ctx.send('**Error:** It appears this summoner is not in a game.')


def setup(viking):
	viking.add_cog(LeagueOfLegends(viking))
