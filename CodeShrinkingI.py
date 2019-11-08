# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:29:54 2019

@author: gy19yh
"""

############################
#######pratical 2############
############################


import random
import operator
import matplotlib.pyplot

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents = []
agents.append([y0,x0])
agents.append([50,50])
print(y0,x0)
#### get rid of X and Y
# agents = []
# agents.append([random.randint(0,99)],[random.randint(0,99)])
print(max(agents, key = operator.itemgetter(1)))

matplotlib.pyplot.ylim(0,99)
matplotlib.pyplot.xlim(0,99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(x0, y0, color= 'red')
matplotlib.pyplot.show()