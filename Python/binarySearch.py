︠def BinarySearch(A,x):
    n=len(A)
    if n <= 2:
        if A[0]==x or A[1]==x:
            return True
        else:
            return False
    else:
        m=n//2
        if A[m]==x:
            return True
        else:
            LeftA=A[0:m]
            RightA=A[m:n]
            if A[m]<=x:
                return BinarySearch(RightA, x)
            if A[m]>x:
       
def BinarySearch(A,x):
    n=len(A)
    if n <= 2:
        if A[0]==x or A[1]==x:
            return True
        else:
            return False
    else:
        m=n//2
        if A[m]==x:
            return True
        else:
            LeftA=A[0:m]
            RightA=A[m:n]
            if A[m]<=x:
                return BinarySearch(RightA, x)
            if A[m]>x:
                return BinarySearch(LeftA, x)

BinarySearch(A49261, 123)