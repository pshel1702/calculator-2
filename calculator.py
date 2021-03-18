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
        num1 = int(tokenized_input[1])
       
        if len(tokenized_input) == 2:
            num1 = int(tokenized_input[1])
        elif len(tokenized_input) == 3:
            num1 = int(tokenized_input[1])
            num2 = int(tokenized_input[2])
        if len(tokenized_input) == 4:
            num1 = int(tokenized_input[1])
            num2 = int(tokenized_input[2])
            num3 = int(tokenized_input[3])   
        

        if tokenized_input[0] == "+" :
            result = add(num1,num2)

        if tokenized_input[0] == "-" :
            result = subtract(num1,num2)

        if tokenized_input[0] == "*":
            result = multiply(num1,num2)
        
        if tokenized_input[0] == "/":
            result = divide(num1,num2)
        
        if tokenized_input[0] == "%":
            result = mod(num1,num2)

        if tokenized_input[0] == "squared":
            result = square(num1)
        
        if tokenized_input[0] == "cubed":
            result = cube(num1)

        if tokenized_input[0] == "power":
            result = power(num1,num2)
        
        if tokenized_input[0] == "add_prod":
            result = add_mult(num1,num2,num3)

        if tokenized_input[0] == "sum_cubes":
            result = add_cubes(num1,num2)
        
    elif user_expression =="q":
        break
            
    print (result)
    


