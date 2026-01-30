x="KBTU" #global variable
def myfunc():
    global x #we are taking global variable
    x="University" # x variable is changed to University
myfunc()
print(x,"is where we study")