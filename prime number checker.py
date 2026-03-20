# Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Input
num = int(input("Enter a number: "))

# Using if-else to display result
if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")