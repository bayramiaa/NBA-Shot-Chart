from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt

def draw_court(ax = None, color = "black", lw=2,outer_lines = False):
	"""
	Uses matplotlib to draw out the lines of half a basketball court
	"""

	if ax is None:
		ax = plt.gca()

	hoop = Circle((0,0), radius = 7.5, linewidth=lw,color = color, fill = False)
	backboard = Rectangle((-30,-7.5), 60, -1, linewidth=lw, color = color)
	key1 = Rectangle((-80,-47.5), 160, 190, linewidth=lw, color=color,fill=False)
	key2 = Rectangle((-60,-47.5), 120, 190, linewidth=lw, color=color,fill=False)
	top_ft= Arc((0,142.5),120,120,theta1=0,theta2=180,linewidth=lw,color=color,fill=False)
	bot_ft= Arc((0,142.5),120,120, theta1=180, theta2=0,linewidth=lw,color=color,linestyle='dashed')
	restricted = Arc((0,0),80,80,theta1=0,theta2=180,linewidth=lw,color=color)
	right3= Rectangle((-220,-47.5),0,140,linewidth=lw,color=color)
	left3 = Rectangle((220,-47.5),0,140, linewidth=lw,color=color)
	arc3 = Arc((0,0),475,475, theta1=22, theta2=158,linewidth=lw,color=color)
	Center_court1 = Arc((0,395), 120, 120, theta1=180, theta2 = 0, linewidth=lw,color=color)
	Center_court2 = Arc((0,395),40,40, theta1=180,theta2=0,linewidth=lw,color=color)

	### Court elements to be plotted
	court_elements = [hoop,backboard,key1,key2,top_ft,bot_ft,
					  restricted,right3,left3,arc3,Center_court1,Center_court2]

	if outer_lines:
		outer_lines = Rectangle((-250,-47.5), 500, 442.5,linewidth=lw,color=color,fill=False)
		court_elements.append(outer_lines)

	for element in court_elements:
		ax.add_patch(element)
	return ax