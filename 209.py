n=int(input())
arr=list(map(int,input().split()))
maxim=max(arr)#find maximum
mini=min(arr)#find minimum
for i in range(n):
    if arr[i]==maxim:
        arr[i]=mini 
for i in range(n):
       print(arr[i],end=" ")
