import numpy as np
class Solution:
  def productExceptSelf(self, nums):
    # Return multiplication of all elements except i^th element
    dim = len(nums)

    res = []
    for i in range(dim):
      # Initialize list with original list
      nums2 = [nums[it] for it in range(dim) if it != i]
      # print(i, nums2)
      res.append(np.prod( np.array(nums2)))
    return res

nums = [1, 2, 3, 4]
# nums = [0, 0]
sol = Solution()
print(sol.productExceptSelf(nums))
   
