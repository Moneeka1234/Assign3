# calcuate factorial using function

def fact(x):
    if x<2:
        return 1
    else :
        return x * fact(x-1)

x=5    
factorial = fact(x)
print("Factorial of " + str(x) + " is :", factorial)