f=open("ram.txt","w")
f.write("namaste dosto , to kya haal hai ap sab ke ")
f.close()

f=open("ram.txt","a")
f.write("\nasha hai ki aap sab thik thak honge ")
f.close()

# for write and  append , if the file does not exist then it will be automatically created
m=open("sample.txt","w")
m.write("hum ha jail te bhage hoe most wanted\nto bs humte darka rahe karo")
m.close