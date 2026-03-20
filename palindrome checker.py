# Function to check palindrome
def is_palindrome(value):
    s = str(value)   # Convert number/string to string
    start = 0
    end = len(s) - 1
    
    # Using while loop
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Input from user
data = input("Enter a number or string: ")

# Using if-else to print result
if is_palindrome(data):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")