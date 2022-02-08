#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1 - Tile Puzzle
#
"""tile puzzle implementation with DFS and BFS"""


class State:
    """State Representation: current configuration of puzzle"""

    def __init__(self, blank, state, move=None):
        self.blank = blank
        self.state = state
        self.move = move


class Puzzle(State):
    """State Space Representation"""

    def __init__(self, blank, start=None, goal=None):
        State.__init__(self, blank, start)

        self.goal = goal
        self.path = [{ 'state': self.state, 'move': None }]
        self.closed = []
        self.size = len(self.state) ** (1/2) # get matrix size

    def reset(self):
        """re-initializes the path and closed list from future searches"""
        self.closed.clear()
        self.path.clear()

    def expand(self, blank):
        """expands neighbor tiles by removing tiles if the blank is on any border"""
        action = {"UP": -self.size, "DOWN": self.size, "LEFT": -1, "RIGHT": 1}
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]

        if blank < self.size: # blank is on the top-most border 
            direction.remove("UP")
        if blank >= self.size ** 2 - self.size: # blank is on the bottom-most border 
            direction.remove("DOWN")
        if blank % self.size == 0: # blank is on the left-most border 
            direction.remove("LEFT")
        if blank % self.size == self.size-1: # blank is on the right-most border 
            direction.remove("RIGHT")

        return [int(blank + action[move]) for move in direction]

    def action(self, blank, move):
        """returns the action with respect to the blank tile and the target tile"""
        dis = move - blank # find distance
        action = {-self.size: "UP", self.size: "DOWN", -1: "LEFT", 1: "RIGHT"}
        return action[dis]

    def solve(self):
        """generates search algorithms to solve the tile puzzle"""
        print("---\nDFS\n---")
        self.dfs(State(self.blank, self.state))
        self.reconstruct()

        self.reset()

        print("---\nBFS\n---")
        self.bfs()
        self.reconstruct()

    def reconstruct(self):
        """outputs the states and path needed to solve"""
        for node in self.path:
            print("State: {} Move: {}".format(node['state'], node['move']))

        print("Explored {} States".format(len(self.path)))


    def dfs(self, top):
        """depth-first search implementation"""
        self.closed.append(top.state)

        if top.state != self.goal:
            #for move in self.table[top.blank]:
            for move in self.expand(top.blank):
                child = top.state[:]
                child[top.blank], child[move] = child[move], child[top.blank]

                if child not in self.closed:
                    self.path.append({ 'state': child, 'move': self.action(top.blank, move) })
                    return self.dfs(State(move, child, move))

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self]  # queue data structure
        self.closed.append(self.state)  # closed list of visited states

        while OPEN:
            frontier = OPEN.pop(0)
            #for move in self.table[frontier.blank]:
            for move in self.expand(frontier.blank):
                child = frontier.state[:]
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                if child not in self.closed:
                    self.closed.append(child)
                    self.path.append({ 'state': child, 'move': self.action(frontier.blank, move) })
                    OPEN.append(State(move, child, move))

                    if child == self.goal:
                        return None


if __name__ == "__main__":
    TILE_2 = Puzzle(0, [0, 3, 2, 1], [1, 2, 3, 0])
    TILE_3 = Puzzle(4, [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0])

    TILE_2.solve()
    TILE_3.solve()
