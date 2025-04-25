#Question three: Write a function that computes the factorial

#Factorial function:
def factorial(num):
    #Will ensure that zero is not input
    if num < 0 :
        print("You cannot get the factorial of negative number.")

    #If we intiliaze it as 0,we will get 0 as the ultimate value
    result = 1
    
    #Will multiply the number given from 1 till its own value
    #We put n+1 because the range method ignores the "end" value
    for i in range (1,num+1):
        #This will multiply and store the values as they are multiplied
        result*= i
    return result

number = 5
TestResult=factorial(number)

print(f"The factorial of {number} is: {TestResult}")
