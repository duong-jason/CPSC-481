# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#
"""2x2 tile puzzle implementation with DFS and BFS"""

TABLE = ((1, 2), (0, 3), (3, 0), (2, 1))
ACTION = {
    (0, 1): "Right",
    (0, 2): "Down",
    (1, 0): "Left",
    (1, 3): "Down",
    (2, 3): "Right",
    (2, 0): "Up",
    (3, 2): "Left",
    (3, 1): "Up",
}

CLOSED = []

class State:
    """State Reprsentation"""

    def __init__(self, blank, state, parent=None, move=None):
        self.blank = blank
        self.state = state
        self.parent = parent
        self.move = move


class Problem(State):
    """State Space/Problem Representation"""

    def __init__(self, blank, table, start=None, goal=None):
        State.__init__(self, blank, start)

        self.table = table
        self.goal = goal
        self.path = []

    def reset(self):
         self.path = []

    def solve(self):
        """
        print("DFS")
        self.reconstruct(self.dfs(State(self.blank, self.state)))

        self.reset()
        """

        print("DFS")
        print("\nBFS")
        self.reconstruct(self.bfs())

    def reconstruct(self, node):
        """outputs the states and path needed to solve"""
        for count, node in enumerate(self.path):
            print("Explored #", count, node)

    def dfs(self, frontier):
        """depth-first search implementation"""
        CLOSED.append(frontier.state)
        self.path.append("State: {} Move: {}".format(frontier.state, frontier.move))

        if frontier.state != self.goal:
            for move in self.table[frontier.blank]:
                child = frontier.state.copy()
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                if child not in CLOSED:
                    return self.dfs(State(move, child, frontier.state, move))

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self] # queue data structure
        CLOSED.append(self.state) # closed list of visited states

        while OPEN:
            frontier = OPEN.pop(0)
            for move in self.table[frontier.blank]:
                child = frontier.state.copy()
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                if frontier.state == self.goal:
                    self.path.append("State: {} Move: {}".format(frontier.state, move))
                    return None

                if child not in CLOSED:
                    CLOSED.append(child)
                    OPEN.append(State(move, child, frontier.state, move))
                    self.path.append("State: {} Move: {}".format(frontier.state, move))


tile2 = Problem(0, ((1, 2), (0, 3), (3, 0), (2, 1)), [0, 3, 2, 1], [1, 2, 3, 0])
tile3 = Problem(4, ((1, 3), (0, 2, 4), (1, 5), (0, 4, 6), (1, 3, 5, 7), (2, 4, 8), (3, 7), (4, 6, 8), (5, 7)), [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0])


if __name__ == "__main__":
    tile2.solve()
    tile3.solve()
