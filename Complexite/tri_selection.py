def tri_selection(L) : 
    n = len(L)
    while n!=0 : 
        j = 0
        min = L[j] 
        for i in range(j + 1, n) :
            if min > L[i] :
                min = L[i]
        tmp = L[j] 
        L[j] = min  
        L[n-1] = tmp
        j = j + 1
        n -= 1
    return L 
            
#Main 

L= [2,8,1,5,6,4,8,1]
L = tri_selection(L)
print(L)