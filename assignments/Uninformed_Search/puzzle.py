#!/usr/bin/env python3
# Danny Diep, Jason Duong, Joshua Konechy
# CPSC 481-01
# 2022-02-02
# @DannyDiep963, @duong-jason, @KonechyJ
#
# Assignment #1 - Sliding Tile Puzzle
#
"""sliding tile puzzle implementation with DFS and BFS"""

"""
TODO:
    fix dfs for 3x3 tile
    display the state as a square-grid
"""

class State:
    """State Representation: current configuration of puzzle"""

    def __init__(self, blank, state, move=None):
        self.blank = blank  # the blank tile position
        self.state = state  # a list of the current configuration
        self.move = move    # the action to get to current state


class Board(State):
    """State Space Representation"""

    def __init__(self, blank, start=None, goal=None, table=None):
        State.__init__(self, blank, start)

        self.goal = goal                             # goal state
        self.closed = [self.state]                   # avoids revisited (cycles)
        self.table = table                           # set of possible moves
        self.size = len(self.state) ** (1 / 2)       # matrix size
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

    def action(self, blank, move):
        """returns the action with respect to the blank tile and the target tile"""
        # map of numerical position to string position
        action = { -self.size: "UP", self.size: "DOWN", -1: "LEFT", 1: "RIGHT" }
        # returns the action/move in a string representation based on the direction
        return action[move - blank]

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

    def dfs(self, frontier, path):
        """depth-first search implementation"""
 
        # validate if goal state reached
        if frontier.state != self.goal:
            for move in self.table[frontier.blank]:
                # gets all possible actions from the current blank tile
                # swaps a copy of the current blank tile with one of its child tile
                # original copy is unmodified if backtrack occurs
                child = frontier.state[:]
                child[frontier.blank], child[move] = child[move], child[frontier.blank]
                # check if the child has already been visited
                if child not in self.closed and child not in path:
                    self.closed.append(child) # child is now visited
                    self.path["state"].append(child)
                    self.path["move"].append(self.action(frontier.blank, move))

                    # recursively search the child state until goal state or exhausted
                    # keeps a record of the current path (root + siblings)
                    return self.dfs(State(move, child, self.action(frontier.blank, move)), path + [child])

        return None


    def bfs(self):
        """breadth-first search implementation"""

        open = [self] # queue data structure
        mem = [([self.state], [None])] # tuple-list conntaining the current state path and current action/move path

        while open:
            frontier, spath, mpath = open.pop(0), mem[0][0], mem[0][1]

            for move in self.table[frontier.blank]:
                # gets all possible actions from the current blank tile
                # swaps a copy of the current blank tile with one of its child tile
                child = frontier.state[:]
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                # check if the child has already been visited (cycle)
                # or currently in queue to be explored (redundant-path/back-edge)
                if child not in self.closed and child not in open:
                    self.closed.append(child)                                          # child is now visited
                    open.append(State(move, child, self.action(frontier.blank, move))) # push child node to explore set
                    mem.append((                                                       # keeps track of the current path from root to child state
                        spath + [child],
                        mpath + [self.action(frontier.blank, move)]
                    ))

                # validates whether the current state has reached its goal state
                if child == self.goal:
                    self.path = { # save the direct paths and moves
                        "state": spath + [child],
                        "move" : mpath + [self.action(frontier.blank, move)],
                    }
                    return None

            mem.pop(0)


if __name__ == "__main__":
    task = [
        Board(0, [0, 3, 2, 1], [1, 2, 3, 0], [[1, 2], [0, 3], [3, 0], [2, 1]]),
        Board(4, [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0], (
                (1, 3),
                (2, 0, 4),
                (5, 1),
                (4, 0, 6),
                (1, 3, 5, 7),
                (8, 4, 2),
                (3, 7),
                (6, 4, 8),
                (5, 7))
             )
    ]

    for puzzle in task:
        puzzle.solve()
