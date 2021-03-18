"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_cubes, add_mult)


# Replace this with your code


#get the user input
#if input == q, exit loop 
#tokenize the input
#check if operand equals a certain value
#pass the numbers through the equation that the operand suggests
#assign the eqaution to a variable and print the variable

#accept user input


while True:
    user_expression = input("Enter your equation!")
    if user_expression != "q":
        tokenized_input = user_expression.split(' ')
    

        if tokenized_input[0] == "+" :
            print (tokenized_input)
            result = add(tokenized_input)

        if tokenized_input[0] == "-" :
            result = subtract(tokenized_input)

        if tokenized_input[0] == "*":
            result = multiply(tokenized_input)
        
        if tokenized_input[0] == "/":
            result = divide(tokenized_input)
        
        if tokenized_input[0] == "%":
            result = mod(tokenized_input)

        if tokenized_input[0] == "squared":
            result = square(tokenized_input)
        
        if tokenized_input[0] == "cubed":
            result = cube(tokenized_input)

        if tokenized_input[0] == "power":
            result = power(tokenized_input)
        
        if tokenized_input[0] == "add_prod":
            result = add_mult(tokenized_input)

        if tokenized_input[0] == "sum_cubes":
            result = add_cubes(tokenized_input)
        
    elif user_expression =="q":
        break
            
    print (result)
    


