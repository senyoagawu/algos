def cellsInRange(s):
    l, r = s.split(':')
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_id, r_id =  alpha.index(l[0]),alpha.index(r[0])
    nl, nr = int(l[1]),int(r[1])
    ans = []
    for char in alpha[l_id:r_id+1]:
        for num in range(nl,nr+1):
            ans.append(char + str(num))
    return ans
    
s = "K1:L2"
print(cellsInRange(s))


