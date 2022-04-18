import re
p= input("Input your password:\n")
x = True
while x:  
    if (len(p)<14):
        print("Sorry, but your password contains less than 14 characters. Please try again")
        break
    elif not re.search("[a-z]",p):
        print("Sorry, but your password does not contain at least one lowercase letter. Please try again.")
        break
    elif not re.search("[0-9]",p):
        print("Sorry, but your password does not contain at least one number. Please try again.")
        break
    elif not re.search("[A-Z]",p):
        print("Sorry, but your password does not contain at least one uppercase letter. Please try again.")
        break
    elif re.search("\s",p):
        print("Sorry, but your password  contain the space. Please try again.")
        break
    elif not re.search("[$#@%,.;:*^&!?})\\\({>~<|?/`'\"\[\]]",p):
        print("Sorry, but your password does not contain at least one punctuation character. Please try again.")
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")