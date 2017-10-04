# Sequence Alignment
#X=['A','T','G','C','C']
#Y=['T','A','C','G','C','A']
#result is 17

delta={}

delta[('-','A')]=-5
delta[('-','T')]=-5
delta[('-','C')]=-5
delta[('-','G')]=-5
delta[('A','-')]=-5
delta[('T','-')]=-5
delta[('C','-')]=-5
delta[('G','-')]=-5

delta[('A','A')]=10
delta[('A','C')]=-1
delta[('A','G')]=-3
delta[('A','T')]=-4

delta[('C','A')]=-1
delta[('C','C')]=7
delta[('C','G')]=-5
delta[('C','T')]=-3

delta[('G','A')]=-3
delta[('G','C')]=-5
delta[('G','G')]=9
delta[('G','T')]=0

delta[('T','A')]=-4
delta[('T','C')]=-3
delta[('T','G')]=0
delta[('T','T')]=8

# Answer:
X=['G', 'C', 'A', 'T', 'G', 'C']
Y=['G', 'A', 'T', 'T', 'A', 'C', 'A']
ADNsequence(X, Y, delta)

X1=['A','T','G','C','C']
Y1=['T','A','C','G','C','A']
ADNsequence(X1, Y1, delta)
#maxscore=17

X2=['C','A','T']
Y2=['C','A','T']
# maxscore=25
ADNsequence(X2, Y2, delta)

X3=['C','A','T','C','A','T']
Y3=['A','T','C','A','T','C']
# maxscore=33
ADNsequence(X3, Y3, delta)


def ADNsequence(X, Y, delta):
    #initialize
    bestScores={}
    m=len(X)
    n=len(Y)
    bestScores[0,0]=0
    #base case
    for i in range(1, m+1):
        bestScores[i, 0]=delta[(X[i-1],'-')]+bestScores[i-1, 0]
    for j in range(1, n+1):
        bestScores[0, j]=delta[('-',Y[j-1])]+bestScores[0, j-1]
    #code
    for i in range(1, m+1):
        for j in range(1, n+1):
            U=delta[(X[i-1], Y[j-1])]+bestScores[i-1,j-1]
            V=delta[("-", Y[j-1])]+bestScores[i,j-1]
            W=delta[(X[i-1], "-")]+bestScores[i-1,j]
            bestScores[i, j]=max(U, V, W)
    return bestScores[m,n]