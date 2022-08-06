# Sum of primes

def isprime(n):
    if n<0 or type(n) != int:
        return False
        
    for i in range(2,int(n**1/2)+1):
        if n%i == 0:
            return False
    return True
  
def sumprimes(l):
    s = 0
    for  i in range(len(l)):
        if isprime(l[i]):
            s = s + l[i]
    return s

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))
