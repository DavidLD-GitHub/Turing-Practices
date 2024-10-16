import validators

def main():
    mail = input("What is your email adress?: ")
    validate(mail)

def validate(mail):
    if validators.email(mail):
        print("Valid")
    else:
        print("Invalid")

if __name__== "__main__":
    main()