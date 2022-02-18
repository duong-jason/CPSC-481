# Assignment #1 - Sliding Tile Puzzle with Depth-First and Breadth-First Searches

# Issues
```python
# the dfs function for the 3x3 puzzle seems to stop processing due to the stack recursion limit
def dfs(self, frontier, path)
```

# Accomodations
During testing/debugging, we found the solution to the 3x3 tile puzzle at <em> Depth: 14. </em> <br>
This assumes that our original depth-first search implementation did not have enough memory to reach a terminal state. <br>
In addition, this meant the solution laid in another branch, which was never reached by our depth-first search algorithm.

## Group Members
**Names:** Danny Diep, Jason Duong, Joshua Konechy <br>
**Emails:** danny.963.dk@gmail.com, reddkingdom@csu.fullerton.edu, Jkonechy@live.com <br>
