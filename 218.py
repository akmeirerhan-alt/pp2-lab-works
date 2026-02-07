n=int(input())#read number of strings
string=[] #strings we read
counted={} #dictionary to store first occurance
for i in range(n):
    string.append(input()) #read strings 

for i in range(n):
    if string[i] not in counted:#if string not seen before
        counted[string[i]]=i+1 # store its first position 


for k in sorted(counted):#print in alphabetical order 
    print(k,counted[k])
    
