"""

A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

  1  2  3
  4  5  6
  7  8  9
would be represented as [[1,2,3], [4,5,6], [7,8,9]].

Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get

  3  6  9
  2  5  8    
  1  4  7

 
  >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]

  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

  >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]



"""

def leftrotate(l):
  a,x = [],[]
  for i in range(len(l)-1,-1,-1):
    for j in range(len(l)):
      a.append(l[j][i])
    x.append(a)
    a = []
  return x

print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))