

def mult_matr(a,b):
    ra=len(a)
    ca=len(a[0])
    rb=len(b)
    cb=len(b[0])
    if ca==rb:
        r=[[0 for _ in range(cb)] for _ in range(ra)]
        for row in range(ra):
            for col in range(cb):
                for j in range(ca):
                    r[row][col]+=a[row][j]*b[j][col]
        return r            
    else:
        return None
        
# nn,mm=tuple(map(int,input().split(' ')))
# a=[]
# for i in range(nn):
#     a.append(list(map(int,input().split(' '))))
 
# input()  
 
# mm,kk=tuple(map(int,input().split(' ')))
# b=[]
# for i in range(mm):
#     b.append(list(map(int,input().split(' '))))

a = [[1, 2], [2, 1]]
b = [[2, 1], [1, 2]]
    
r=mult_matr(a,b)
print(*r, sep='\n')