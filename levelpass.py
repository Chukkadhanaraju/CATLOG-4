import getpass
import random

def biometric_authentication(fingerprint):
    saved_fingerprint = "DhanaBio"
    if fingerprint == saved_fingerprint:
        return True
    return False

def graphical_password():
    correct_image = random.randint(1, 7) 
    
    print("Select the correct image:")
    for i in range(1, 8):
        print(f"Image {i}")
    
    user_selection = int(input("Enter the image number (1-7): "))
    if user_selection == correct_image:
        return True
    return False

def text_password():
    stored_password = "Dhanaraj1"
    user_password = getpass.getpass("Enter your text password: ")

    if user_password == stored_password:
        return True
    return False

def three_level_password_system():
    print("Welcome to the Three-Level Password System")

    if text_password():
        print("Level 1 Authentication: Success")

        if graphical_password():
            print("Level 2 Authentication: Success")

            user_fingerprint = input("Simulate fingerprint input (e.g., 'fingerprint_123'): ")
            if biometric_authentication(user_fingerprint):
                print("Level 3 Authentication: Success")
                print("Access Granted!")
            else:
                print("Level 3 Authentication: Failed - Access Denied")
        else:
            print("Level 2 Authentication: Failed - Access Denied")
    else:
        print("Level 1 Authentication: Failed - Access Denied")

if __name__ == "__main__":
    three_level_password_system()