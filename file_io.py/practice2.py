# sear if the word "learning " exsist in the file or not 

def check_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

check_word()