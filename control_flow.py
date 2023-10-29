# If-elif-else statement
print("\n")

print("#If-elif-else statement : ")
a = ''
b = ''
if a:
    print(a)
elif b:
    print(b)
else:
    print("Number not available")

print("\n")

# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

# for statement
print("#for statement : ")
words = ['cat','window','home']

for w in words:
    print(w,len(w))

print("\n")

# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

# range function
print("#range function : ")
for i in range(5):
    print(i)

print("\n")

print(list(range(5,10)))

print("\n")

print(list(range(1,10,2)))

print("\n")

print(list(range(-1,-10,-2)))

print("\n")

print(sum(list(range(5))))

print("\n")
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

# break and continue Statements, and else Clauses on Loops
print("#break statement : ")

for n in range(2,10):
    for i in range(2,n):
        if n%i==0:
            print(str(n) + " is not a prime number")
            break
    else:
        print(str(n)+ " is a prime number")

# Continue statement 
print("#continue statement : ")

for  n in range(2,10):
    if n%2 == 0:
        print("Found an even number ",n)
        continue
    print("Found an odd number ",n) 

# Pass statement 
print("#pass statement : ")

while True:
    pass

print("\n")
# +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+