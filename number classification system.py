# Function to check number properties
def check_number(num):
    # Check Positive / Negative / Zero
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")
    
    # Nested if for Even / Odd
    if num != 0:   # optional check (0 भी even होता है)
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
    else:
        print(num, "is Even")  # 0 is even

# Taking list input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Using for loop to process all numbers
for n in numbers:
    check_number(n)
    print("-----")