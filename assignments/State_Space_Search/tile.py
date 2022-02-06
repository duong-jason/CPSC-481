#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1 - Tile Puzzle
#
"""2x2 tile puzzle implementation with DFS and BFS"""



class State:
    """State Reprsentation: current configuration of puzzle"""

    def __init__(self, blank, state, move=None):
        self.blank = blank
        self.state = state
        self.move = move


class Problem(State):
    """State Space Representation"""

    def __init__(self, blank, table, start=None, goal=None):
        State.__init__(self, blank, start)

        self.table = table
        self.goal = goal
        self.path = []
        self.closed = []

    def reset(self):
        """re-initializes the path and closed list from future searches"""
        self.closed.clear()
        self.path.clear()

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
        for count, node in enumerate(self.path):
            print("Explored #", count, node)

    def dfs(self, top):
        """depth-first search implementation"""
        self.path.append("State: {} Move: {}".format(top.state, top.move))
        self.closed.append(top.state)

        if top.state != self.goal:
            for move in self.table[top.blank]:
                child = top.state.copy()
                child[top.blank], child[move] = child[move], child[top.blank]

                if child not in self.closed:
                    return self.dfs(State(move, child, move))

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self]  # queue data structure
        self.closed.append(self.state)  # closed list of visited states

        while OPEN:
            frontier = OPEN.pop(0)
            for move in self.table[frontier.blank]:
                child = frontier.state.copy()
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                if frontier.state == self.goal:
                    self.path.append("State: {} Move: {}".format(frontier.state, move))
                    return None

                if child not in self.closed:
                    self.closed.append(child)
                    OPEN.append(State(move, child, move))
                    self.path.append("State: {} Move: {}".format(frontier.state, move))


if __name__ == "__main__":
    TILE_2 = Problem(0, ((1, 2), (0, 3), (3, 0), (2, 1)), [0, 3, 2, 1], [1, 2, 3, 0])
    TILE_3 = Problem(
        4,
        (
            (3, 1),
            (0, 2, 4),
            (1, 5),
            (0, 4, 6),
            (1, 5, 7, 3),
            (2, 4, 8),
            (7, 3),
            (8, 4, 6),
            (7, 5),
        ),
        [1, 4, 3, 7, 0, 6, 5, 8, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
    )

    TILE_2.solve()
    TILE_3.solve()
