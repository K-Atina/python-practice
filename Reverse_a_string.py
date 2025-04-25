#Question Four : Write a function to reverse a string without using built-in methods

#We can convert the string into a list of elements,loop in reverse then join the reversed elements back into the string form

intial_string="COMPUTER"

def reverse_the_string(str):
    #We first convert the string to a list
    element_list=list(str)
    
    #We create an empty list to store the individual characters we will reverse
    reversed_element_list = []
    
    #We loop "element_list" in reverse order
    #The first (-1) lets the loop know we satrt from the last character
    #The second (-1) will stop at the first element
    #The third(-1) specifies the step in this case telling it move in reverse
    for i in range(len(element_list)-1,-1,-1):
        #Will append the reversed elements to the new list
        reversed_element_list.append(element_list[i])
        
    #We then change it from elements to a full string
    reversed_string =''.join(reversed_element_list)
    
    return reversed_string

print(reverse_the_string(intial_string))
        
        

