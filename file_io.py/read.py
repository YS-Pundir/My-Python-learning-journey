# data =f.read(n) ->this will read first n words at a time
# data =f.readline()-> reads one line at a time
file=open("ram.txt","r")
ch=file.read(5)#will read first 5 char only
print(ch)

# pata nhi kyu lekin agar pehle jo charachter maine read karwa liye hai 
# , unhe mai radline mai line ke sath read nhi kr pa raaha hu
# because the cusor niche aa gay hai , aur wo fir hume same read nhi krke de skta .
# uske liye hume file ko close krke dubara open krna hoga
line1=file.readline()
print(line1)

file.close