#!/usr/bin/env python3
# Danny Diep, Jason Duong, Joshua Konechy
# CPSC 481-01
# 2022-02-18
# @dannydiep963, @duong-jason, @Konechyj
#
# Assignment #1 - Sliding Tile Puzzle
#
"""sliding tile puzzle implementation with DFS and BFS"""


import math
from collections import namedtuple


State = namedtuple("State", ["board", "blank", "move"])


class Puzzle:
    """State Space Representation"""

    def __init__(self, blank, start=None, goal=None, table=None):
        self._state = State(start, blank, None)

        self._size = math.isqrt(len(start)) # matrix size
        self._goal = goal # goal state
        self._table = table # set of possible moves
        self._closed = [self._state] # avoids revisited (cycles)
        self._path = [self._state] # keeps track of the current path of states
        self._action = {-self._size: "UP", self._size: "DOWN", -1: "LEFT", 1: "RIGHT"}

    def solve(self):
        """generates search algorithms to solve the tile puzzle"""
        print(f"---\n{self._size}x{self._size} -> IDDFS\n---")
        self.iddfs()
        self.reconstruct()

        print(f"---\n{self._size}x{self._size} -> BFS\n---")
        self.bfs(self._closed)
        self.reconstruct()

    def reconstruct(self):
        """outputs the states and path needed to solve"""
        for node in self._path:
            print(f"State: {node.board} Move: {node.move}")
        print(f"\nExplored {len(self._closed)} States")

    def iddfs(self, depth=0):
        """iterative deepening depth-first search implementation"""
        while not self.dls(self._state, self._path, self._closed, depth := depth + 1):
            pass

    def dls(self, frontier, path, closed, depth):
        """depth-limited search implementation"""

        if frontier.board == self._goal: # validate if goal state reached
            self._path = path
            return True
        if depth < 1: # depth-limit reached
            self._closed = [self._state]
            self._path = [self._state]
            return False

        for move in self._table[frontier.blank]:
            # gets all possible actions from the current blank tile
            # swaps a copy of the current blank tile with one of its child tile
            child = frontier.board[:]
            child[frontier.blank], child[move] = child[move], child[frontier.blank]

            # check if the child has already been visited
            if child not in closed and child not in path:
                self._closed.append(child) # child is now visited

                # recursively search the child state until goal state or exhausted
                # keeps a record of the current path (root + siblings)
                # recursion ends when goal state is found; otherwise exhausts all nodes <= depth
                if self.dls(
                    State(child, move, self._action[move - frontier.blank]),
                    path + [State(child, move, self._action[move - frontier.blank])],
                    closed + [child],
                    depth - 1
                ):
                    return True

    def bfs(self, closed):
        """breadth-first search implementation"""
        open = [self._state] # queue data structure
        history = [[self._state]]

        while open:
            frontier, path = open.pop(0), history.pop(0)

            for move in self._table[frontier.blank]:
                # gets all possible actions from the current blank tile
                # swaps a copy of the current blank tile with one of its child tile
                child = frontier.board[:]
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                # check if the child has already been visited (cycle)
                # or currently in queue to be explored (redundant-path/back-edge)
                if child not in closed and child not in open:
                    self._closed.append(child) # child is now visited
                    open.append(State(child, move, self._action[move - frontier.blank])) # push child node to explored set
                    history.append(path + [State(child, move, self._action[move - frontier.blank])]) # keeps track of the current path from root to child state

                # validates whether the current state has reached its goal state
                if child == self._goal:
                    self._path = path + [State(child, move, self._action[move - frontier.blank])] # save the direct paths and moves
                    return


if __name__ == "__main__":
    task = [
        Puzzle(0, [0, 3, 2, 1], [1, 2, 3, 0], [[1, 2], [0, 3], [3, 0], [2, 1]]),
        Puzzle(4, [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0], (
                (1, 3),
                (2, 0, 4),
                (5, 1),
                (4, 0, 6),
                (1, 3, 5, 7),
                (8, 4, 2),
                (3, 7),
                (6, 4, 8),
                (5, 7),
            ))
    ]

    for puzzle in task:
        puzzle.solve()
