def solve(a0, a1, a2, b0, b1, b2):
    
    a = 0
    b = 0
    if a0 > b0:
        a=a+1
    elif a0 < b0:
        b=b+1
   
    if a1 > b1:
        a=a+1
    elif a1 < b1:
        b=b+1
        
    if a2 > b2:
        a=a+1
    elif a2 < b2:
        b=b+1
    
    return a, b
    

