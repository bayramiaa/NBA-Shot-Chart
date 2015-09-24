import requests
import pandas as pd
import matplotlib.pyplot as plt
import urllib

class get_shots:
	def __init__(self,ID):
		self.id = ID

	def get_df(self):
		"""
		returns a DataFrame of players stats from the past season 
		"""
		url = 'http://stats.nba.com/stats/shotchartdetail?Period=0&Vs'\
		    'Conference=&LeagueID=00&LastNGames=0&TeamID=0&Position'\
		    '=&Location=&Outcome=&ContextMeasure=FGA&DateFrom=&Star'\
		    'tPeriod=&DateTo=&OpponentTeamID=0&ContextFilter=&Range'\
		    'Type=&Season=2014-15&AheadBehind=&PlayerID=%s&EndR'\
		    'ange=&VsDivision=&PointDiff=&RookieYear=&GameSegment=&'\
		    'Month=0&ClutchTime=&StartRange=&EndPeriod=&SeasonType='\
		    'Regular+Season&SeasonSegment=&GameID=' %self.id
		response = requests.get(url)
		headers = response.json()['resultSets'][0]['headers']
		shots = response.json()['resultSets'][0]['rowSet']
		return  pd.DataFrame(shots,columns = headers)



