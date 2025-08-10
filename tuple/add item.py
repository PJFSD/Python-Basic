x=("apple","banana","cherry")
y=list (x)
y[1] = "mango"

print(x)

y.append("orange")
x=tuple(y)
print(y)