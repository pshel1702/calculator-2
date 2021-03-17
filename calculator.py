"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


#get the user input
#if input == q, exit loop 
#tokenize the input
#check if operand equals a certain value
#pass the numbers through the equation that the operand suggests
#assign the eqaution to a variable and print the variable

#accept user input

user_expression = input("Enter your equation!")

while user_expression!="q" :
    tokenized_input = user_expression.split(' ')

    if tokenized_input[0] == "+" :
        result = add(int(tokenized_input[1]),int(tokenized_input[2]))
    
    print (result)
    break

    


