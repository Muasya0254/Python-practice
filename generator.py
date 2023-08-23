# Generators
# A generator is a function that produces a sequence of results instead of a single value.

# Generator functions are distinguished from regular functions in that they use the yield keyword instead of return.
print("Generator Functions")

def countdown():
    k=5
    while k>0:
        yield k
        k-=1

for i in countdown():
    print(i)

# Fibonacci Sequence
# The Fibonacci sequence is a classic use case for generators in Python. The sequence itself is defined as a recursive formula that takes the sum of the two previous numbers to generate the next one.

print("Fibonacci Sequence")

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i>100:
        break
    print(i)