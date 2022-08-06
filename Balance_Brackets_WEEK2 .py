# Matched Value

def matched(s):
    
    l = []
    
    for i in range(len(s)):
        if s[i] == '(':
            l.append(s[i])
        elif s[i] == ')':
            try:
                l.pop()
            except:
                pass
            
    if len(l) == 0:
        return True
    return False

print(matched("zb%78"))
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))