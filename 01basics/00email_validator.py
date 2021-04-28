from validate_email import validate_email

mails = ['sudharsan8921@gmail.com','dfsafas3@gmail.com','unexistedmail@gmail.com']
for mail in mails:
    is_valid = validate_email(email_address=mail, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10, smtp_debug=False)
    if is_valid :
        print(f'{mail} is a valid mail')
    else:
        print(f'{mail} is not a valid mail')