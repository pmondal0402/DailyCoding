import numpy as np

class Solution:
  def solveSudoku(self, board):
      def getarray(board):
          for col in range(9): 
            for row in range(9):
               if board[row][col] == ".":
                   board[row][col] = 0
          grid = np.array(board)
          return grid.astype(np.float)         

      def printGrid():      
          for row in grid:
             print(row)

      def ispossible(y, x, n):
         """
         Returns if it's possible to put a number n in box position (x, y)
         """
         # Each of the digits 1-9 must occur exactly once in each column
         for col in range(9):
            if grid[y, col] == n:
               return False
         
         # Each of the digits 1-9 must occur exactly once in each row.         
         for row in range(9):
             if grid[row, x] == n:
                return False

         # Each of the digits 1-9 must occur exactly once in each of the 9 3x3
         # sub-boxes of the grid. 
         # Shift box coordinate i.e. which 3x3 box -->1st or 2nd or 3rd
         x0 = (x//3)*3  
         y0 = (y//3)*3
         for col in range(3):
            for row in range(3):
               if grid[ y0 + col, x0 + row] == n :
                  return False

         return True 


      # Now solve the sudoku puzzle
      def solve_sudoku():
         """
         Solves sudoku empty boxes one at a time
         """
         for y in range(9):
             for x in range(9):
                if grid[y, x] == str(0):
                   # print('Empty spot found')
                   for n in range(1, 10):
                       if ispossible(y, x, n):
                           # print('position filled is', y, x, 100*n)
                           # fill the spot with n if possible
                           grid[y, x] = n
                           solve_sudoku()
                           # If the number n is not a good choice
                           # and we reached a deadend, then backtrack
                           grid[y, x] = 0 
                           # Print("Spot is empty again! Backtracking")
                   return 
         print('The Solution is\n')
         printGrid()
         
      grid = getarray(board)
      solve_sudoku() 
      # return solve_sudoku()

board = \
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution().solveSudoku
sol(board)
