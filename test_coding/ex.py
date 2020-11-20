class Solution:
  def SumMinList(self, nums):
    # Sort the list
    nums.sort()
    # Return sum of every alternate elements
    # starting 0th element of sorted list 
    return sum(nums[0:-1:2])

# nums = [1,4,3,2]
nums = [6,2,6,5,1,2]
sol = Solution().SumMinList
print(sol(nums))

