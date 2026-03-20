# Input for number of rows
rows = int(input("Enter number of rows: "))

# Loop to print triangle pattern
for i in range(1, rows + 1):
    # Check even or odd row
    if i % 2 == 0:
        char = "*"
    else:
        char = "#"
    
    # Print pattern
    for j in range(i):
        print(char, end=" ")
    
    print()  # Move to next line