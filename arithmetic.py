"""Functions for common math operations."""

def convert_to_int(input_list):
    num=[]
    for i in range(1,len(input_list)):
        num.append(int(input_list[i]))
    
    return num


def add(user_expression):
    """Return the sum of the two inputs."""
    # define a variable "sum"
    # set this variable as the sum of num1, num2. sum = num1+num2
    # return sum
    sum = 0
    num = convert_to_int(user_expression)
    for i in range (0,len(num)):
        sum = sum + num[i]
    return sum

def subtract(user_expression):
    """Return the second number subtracted from the first."""
    #def variable for subtract
    #set subtract variable to find difference between two numbers
    #return subtract variable
    
    num = convert_to_int(user_expression)
    difference = num[0]
    for i in range (1,len(num)):
        difference = difference-num[i]
    return difference


def multiply(user_expression):
    """Multiply the two inputs together."""
    #define variable for result
    #save result of num1 multiplied by num2
    #return result

    num = convert_to_int(user_expression)
    product = 1
    for i in range (0,len(num)):
        product = product * num[i]
    return product

def divide(user_expression):
    """Divide the first input by the second and return the result."""
    #define function for divide
    #add quotient variable that divides num1 and num2
    #return quotient
    num = convert_to_int(user_expression)
    print(num)
    return num[0]/num[1]


def square(user_expression):
    """Return the square of the input."""
    #define variable for square
    #save result of squaring to the variable
    #return result [squared]
    num = convert_to_int(user_expression)
    return num[0] ** 2

def cube(user_expression):
    """Return the cube of the input."""

    #define variable for a cube
    #take num1 to the third power
    #return the cube variable
    num = convert_to_int(user_expression)
    return num[0]**3


def power(user_expression):
    """Raise num1 to the power of num2 and return the value."""
    #define variable for result
    #save result of num1 raised to num2 into result
    #return result

    num = convert_to_int(user_expression)
    return num[0] ** num[1]

def mod(user_expression):
    """Return the remainder of num1 / num2."""

    #define remainder variable
    #capturn remainder when num1 / num2
    #return remainder variable

    num = convert_to_int(user_expression)
    return num[0] % num[1]


# define function add_mult with 3 parameters
# add num1 and num2, multiply the result with num3
# return the final result

def add_mult(user_expression):
    """ Return the sum of num 1 + num2 multiplied by num3"""
  

    num = convert_to_int(user_expression)
    equation = (num[0] + num[1]) * num[2]
    return equation 

#define function add_cubes with 2 parameters
#define vaiable that takes the cubes of num1 and num2 and adds them together
#return the sum of the cubes save in that variable

def add_cubes(user_expression) :
    """ Return the sum of cubes."""
    num = convert_to_int(user_expression)
    sum_cubes = (num[0]**3) + (num[1]**3)
    return sum_cubes