# Function to calculate bonus
def calculate_bonus(salary, experience):
    if experience >= 10:
        bonus = salary * 0.20
    elif experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    
    return bonus

# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(1, n + 1):
    print(f"\nEmployee {i}:")
    salary = float(input("Enter salary: "))
    experience = int(input("Enter years of experience: "))
    
    bonus = calculate_bonus(salary, experience)
    print("Bonus:", bonus)