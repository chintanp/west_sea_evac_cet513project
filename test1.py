# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:37:47 2020

@author: icnis
"""
# for the maximum flow problem

from ortools.graph import pywrapgraph
import numpy as np

# instantinae a SimpleMinCostFlow Solver
max_flow = pywrapgraph.SimpleMaxFlow()

# instantinae a SimpleMinCostFlow Solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# define start_nodes, end_nodes, capacities, and unit_cost

# (a): maximum flow problem
start_nodes = [0, 0, 1, 1, 2, 2, 3, 4, 5, 6]
end_nodes =   [1, 3, 2, 6, 4, 6, 2, 5, 6, 7]

# cap. in veh/hr
#capacities = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1900, 1900]
# cap in veh/min
capacities = [25, 25, 25, 25, 25, 25, 25, 25, 32, 32]

# (c) minimum cost problem

# cost in hr
#unit_cost = [0.05, 0.04, 0.051, 0.056, 0.016, 0.05, 0.02, 0.048, 0.014, 0.033]

# cost in min
unit_cost = [3, 2, 3, 4, 1, 3, 1, 3, 1, 2]

print('UnitCost:', unit_cost)

# add each link
for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_cost[i])
    print('%3s -> %3s' % (start_nodes[i], end_nodes[i]))

# solve
# Note: revise this to be consistent with the node definition
if max_flow.Solve(0, 7) == max_flow.OPTIMAL:
    print('Max Flow:', max_flow.OptimalFlow())
    print(' ')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    # (b): minimum cut problem
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('There was an issue with the max flow input.')


# add supplies:
#supplies = [100 , 100, 100, 100, 100, 100, 100, -700]
supplies = [2, 2, 2, 2, 2, 2, 2, -14]

for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

# solve
if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print(' ')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
            min_cost_flow.Tail(i),
            min_cost_flow.Head(i),
            min_cost_flow.Flow(i),
            min_cost_flow.Capacity(i),
            cost))
else:
    print('There was an issue with the min cost flow input.')
