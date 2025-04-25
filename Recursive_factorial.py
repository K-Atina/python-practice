#Question Five: Write a function to calculate a factorial(recursive)
def factorial_recursive(num):
    #This will check if the "num" is either zero or one
    if num == 1 or num == 0:
        #returning 1 to stop the code
        return 1
    else:
        #multiplies the current number by the factorial of the number minus one, using recursion.
        # It will break down the calculation into smaller parts until reaching the base case.
        return num * factorial_recursive(num - 1)
    
print(factorial_recursive(5))
    