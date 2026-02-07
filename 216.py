n=int(input())
a=list(map(int,input().split()))
newbie=[]
for i in range(n):
   if a[i] not in newbie:
      print("YES")
      newbie.append(a[i])
   else:
      print("NO")