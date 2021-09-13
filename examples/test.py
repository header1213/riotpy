import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from riot import riotpy

riot = riotpy.Riot('my_api_key')

summoner = riot.summoner(summonerName='hide on bush')
puuid = summoner['puuid']
matches = riot.match(puuid=puuid, count=1)
matchid = matches[0]
match = riot.match(matchId=matchid)
print(match)