# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:30:28 2019

@author: gy19yh
"""

############################
#######pratical 3###########
########Looping#############
import random
import operator
import matplotlib.pyplot

agents = []
num_of_agents = 10
agents.append([random.randint(0,100),random.randint(0,100)])
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.ylim(0,100)
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1], m[0], color = 'red')
matplotlib.pyplot.show()

###########Boundary##########
import random
import matplotlib.pyplot

data = []
processed_data = []
#i = 0
#j = 0
#Fill with random data.

for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

# Move agent.

#blur.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
        datarow.append(sum)
    processed_data.append(datarow)
    
matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()

