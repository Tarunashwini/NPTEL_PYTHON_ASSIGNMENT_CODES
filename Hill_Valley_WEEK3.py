"""
In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.

Here are some examples to show how your function should work.

 
>>> counthv([1,2,1,2,3,2,1])
[2, 1]

>>> counthv([1,2,3,1])
[1, 0]

>>> counthv([3,1,2,3])
[0, 1]

"""

# 2. function counthv(l)

def counthv(l):
  a = []
  for i in range(len(l)-1):
    if l[i] < l[i+1]:
      a.append("H")
    else:
      a.append("D")
  he,dw = 0,0
  for i in range(1,len(a)):
    if a[i] == "D" and a[i-1] == "H":
      he += 1
    elif a[i] == "H" and a[i-1] == "D":
      dw += 1
  out = []
  out.append(he)
  out.append(dw)
  return (out)

print(counthv([1,2,1,2,3,2,1]))