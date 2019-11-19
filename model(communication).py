# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import operator
import matplotlib.pyplot
import agentframework

# Initialising parameters
num_of_agents = 10
num_of_iterations = 1
neighbourhood = 20


#def distance_between(agents_row_a, agents_row_b):
    #return (((agents_row_a.x - agents_row_b.x)**2) +((agents_row_a.y - agents_row_b.y)**2))**0.5

#def distance_between(self, agent):
    #return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

# Loading the environment
f = open("in.txt", 'r')
environment = []
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    environment.append(rowlist)
#print(environment)


# Initialising agents
agents = []
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))

#for i in range(num_of_agents):
#    x =
#    y =
#    agents.append(agentframework.Agent(environment,agents, x, y))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Plot the agents        
matplotlib.pyplot.xlim(0, 99) 
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#Calculate distances between all agetns
distances = []
for agent_a in agents:
    distance = []
    for agent_b in agents:
        distance.append(distance_between(agent_a, agent_b))
    distances.append(distance)
    
    
for j in range(num_of_iterations):
    for i in range(num_of_iterations):
#        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
print(distances)
   