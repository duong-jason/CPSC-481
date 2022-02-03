#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#

class Graph:
    """
        @start = start state
        @final = final/goal state
        @visited = list of visited nodes/states
        @action = list of valid moves/operators
    """
    def __init__(self, start, final, visited, action):
        self.start = start 
        self.final = final
        self.visited = start
        self.action = action.split("\\")

    def dfs:

    def bfs:


def main():
    puzzle2 = Graph([None, 3, 2, 1],
                    [1, 2, 3, None],
                    "U\D\L\R")

    puzzle3 = Graph([1, 4, 3, 7, None, 6, 5, 8, 2],
                    [1, 2, 3, 4, 5, 6, 7, 8, None],
                    "U\D\L\R")


if __name__ == "__main__":
    main()
