import copy

x=[1]
x.append(x)
print(x)

y=copy.deepcopy(x)
print(y)

y=x

print(y)
# x==y
# print(x)