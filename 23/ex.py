import numpy as np
class Solution:
  def generateMatrix(self, n):
    # Create nxn matrix
    mat = np.zeros((n, n))


    # Create a loop to fill all empty spots
    fill = 0
    # Fill elements as long as there is any element 0 
    while np.any(mat == 0) : 
      
      # Fill first row with elements from 2 to n along row
      if mat[fill, fill] == 0:
        val = np.amax(mat)
        count = 1
        for j in range(fill, n - fill):
          for i in range(fill, fill+1):
            mat[i, j] = val + count
            count +=1
  
      if n > 1: 
        # Fill the last column
        j = n - 1 - fill # Last column
        if mat[1+fill, j] == 0:
           val = np.amax(mat)
           count = 1
           for i in range(1+fill, n-fill):
             mat[i, j] = val + count
             count += 1 
  
        # Fill last row
        i = n - 1 - fill # Last row
        if mat[i, n-2 - fill] == 0:
          val = np.amax(mat)
          count = 1
          for j in range(n-2 - fill, -1 + fill, -1):
            mat[i, j] = val + count
            count += 1 
  
        
        # Fill the first column
        j = fill # First column
        if mat[n-2-fill, j] == 0:
           count = 1
           val = np.amax(mat)
           for i in range(n-2 - fill, 0+fill, -1):
             mat[i, j] = val + count 
             count += 1
        fill +=1
   
    print(mat) 
    return mat

# Ex.
n = 9
sol = Solution().generateMatrix
sol(n)
