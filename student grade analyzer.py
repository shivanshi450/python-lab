def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"

# Example usage
marks = int(input("Enter marks (0-100): "))
grade = calculate_grade(marks)
print("Grade:", grade)