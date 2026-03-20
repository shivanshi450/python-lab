# Function to print table
def print_table(num):
    # Check for negative number
    if num < 0:
        print("Please enter a positive number")
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

# Take input from user
number = int(input("Enter a number: "))

# Call function
print_table(number)