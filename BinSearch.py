def binsearch(A,k,b,c):
    l = (c+b)//2
    #l = a+b//2
    #pivot =  A[l//2]
    if (k==A[l]):
        return l
    elif (A[l] < k):
        return binsearch(A,k,l+1,c)
    elif (A[l]>k):
        return binsearch(A,k,b,l-1)
    return -1


A= [1,2,3,4,5,6,8,9]
k=8
r = len(A)-1
print(binsearch(A,k,0,r))
