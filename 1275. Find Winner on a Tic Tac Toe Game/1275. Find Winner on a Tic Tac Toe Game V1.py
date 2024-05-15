from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[1, 2, 3], # Row 1 (columns: 1, 2, 3)
                [4, 5, 6], # Row 2 (columns: 1, 2, 3)
                [7, 8, 9]] # Row 3 (columns: 1, 2, 3)
        
        turn_number = 0
        for move in moves:
            row = move[0]
            col = move[1]
            if turn_number % 2 == 0:    # player A turn places X
                grid[row][col] = 'X'
            else:                       # player B turn places O
                grid[row][col] = 'O'

            turn_number += 1

        if turn_number <= 4:
            return("Pending")

        elif grid[0][0] == grid[0][1] == grid[0][2]: # Row 0 Check
            if grid[0][0] == 'X':
                return('A')
            else:
                return('B')

        elif grid[1][0] == grid[1][1] == grid[1][2]: # Row 1 Check
            if grid[1][0] == 'X':
                return('A')
            else:
                return('B')

        elif grid[2][0] == grid[2][1] == grid[2][2]: # Row 2 Check
            if grid[2][0] == 'X':
                return('A')
            else:
                return('B')

        elif grid[0][0] == grid[1][0] == grid[2][0]: # Col 0 Check
            if grid[0][0] == 'X':
                return('A')
            else:
                return('B')

        elif grid[0][1] == grid[1][1] == grid[2][1]: # Col 1 Check
            if grid[0][1] == 'X':
                return('A')
            else:
                return('B')

        elif grid[0][2] == grid[1][2] == grid[2][2]: # Col 2 Check
            if grid[0][2] == 'X':
                return('A')
            else:
                return('B')

        elif grid[0][0] == grid[1][1] == grid[2][2]: # Diag 0 Check
            if grid[0][0] == 'X':
                return('A')
            else:
                return('B')

        elif grid[0][2] == grid[1][1] == grid[2][0]: # Diag 1 Check
            if grid[0][2] == 'X':
                return('A')
            else:
                return('B')

        else:
            for row in grid:
                for col in row:
                    if isinstance(col, int):
                        return("Pending")
            return('Draw')

# Test cases
solution = Solution()
print(solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))                          # A
print(solution.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))                    # B
print(solution.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))  # Draw
print(solution.tictactoe([[1,1],[2,0],[0,2],[0,1],[0,0],[2,2],[2,1],[1,2]]))        # Expected Pending