import pygame
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *


class Astar


def A(start, goal):
    closedset = {}
    openSet = {}
    cameFrom = Node()
    gScore: = 10
    gScore[start] = 0
    fScore[start] += (start, goal)

    while openSet is not empty
        current = the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        closedSet.Add(current)
        for each neighbor of current
            if neighbor in closedSet
                continue
            tentative_gScore[current] + dist_between(current, neighbor)
            if neighbor not in openSet
                openSet.Add(neighbor)
            else if tentative_gScore >= gScore[neighbor]
                continue

            cameFrom[neighbor]: = current
            gScore[neighbor]: = tentative_gScore
            fScore[neighbor]: = gScore[nighbor] + heuristic_cost_estimate(neighbor, goal)

        return failure

def reconstruct_path(cameFrom, current)
    total_path: = [current]
    while current in cameFrom.Keys:
        current: = cameFrom[current]
        total_path.append(current)
    return total_path