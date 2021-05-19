# try..except

try:
    print("Enter phone number (only  numbers):")
    phone=input()
    phone = int(phone)
    print(phone)
except ValueError:
    print("Enter only phone numbers!")    

# Python program to handle simple runtime error

a = [1, 2, 3]
try:
	print (f"Second element = {(a[1])}")

	# Throws error since there are only 3 elements in array
	print (f"Fourth element = {(a[3])}")

except IndexError:
	print ("An error occurred")

finally:
    print('This always executes!')

# Raising and Exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
