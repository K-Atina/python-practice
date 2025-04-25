#Question: Write a function to sum all elements in a list

#We define the list
list_of_numbers=[5,6,7,8]

#We then define the function
def sum_of_elements(elementList):
    #Will sit the varaiable sum to zero
    sum = 0
    #Introduces a "for loop" to loop through all elements adding them
    for element in elementList:
        sum += element
    #Will return the sum of all elements
    return sum

print(f"The sum of all the numerical elements in this list is: {sum_of_elements(list_of_numbers)}")