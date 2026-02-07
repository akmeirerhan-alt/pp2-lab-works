n=int(input())
for i in range(32):# enough for 32-bit integers
   if n==pow(2,i):
      print("YES")
      break
else:
      print("NO")