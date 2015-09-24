

import matplotlib.pyplot as plt
from matplotlib.offsetbox import  OffsetImage
import seaborn as sns

from player_ID import get_playerID, get_img
from shots import get_shots
from court import draw_court


playerIDs = get_playerID()


#### input players name as lowercase string
#### ShotChart('kevin durant').scatterplot()
#### still having problems with jointplot



class ShotChart:
	def __init__(self,player):
		self.player = player 
		self.ID = str(playerIDs[player.lower()])
		self.df = get_shots(str(playerIDs[player])).get_df()

	def scatterplot(self):
		"""
		Returns a scatterplot of a players shots for the 2014-2015 NBA Season
		"""
		plt.figure(figsize=(10,9))
		plt.scatter(self.df.LOC_X,self.df.LOC_Y)
		draw_court(outer_lines=True)
		plt.xlim(-250,250)
		plt.ylim(395,-47.5)
		ax = plt.axes([.8,0.2, 0.1, 0.2], frameon=True)
		ax.axis('off')
		plt.show()

	def jointplot(self):
		"""
		returns joing plot of players shots, players image, and title (Not functioning)
		"""
		joint_shot_chart = sns.jointplot(self.df.LOC_X,self.df.LOC_Y, stat_func=None,kind='scatter',space=0)
		joint_shot_chart.fig.set_size_inches(12,11)
		ax = joint_shot_chart.ax_joint
		draw_court(ax)
		ax.set_xlim(-250,250)
		ax.set_ylim(395, -47.5)
		ax.set_xlabel('')
		ax.set_ylabel('')
		ax.tick_params(labelbottom='off', labelleft='off')
		ax.set_title('%s FGA \n2014-15 Reg. Season' %self.player, 
		              y=1.2, fontsize=18)
		ax.text(-250,420,'Data Source: stats.nba.com', fontsize=12)
		plt.show()