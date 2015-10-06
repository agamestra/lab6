N=int(input())
A = list(map(int, input().split()))
P=0
for i in range (N):
    if (A[i]==5):
        P=P-1
    else:
        P=P+(A[i]-5)/5
print (int(P))