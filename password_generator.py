import random
import string    # to grab all lowerand upper letters and special characters

def generate_password(min_length,numbers=True,special_characters=True):
    letters= string.ascii_letters
    digits= string.digits
    special = string.punctuation

    characters =letters      # letters are to be taken for sure
    if numbers:                    # if numbers are to be taken the add them to characters
        characters += digits
    if special_characters:         # if special_charcaters to be taken then add them to characters 
        characters += special

    pwd= ""          #stores the password
    meets_criteria = False    # currently we dont meet the criteria
    has_number = False         # do not have number
    has_special = False        # do not have special

    while not meets_criteria or len(pwd) < min_length: # while we are not meeting the criteria (if we dont have a number or dont have a special character) or the length of password is not yet equal to or greater than min length
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits :
            has_number= True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:                  #if we should include a number then set meet_criteria to if we have a number or not .so we do have a number its going to be true if we dont then false
            meets_criteria = has_number
        if special_characters:       # if we should include special character the meet_criteria should be equal to meet_criteria and has special 
            meets_criteria = meets_criteria and has_special      # and is used beacause if meet_criteria for numbers is False then this also becomes false as if we dont meet the criteria(if number is needed but it dont meet the criteria ) then it also becomes false


    return pwd

min_length = int(input("enter minimum length:"))
has_number = input("Do you want to have numbers (y/n)?") == 'y'
has_special = input("Do you want to have special charcters (y/n)?") == 'y'
pwd=generate_password(min_length,has_number,has_special)
print("password is :",pwd)
"""
print("password with number and special character:")
pwd1=generate_password(10) 
print(pwd1)
print()

print("password without number and special character:")
pwd2=generate_password(10,False,False) 
print(pwd2)
print()

print("password without number:")
pwd3=generate_password(10,False) 
print(pwd3)
print()

print("password without  special character:")
pwd4=generate_password(10,True,False) 
print(pwd4)
"""