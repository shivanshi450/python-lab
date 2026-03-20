def login():
    correct_username = "admin"
    correct_password = "1234"
    
    attempts = 0
    
    while attempts < 3:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            print("Invalid credentials")
            attempts += 1
    
    print("Account Locked")

# Call the function
login()