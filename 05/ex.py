class py_solution:
  def longestCommonPrefix(self, s):
    if not s:
      return ""
    shortest_str = min(s, key = len)
    # Get first letter of shortest_str
    for i , char in enumerate(shortest_str):
      # print(i, char)
      # Compare with first letter of other strings in list
      for others in s:
        # print(others)
        # If letters do not match save shortest_str till i-1 letter
        if others[i] != char:
          return shortest_str[:i]
    return shortest_str


# st = ["dog","racecar","car"]
st = ["flower","flow","flight"]
print(py_solution().longestCommonPrefix(st))
