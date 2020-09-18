class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

# Define a function to return a listed node
def newNode(key):
  temp = Node(key)
  temp.data = key
  # print('->', temp.data)
  temp.next = None
  return temp

def merge(h1, h2):
  """
  merge two linked lists h1 and h2 
  """
  if (h1 == None):
    return h2

  if (h2 == None):
    return h1
  
  # Start with linked list whose data is lease
  if (h1.data < h2.data):
    
    h1.next = merge(h1.next, h2)
    return h1
  else:
    h2.next = merge(h1, h2.next)
    return h2
  
  return None 

# Create a linked list 1->3->5
head1 = newNode(1)
head1.next = newNode(3)
head1.next.next = newNode(5)
# print(head1.data)
# print(head1.next.data)
# print(head1.next.next.data)

# Create a linked list 0->2->4
head2 = newNode(0)
head2.next = newNode(2)
head1.next.next = newNode(4)
mg = merge(head1, head2)

print('mg is', mg.data)
print('mg is', mg.next.data)
print('mg is', mg.next.next.data)
print('mg is', mg.next.next.next.data)





