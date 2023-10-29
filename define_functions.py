# Define function
def fib(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b = b, a+b
        
# Call function
fib(9)