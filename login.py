# Login Module

# Default Username and Password
username = "admin"
password = "1234"

login_status = False


# Welcome Function
def welcome():
    print("\nSMART CAMPUS MANAGEMENT SYSTEM")
    print("====== LOGIN PAGE ======")
    print("Welcome to Smart Campus Management System")


# Retry Function
def retry():
    print("Please try again.")


# Login Function
def login():
    global login_status

    entered_username = input("Enter Username: ")
    entered_password = input("Enter Password: ")

    # Check for empty inputs
    if entered_username == "":
        print("Username cannot be empty.")
        return

    if entered_password == "":
        print("Password cannot be empty.")
        return

    # Validate Login
    if entered_username == username and entered_password == password:
        login_status = True
        print("\nLogin Successful")
        print("Access Granted")
    else:
        login_status = False
        print("\nInvalid Username or Password")
        print("Access Denied")
        retry()

    print("Status:", login_status)
    print("--------------")
    print("Thank You")


# Main Program
welcome()
login()










































































































































































































































































































if entered_username == username and entered_password == password:
printf("Login Succesful")


































































