global numScores, desiredDistribution, Grades, K, N, M

M=100
numScores={0:0,  1:0,  2:0,  3:0,  4:0,  5:0,  6:0,  7:0,  8:0,  9:0, 
10:0,  11:0,  12:0,  13:0,  14:0,  15:0,  16:0,  17:0,  18:0,  19:0, 
20:0,  21:0,  22:0,  23:0,  24:0,  25:0,  26:0,  27:0,  28:0,  29:0, 
30:0,  31:0,  32:0,  33:0,  34:0,  35:1,  36:2,  37:0,  38:0,  39:0, 
40:0,  41:0,  42:1,  43:2,  44:2,  45:0,  46:0,  47:0,  48:4,  49:1, 
50:1,  51:3,  52:6,  53:3,  54:2,  55:1,  56:4,  57:6,  58:0,  59:1, 
60:2,  61:6,  62:1,  63:1,  64:2,  65:0,  66:2,  67:5,  68:2,  69:0, 
70:4,  71:0,  72:3,  73:1,  74:2,  75:2,  76:2,  77:0,  78:4,  79:6, 
80:1,  81:1,  82:2,  83:1,  84:0,  85:1,  86:0,  87:1,  88:1,  89:3, 
90:1,  91:0,  92:1,  93:1,  94:0,  95:0,  96:0,  97:0,  98:0,  99:0, 
100:1}
N=sum([numScores[i] for i in xrange(M+1)])

K=9
Grades=['D','C','C+','B-','B','B+','A-','A','A+']
desiredDistribution={'D':0.05,'C':0.05,'C+':0.05,'B-':0.05,'B':0.05,'B+':0.5,'A-':0.15,'A':0.09,'A+':0.01}

import copy
def gradeDistributor():
    #initialize
    penalty={}
    cutoff={}
    #base case for the column K-1
    for i in range(K-1,M+1):
        numgrade=sum([numScores[y] for y in range(i,M+1)])
        penalty[i,K-1]=(numgrade-desiredDistribution[Grades[K-1]]*N)^2
        cutoff[i,K-1]=[i]
    #recursively generate our values
    for k in range(K-2,-1,-1):
        for i in range(k,M-K+k+2):
            penalty[i,k]=-1
            for j in range(i+1,M-K+k+3):
                mySum=0
                for x in range(i,j):
                    mySum=mySum+numScores[x]
                if penalty[i,k]<0:
                    penalty[i,k]=(mySum-desiredDistribution[Grades[k]]*N)^2+penalty[j,k+1]
                    cutoff[i,k]=copy.copy(cutoff[j, k+1])
                    cutoff[i,k].insert(0,i)
                elif penalty[i,k]>((mySum-desiredDistribution[Grades[k]]*N)^2+penalty[j,k+1]):
                    penalty[i,k]=(mySum-desiredDistribution[Grades[k]]*N)^2+penalty[j,k+1]
                    cutoff[i,k]=copy.copy(cutoff[j, k+1])
                    cutoff[i,k].insert(0,i)
    return "penalty is %i and cutoff list is: %s" %(penalty[0, 0], cutoff[0,0])
gradeDistributor()
