def isPossible(a, n):
  cur = a[0]
  cur -=1

  for i in range(1, n):
    nxt = a[i]
    if (nxt > cur):
      nxt -= 1

    elif(nxt < cur):
      return False
    cur = nxt

  return True

a = [4, 2, 3] # [1, 2, 1, 2, 3]

n = len(a)
print(isPossible(a, n))
