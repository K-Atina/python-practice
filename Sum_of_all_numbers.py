number=1234

def sum_of_digits(num):
    sum = 0
    #We initilize the sum to 0
    
    #While loop to loop till the number is 0
    while num > 0:
        # % returns the reminder
        #That means if we "modulo" 124 by 10 ,the value return will be 4
        value = num % 10
        
        #We will added the extracted value to sum
        sum += value
        
        #We then need to remove the last digit.
        #Going by the last example,we'll need to remove 4
        num = num // 10
        #This will divide the number by 10 then drop the decimal part
    return sum
#Lastly we return the sum

print(sum_of_digits(number))