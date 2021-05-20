from dotenv import load_dotenv
# pip install python-dotenv
import os
load_dotenv()

domain = os.getenv('DOMAIN')
print(domain)

password = os.getenv('PASSWORD')
print(password)
