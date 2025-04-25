#Question: Write a function that checks if a number is even or odd.
#Even number: One that is divisible by 2
#Odd Number: One that is not divisible by 2

def even_or_odd_number(num):
    if num % 2 == 0 :
        #Will check if the number has a reminder of 0 when divided by 2
        print(f"{num} is even!")
    else:
        #If the conditional is not true,the print statement will run
        print(f"{num} is odd!")
        
even_or_odd_number(21)
#Expected output: 21 is odd