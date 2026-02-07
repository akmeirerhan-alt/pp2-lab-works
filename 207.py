n=int(input())
arr=list(map(int,input().split()))
maxim=arr[0]
maxpos=0
for i in range(n):
   if arr[i]>maxim:
      maxim=arr[i]
      maxpos=i

print(maxpos+1)