# set is collecction of unique elements
# sets are muttable , but the elements are immutable it means we can add or remove the elements but can not change it
collection={
    1,2,3,4,5,6,7,8
}
print(collection)

# way to write emty set
collection2=set()
collection2.add(1)
collection2.add(3)
collection2.add("yuvraj")
collection2.add((1,2,3,4,5,))#adding the tuple in it

print(collection2)

print("the union of both of this sets ",collection.union(collection2))
print("the intersection  of both of this sets ",collection.intersection(collection2))