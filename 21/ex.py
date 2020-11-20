# LeetCode Submission
# https://leetcode.com/problems/pascals-triangle/submissions/

class solution:
  def pascaltriangle(self, numRows):
    result = []
    first_list = [1]
    second_list = [1, 1]
    # If numRows is zero, return empty sequence i.e. result
    if numRows == 0:
       return result

    result.append(first_list)
    if numRows ==1:
       return result
    result.append(second_list)

    if numRows ==2:
       return result
    
    for i in range(2, numRows):
        this_list = list(range(i+1))
        # Fill 1st and last element with 1
        this_list[0] = 1
        this_list[i] = 1
        # Get center position
        center = i // 2
        for j in range(1, center+1): # Couting only half
           this_list[j] = result[i - 1][j - 1] + result[i - 1][j]
           this_list[i-j] = this_list[j]
        # Append the row before starting to calculate next row
        result.append(this_list)
    return result     

n = 3
sol = solution().pascaltriangle
print(sol(n))
