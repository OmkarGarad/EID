import random
 
def generate_random_32_digit_number():
    while True:
        # Generate a random 32-digit number
        number = random.randint(10**31, 10**32 - 1)
        
        # Adjust to ensure the remainder is 1 when divided by 97
        adjustment = (97 - (number % 97)) + 1
        number += adjustment
        
        # Ensure the number is still 32 digits long after adjustment
        if len(str(number)) == 32:
            return number
 
def check_remainder(number, divisor):
    return number % divisor
 
# Generate the number
number = generate_random_32_digit_number()
 
# Check the remainder when divided by 97
remainder = check_remainder(number, 97)
 
# Get the length of the generated number
length_of_number = len(str(number))
 
print(f"Generated number: {number}")
print(f"Length of generated number: {length_of_number}")
print(f"Remainder when divided by 97: {remainder}")import random
 
def generate_random_32_digit_number():
    while True:
        # Generate a random 32-digit number
        number = random.randint(10**31, 10**32 - 1)
        
        # Adjust to ensure the remainder is 1 when divided by 97
        adjustment = (97 - (number % 97)) + 1
        number += adjustment
        
        # Ensure the number is still 32 digits long after adjustment
        if len(str(number)) == 32:
            return number
 
def check_remainder(number, divisor):
    return number % divisor
 
# Generate the number
number = generate_random_32_digit_number()
 
# Check the remainder when divided by 97
remainder = check_remainder(number, 97)
 
# Get the length of the generated number
length_of_number = len(str(number))
 
print(f"Generated number: {number}")
print(f"Length of generated number: {length_of_number}")
print(f"Remainder when divided by 97: {remainder}")