from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize an empty board (use 'E' for empty cells)
        board = ['E'] * 9

        turn_max = len(moves)
        for turn, move in enumerate(moves):
            row, col = move
            pos = 3 * row + col
            player = 'A' if turn % 2 == 0 else 'B'
            board[pos] = player

            # Check for row, column, and diagonal wins
            for i in range(3):
                if all(board[i * 3 + j] == player for j in range(3)):
                    return player
                if all(board[j * 3 + i] == player for j in range(3)):
                    return player
            if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
                return player

        # Check for draw or pending
        if turn_max == 9:
            return 'Draw'
        else:
            return 'Pending'

# Test cases
solution = Solution()
print(solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))                          # A
print(solution.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))                    # B
print(solution.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))  # Draw
print(solution.tictactoe([[1,1],[2,0],[0,2],[0,1],[0,0],[2,2],[2,1],[1,2]]))        # Pending
