# A function is a code that runs only when you call it

# Example 1

def greet(): #def <function_name>():
    print("How are you doing?")

greet() # to invoke the code and run it, need to write this code.




def say_hi():
    print("hi")

# Won't run until we call it out






# Parameters and Arguements

def greetings(name): #name is a parameter, we can change the name of the parameter to anything we want, it is just a placeholder for the argument that we will pass in when we call the function.
    print(f"Hello, {name}")


greetings("Advait") # "Advait" is an argument, we can change the argument to anything we want and it will work.

# Parameter is an empty box.
# Argument is the value that we put in the box.

# Multiple parameters

# Calculate a price of a product whose unit is 300rs, and quantity is 3.

def calculate_price(unit_price, quantity):
    total_price = unit_price * quantity
    print(total_price)

calculate_price(300, 3) # 300 is the unit price and 3 is the quantity. 


