# try..except

try:
    print("Enter phone number (only  numbers):")
    phone=input()
    phone = int(phone)
    print(phone)
except ValueError:
    print(ValueError)    