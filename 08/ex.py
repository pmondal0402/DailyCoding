import math

# See notes on linked lists
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      # print('--> ', self.data)

# Function to create newNode in a linkedList
def newNode(key):
   temp = Node(key)
   temp.data = key
   temp.next = None
   return temp

# A utility function to print linked list
# What is a utility function ?
def printlist(node):
  while (node !=None):
    print(node.data, end = " ")
    node = node.next

# Merges two given lists in-place
# It compares head nodes and calls mergeUtil()

def merge(h1, h2):
  if (h1 == None):
    return h2
  if (h2 == None) :
    return h1

  # Start with the linked list
  # whose head data is the least
  if (h1.data < h2.data):
    h1.next = merge(h1.next, h2)
    return h1
  else:
    h2.next = merge(h1, h2.next)
    return h2

# Create a linked list 1->3->5
head1 = newNode(1)
head1.next = newNode(3)
head1.next = newNode(5)

# Create a linked list 0-->2-->4
head2 = newNode(0)
head2.next = newNode(2)
head2.next = newNode(4)
mergehead = merge(head1, head2)
print(mergehead)

"""
if __name__ == main():
  # Create a linked list 1->3->5
  head1 = newNode(1)
  head1.next = newNode(3)
  head1.next = newNode(5)
  print('bla bla ')
  # Create a linked list 0-->2-->4
  head2 = newNode(0)
  head2.next = newNode(2)
  head2.next = newNode(4)
  
  mergehead = merge(head1, head2)
  print(mergehead)
"""
