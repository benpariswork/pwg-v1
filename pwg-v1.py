

### PWG - Password Generator V1
## By: Ben Paris


## Import Libraries

# String helps python piece together our password.
import string

# Secrets provides our password with cryptographically secure numbers.
import secrets



## Script

# Ask user for desired password length.
print("PWG - Welcome to the Password Generator.")
print("PWG - Please provide an integer from 1-99.") 
length= input("PWG - How long would you like your password to be?  ") 

# Test the user's input to see if it is an integer.
if length.isdigit():
    # Define length as an integer.
    length = int(length)

    # Test length to see if it is within the defined range (1-99)
    if length in range(1, 100):

        # Define 'alphabet' with letters and numbers making it alphanumeric. 
        alphabet = string.ascii_letters + string.digits

        # Create secure alphanumeric password.
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        # Display the password to the user.
        print("PWG - Thank you for using the Password Generator. Please feel free to use it however you see fit.")
        print("PWG - PASSWORD: " + password)

    else:

        # Printer Error message if length is NOT an integer.
        print("PWG - ERROR - Invalid Input. Please provide an integer from 1-99.")

else: 
    print("PWG - ERROR - Invalid Input. Please enter an integer.")
    