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
num_of_iterations = 100

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
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
