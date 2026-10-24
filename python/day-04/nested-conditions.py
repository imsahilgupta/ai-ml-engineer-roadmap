correct_username = "learner"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")