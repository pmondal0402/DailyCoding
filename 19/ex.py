import numpy as np

class Solution:
   def uniqueOccurrences(self, arr):
      # Count number of times each element is repeated 
      # starting from 1st element
      count_elm = [ arr.count(it) for it in set(arr)] 
      # Find unique elemets of the list count_elm
      count_elm_uniq = np.unique(np.array(count_elm))
      if len(count_elm) == len(set(count_elm_uniq)):
         return True
      return False

sol = Solution()
# arr = [1,2] # [1,2,2,1,1,3]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr))
