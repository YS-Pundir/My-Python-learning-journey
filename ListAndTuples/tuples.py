# tuples are used , because it is immutable .
#   hence can not be changed
tup=(2,3,1,4,5,)

print(tup[0])
print(type(tup))
print(tup[1:3])
# tup.index(el) -- return index of first accuarance 
# tup.count(el)  -- erturns the no times thaat number appears 
print(tup.index(4))