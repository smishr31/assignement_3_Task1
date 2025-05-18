def fact(n):
    if(n<2):
        return 1
    else:
        return n * (fact(n-1))
n = int(input("Enter Number: "))
result = fact(n)
print(f"The Factorial of the given number is {result}")
