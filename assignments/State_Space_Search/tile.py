#!/usr/bin/env python3
# Danny Diep, Jason Duong, Joshua Konechy
# CPSC 481-01
# 2022-02-02
# @DannyDiep963, @duong-jason, @KonechyJ
#
# Assignment #1 - Sliding Tile Puzzle
#
"""sliding tile puzzle implementation with DFS and BFS"""


class State:
    """State Representation: current configuration of puzzle"""

    def __init__(self, blank, state, move=None):
        self.blank = blank # the blank tile position
        self.state = state # a list of the current configuration
        self.move = move   # the action/move that was performed to obtain the current state


class Board(State):
    """State Space Representation"""

    def __init__(self, blank, start=None, goal=None):
        State.__init__(self, blank, start)

        self.goal = goal                             # goal state
        self.closed = [self.state]                   # avoids revisited redundant nodes
        self.size = int(len(self.state) ** (1 / 2))  # matrix size
        self.path = {                                # keeps track of the current path of states and actions/moves
            "state": [self.state],
            "move" : [None]
        }

    def reset(self):
        """re-initializes the path and closed list from future searches"""
        self.closed = [self.state]
        self.path = {
            "state": [self.state],
            "move" : [None]
        }

    def expand(self, blank):
        """
        ORIGINAL SOURCE: https://github.com/aimacode/aima-python/blob/master/search.py on line 440
        expands neighbor tiles by removing tiles if the blank is on any border
        """
        # convert to numerical representation
        action = {"UP": -self.size, "DOWN": self.size, "LEFT": -1, "RIGHT": 1}
        # list of all possible directions
        direction = ["DOWN", "UP", "RIGHT", "LEFT"]

        if blank < self.size:  # blank is on the top-most border
            direction.remove("UP")
        if blank >= self.size ** 2 - self.size:  # blank is on the bottom-most border
            direction.remove("DOWN")
        if blank % self.size == 0:  # blank is on the left-most border
            direction.remove("LEFT")
        if blank % self.size == self.size - 1:  # blank is on the right-most border
            direction.remove("RIGHT")

        # returns the list of valid numerical actions/moves
        return [blank + action[move] for move in direction]

    def action(self, blank, move):
        """returns the action with respect to the blank tile and the target tile"""
        # find distance
        diff = move - blank
        # convert to string representation
        action = { -self.size: "UP", self.size: "DOWN", -1: "LEFT", 1: "RIGHT" }
        return action[diff]  # returns the action/move in a string representation

    def solve(self):
        """generates search algorithms to solve the tile puzzle"""
        print("---\nDFS\n---")
        self.dfs(State(self.blank, self.state), [self.state])
        self.reconstruct()

        self.reset()

        print("---\nBFS\n---")
        self.bfs()
        self.reconstruct()

    def reconstruct(self):
        """outputs the states and path needed to solve"""
        for i, (node, move) in enumerate(zip(self.path["state"], self.path["move"])):
            print("State: {} Move: {}".format(node, move))

        print("\nExplored {} States".format(len(self.closed)))

    def dfs(self, top, path):
        """depth-first search implementation"""

        # validate if goal state reached
        if top.state != self.goal:
            for move in self.expand(top.blank):
                # gets all possible actions from the current blank tile
                # swaps a copy of the current blank tile with one of its child tile
                # original copy is unmodified if backtrack occurs
                child = list(top.state)
                child[top.blank], child[move] = child[move], child[top.blank]

                # check if the child has already been visited
                if child not in self.closed and child not in path:
                    # child is now visited
                    self.closed.append(child)

                    self.path["state"].append(child)
                    self.path["move"].append(self.action(top.blank, move))

                    # recursively search the child state until goal state or exhausted
                    return self.dfs(State(move, child, move), path + [child])

        return None

    def bfs(self):
        """breadth-first search implementation"""

        # queue data structure
        OPEN = [self]
        # tuple-list conntaining the current state path and current action/move path
        MEM = [([self.state], [None])]

        while OPEN:
            frontier = OPEN.pop(0)
            spath, mpath = MEM[0][0], MEM[0][1]

            for move in self.expand(frontier.blank):
                # gets all possible actions from the current blank tile
                # swaps a copy of the current blank tile with one of its child tile
                # original copy is unmodified for future swappings of the same parent
                child = list(frontier.state)
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                # check if the child has already been visited (cycle)
                # or currently in queue to be explored (redundant-path)
                if child not in self.closed and child not in OPEN:
                    # child is now visited
                    self.closed.append(child)
                    # push child node to explore set
                    OPEN.append(State(move, child, move))
                    # keeps track of the current path from root to child state
                    MEM.append((
                        spath + [child],
                        mpath + [self.action(frontier.blank, move)])
                    )

                if child == self.goal:
                    self.path = {
                        "state": spath + [child],
                        "move" : mpath + [self.action(frontier.blank, move)],
                    }
                    return None

            MEM.pop(0)


if __name__ == "__main__":
    task = [
        Board(0, [0, 3, 2, 1], [1, 2, 3, 0]),
        Board(4, [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0]),
    ]

    for puzzle in task:
        puzzle.solve()
