f=open("Lecture 03b_ControlStructure_Solutions.ipynb","r")
data=f.read()
print(data)
print(type(data))

# never forget to close the file
f.close()
# "r "-> ka matlab reading hota hai ye sirf file ko read krta hai 
# "w"->yeh file ko over write krnw mai kaam aattaa hai ,
#  pehle sara data file ka delete ho jaata haai aur fir over write hota hai
# "a"->append,ye file ko open karega aur file ki last se write krna shuru karega
# "b"->binary mode, to open a binary file , 
# hume agar binary ko rad  krna haai to rb likhna hoga , lekin t likhne ki jarurt nhi hoti
# "+"->to read and write both in a file
# "t"->for txt file
