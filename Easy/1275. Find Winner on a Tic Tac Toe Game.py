from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        return moves





# Test cases
solution = Solution()
print(solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))  # Expected output: "X"
print(solution.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))  # Expected output: "Draw"
print(solution.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))  # Expected output: "Draw"