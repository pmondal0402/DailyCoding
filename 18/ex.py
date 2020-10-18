class Solution:
   def arrPairSum(self, nums):
       """
       nums : List[int]
       rtype : int
       """
       # Sort the list in ascending order
       nums.sort()
       # print('nums is',nums,  nums[0:-1:2])
       # Pick min and make a pair with 2nd min num 
       return sum(nums[0:-1:2])

sol = Solution().arrPairSum
nums = [1,4,3,2]
print(nums)
print(sol(nums))
