import numpy as np
class Solution:
  def runningSum(self, nums):
   
    nums2 = np.array(nums)
    # Get the running sum
    dim = len(nums2)
  
    runsum = []
    for i in range(dim):
      # Create array with elements from 0 to i
      runsum.append(sum(nums2[0:i+1]))
      # print(i, sum(nums2[0:i+1]))
    return runsum

# nums = [1, 2, 3, 4]
# nums = [1,1,1,1,1]
# nums = [3,1,2,10,1]
nums = []

sol = Solution().runningSum
print(sol(nums))

