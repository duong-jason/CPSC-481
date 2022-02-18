# Assignment #1 - Sliding Tile Puzzle with Depth-First and Breadth-First Searches

* **Problem/Issues:**
    ```python
    # the dfs function for the 3x3 puzzle stops processing due to the stack recursion limit
    def dfs(self, frontier, path)
    ```
    * Our original depth-first search algorithm did not have enough memory to reach a terminal state.
* **Solution/Accomodations:**
    ```python
    # NOTE: uncomment code to find solution's depth
    def iddfs(self):
        depth = 0
        while not self.dls(State(self.blank, self.state), [self.state], depth):
            depth += 1
            self.reset()
        # print(depth)
    ```

    * We decided to additionally implement an iterative deepening algorithm to prove that the 3x3 tile puzzle's state-space was too large to be executed by a dfs algorithm.
    * During testing/debugging, we found the solution to the 3x3 tile puzzle at <em> Depth = 14 </em>.
    * With our depth-first search algorithm, it explored past depth 14 and preemptively stopped the recursion process.
    * This meant the solution layed in another branch, which was never reached by our depth-first search algorithm.

# Group Members
**Names:** Danny Diep, Jason Duong, Joshua Konechy <br>
**Emails:** danny.963.dk@gmail.com, reddkingdom@csu.fullerton.edu, Jkonechy@live.com <br>
