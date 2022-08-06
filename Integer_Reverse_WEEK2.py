#	Int Reverse 

def intreverse(n):
    val = ''
    while n > 0:
        a = n%10
        n = n//10
        val = val + str(a)
    return int(val)

print(intreverse(783))
print(intreverse(242789))
print(intreverse(3))