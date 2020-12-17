import numpy as np

class Solution:
   def numIdenticalPairs(self, nums) :

    # Pick i and check if nums[j] == nums[i]
    dim = len(nums)
    count = 0  

    for i in range(0, dim): # Change to dim
      numi = nums[i]
      for j in range(i+1, dim):
       # Is nums[i] == nums[j] ?
       if nums[j] == nums[i]:
          count = count + 1  
          print(i, nums[j]) 
         
    return count

# nums = np.array([1,2,3,1,1,3])    
# nums = [1,1,1,1]
# nums = [1,2,3]
nums = []
sol = Solution().numIdenticalPairs
print(sol(nums))  
