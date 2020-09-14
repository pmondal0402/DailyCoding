# Knight's tour for NxN board
def main():
  N = 8 # Chessboard size
 
  def is_valid(i, j, sol):
    '''
    Returns true if (x, y) are valid positons in the N*N chessboard
    else returns false
    '''
    # is the (i, j) position inside the chess board
    if (i>=1 and i<=N and j>=1 and j<=N):
      # Is the cell unoccupied i.e. value -1.
      # All unoccupied cells are filled with value -1
      if (sol[i][j] == -1):
        return True
    return False
  
  def knight_tour(sol, i, j, step_count, x_move, y_move):
    if (step_count == N*N):
      # If solution is obtained, just return True
      return True
  
    for k in range(0, 8):
      # a knight has 8 possibles in in a middle square atmax
      next_i = i + x_move[k]
      next_j = j + y_move[k]
  
      if(is_valid(next_i, next_j, sol)):
        sol[next_i][next_j] = step_count
        # Check if there is a possible second move after this move if not
        # backtrack
        if(knight_tour(sol, next_i, next_j, step_count + 1, x_move, y_move)):
          return True
        sol[next_i][next_j] = -1 # Backtracking 
        # Don't understand this
    return False
  
  def start_knight_tour():
    sol = []
  
    for i in range(0, N+1):
      a = [0] + ([-1]*N)
      # Don't understand
      sol.append(a)
  
    # Valid next moves for a given pos (i, j) --> (i+x_move, j+y_move)
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    
    sol[1][1] = 0 # Placing knight at cell (1, 1)
  
    if (knight_tour(sol, 1, 1, 1, x_move, y_move)):
      for i in range(1, N+1):
        print(sol[i][1:])
      return True
    return False

  print(start_knight_tour())


if __name__ == main():
  main()
  '''
  ref 
  https://www.codesdope.com/course/algorithms-knights-tour-problem/
  '''
