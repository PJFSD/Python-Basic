x=("apple","banana","cherry") #original tuple befor update
y=list(x) #Convert to list
y[1]="kiwi" #Change the list
x =tuple(y) #Convert to tuple

print(x) #print Update Tuple