
# FUNCTIONS
# def get_cordinates():
#     return 10.20
# x,y=get_cordinates()
# print(x,y)


# exercise1: define a function greet a 
# parameter name, set to guests and print message  
# i am a software programmer

def greet(name="guests"):
    message = "Hello, " + name + "! I am a software programmer."
    print(message)

# Example usage
greet("Alice")
greet()


# returning multiple values
def greet(name="guests"):
    message = "Hello, " + name + "! I am a software programmer."
    return name, message

# Example usage
name, message = greet("Alice")
print(name)    # Output: Alice
print(message) # Output: Hello, Alice! I am a software programmer.

name, message = greet()
print(name)    # Output: guests
print(message) # Output: Hello, guests! I am a software programmer.


def get_name_and_position():
    names = 'iyama'
    position = 'i am a software engineer'
    return names, position

# Get the values from the function
names, position = get_name_and_position()

# Print the values
print(names, position)
print(names, position)



# LAMBDA EXPRESSION
# EXAMPLE 5: CREAT ALAMBDA FUNCTION TO ADD TWO NUMBERS
def add(a,b):return a+b
print(add(45,70))

# example 6:use cases of lambda function for sorting
coordinates=[(1,3),(2,3),(3,1),(5,0)]
coordinates.sort(key=lambda coordinates:coordinates[1])


number_squares=[1,2,3,4,5]

# square=list{map(lambda x:x**2, number_squares)}:
print(squares)


# how to  use kwargs
def def_ahabwe_function(a, b, **kwargs):
    print(f"a: {a}, b: {b}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
def_ahabwe_function("example_a", "example_b", key1="value1", key2="value2")

