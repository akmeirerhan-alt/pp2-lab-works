n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=pow(a[i],2)
    print(a[i],end=" ")