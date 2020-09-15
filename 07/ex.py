class py_solution():
  def isvalid(self, s):
   '''
   Given a string s containing just the characters '(', ')',
   '{', '}', '[' and ']',
   determine if the input string is valid.
   '''
   stack = []
   for char in s:
     if char in ["(", "{", "["]:
       # Check if s has openning brackets
       stack.append(char)
     else:
       # if current character is not an openning bracket
       # stack cannot be empty
       if not stack:
         #" stack is empty "
         print('stack is empty', stack)
         return False
       current_char = stack.pop()
       # List.pop() returns elements of list 
       # print('pop is\n', stack.pop())
       if current_char == "(":
         if char !=")":
           return False
       if current_char == "{":
         if char !="}":
           return False
       if current_char == "[":
         if char !="]":
           return False

   # Check if stack is empty 
   if stack:
     # print('stack is empty', stack)
     return False
   return True

expr = "()"
expr2 = "[()]{}{[()()]()}"
expr3 = "[(])"
print(py_solution().isvalid(expr))
print(py_solution().isvalid(expr2))
print(py_solution().isvalid(expr3))
