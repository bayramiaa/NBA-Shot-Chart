import requests
import urllib
import matplotlib.pyplot as plt


def get_playerID():
	"""
	Loads player nbas ID's for each player
	"""

	print "Loading player IDs from 2014-2015 NBA Season..."
	teamIDs = []

	Teamlist = 'http://stats.nba.com/stats/scoreboard?DayOffset=0&LeagueID=00&gameDate=07%2F31%2F2015'
	response1 = requests.get(Teamlist)
	for i in response1.json()['resultSets'][4]['rowSet']:
		teamIDs.append(str(i[0]))
	for j in response1.json()['resultSets'][5]['rowSet']:
		teamIDs.append(str(j[0]))


	player_info = {}

	for teamID in teamIDs:
		url =  'http://stats.nba.com/stats/teamplayerdashboard?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=' + teamID + '&VsConference=&VsDivision='
		response2 = requests.get(url)
		info = response2.json()['resultSets'][1]['rowSet']
		for i in info:
			player_info[i[2].lower()] = i[1]

	return player_info


def get_img(ID):
	"""
	uses players IDs to retrieve images from the nba
	"""
	pic= urllib.urlretrieve("http://stats.nba.com/media/players/230x185/%s.png" %ID,"%s.png" %ID)
	player_pic = plt.imread(pic[0])
	return player_pic