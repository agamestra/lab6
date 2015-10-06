N=int(input())
flag=0
A = list(map(int, input().split()))
for i in range (0,N-2):
    for j in range (0,N-1):
        if i == j:
            continue
        if A[i]==A[j]:
            print(A[i])
            flag=1
            break
    if (flag==1):
        break
