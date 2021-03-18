"""CLI application for a prefix-notation calculator."""
from functools import reduce

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


def convert_to_int(input_list):
    num=[]
    for i in range(1,len(input_list)):
        try: 
            num.append(int(input_list[i]))
        except:
            return False
    return num



while True:
    user_expression = input("Enter your equation!")
    if user_expression != "q":
        tokenized_input = user_expression.split(' ')

        split_list = convert_to_int(tokenized_input)

        if split_list : 

            if tokenized_input[0] == "+" :
                result = reduce(add,split_list)

            elif tokenized_input[0] == "-" :
                result = subtract(split_list)

            elif tokenized_input[0] == "*":
                result = multiply(split_list)
            
            elif tokenized_input[0] == "/":
                result = divide(split_list)
            
            elif tokenized_input[0] == "%":
                result = mod(split_list)

            elif tokenized_input[0] == "squared":
                result = square(split_list)
            
            elif tokenized_input[0] == "cubed":
                result = cube(split_list)

            elif tokenized_input[0] == "power":
                result = power(split_list)
            
            elif tokenized_input[0] == "add_prod":
                result = add_mult(split_list)

            elif tokenized_input[0] == "sum_cubes":
                result = add_cubes(split_list)
            
            else:
                print("Invalid operand, please pick again!")
        
            try:
                if result:
                    print(result)
                result=None
            except: 
                pass
        else :
            print("Invalid input, please enter valid integer values!")

    elif user_expression =="q":
        break
    
  


   
    


