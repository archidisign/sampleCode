︠
def Merge1(A,B):
    nA=len(A)
    nB=len(B)
    merged=[]
    for i in range(nA+nB):
        if A!=[] and B!=[]: #until both are empty, DO:
            minA=min(A) # min(A) yields the smallest element in A in Theta(nA) time.
            minB=min(B) # min(B) yields the smallest element in B in Theta(nB) time.
            # compare and append
            if minA<minB:
                A.remove(minA) # A.remove(minA) removes minA from array A in constant time.
                merged.append(minA) # merged.append(minA) appends minA to the end of array merged in constant time.
            else:
                B.remove(minB)
                merged.append(minB)
        elif A==[]:
            minB=min(B)
            B.remove(minB)
            merged.append(minB)
        else:
            minA=min(A)
            A.remove(minA)
            merged.append(minA)
    return merged
def Merge2(A,B):
    nA=len(A)
    nB=len(B)
    merged=[]
    indA=0
    indB=0
    for i in xrange(nA+nB):
        #finish going through A
        if indA==nA:
            merged.append(B[indB])
            indB+=1
        #finish going through B
        elif indB==nB:
            merged.append(A[indA])
            indA+=1
        #A is smaller so append this one first
        elif A[indA]<B[indB]:
            merged.append(A[indA])
            indA+=1
        else:
            merged.append(B[indB])
            indB+=1
    return merged


n=100
A=[2*i for i in range(n)]
B=[2*i+1 for i in range(n)]

Merge1(A,B)


n=100
A=[2*i for i in range(n)]
B=[2*i+1 for i in range(n)]

Merge2(A,B)