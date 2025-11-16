with open("ram.txt","r") as f:
    data=f.read()
    print(data)
    # with sytax ke sath close statement ki koi jarurt nhi hoti
with open("ram.txt","w") as  f:
    f.write("hat bsdk")