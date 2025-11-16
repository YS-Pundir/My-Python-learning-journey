def check_prime():
    n=int(input("enter any number->",))
    for i in range(2,n):
        if(n%i==0):
            print("the number is not prime")
            return
        else:
            print("the number is prime")
            break

check_prime()

