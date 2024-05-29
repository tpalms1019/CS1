'''
Author: Teddy Palmer
Date: 5/15/24
Description: the code below allows the user to create, alter and access lists of websites, usernames and passwords
Challenges:
    Allow the user to retroactively add more usernames and passwords
    Allow the user to change usernames and passwords
    Generate a secure password for the user
    Check how complex/secure the passwords are
    Ensure user doesn't try to change password or use other functions without having a password already
Bugs: None found
Sources: Ms. Marciano, Mr. Abonto, Caleb (for the idea of having a sort of 'menu')
'''

import sys
import random

websites = []
usernames = []
passwords = []

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
numbers = "0123456789"
special_characters = "!@#$%^&*?"



def add_password():
    while True:
        random_or_chosen = str.lower(input('''
1: Randomly generated secure password
2: Your own password
3: Quit

Please enter choice: '''))

        if random_or_chosen == "1":
            new_website = str.lower(input("Enter website: "))
            new_username = input("Enter username: ")
            new_password = ""
            for i in range(random.randrange(15, 26)):   # for each integer in random range from 15-25 inclusive             
                new_password += random.choice(characters)  # randomly adds characters from characters to new_password
            print(f"Password: {new_password}")
            break
        elif random_or_chosen == "2":
            new_website = str.lower(input("Enter website: "))
            new_username = input("Enter username: ")

            while True:
                new_password = input("Enter password: ")

                number_count = 0
                special_character_count = 0
                
                if len(new_password) < 8:  # if the length of the password is less than 8
                    print("Password must have 8 or more characters for security.")
                else:
                    for character in new_password: # for each character in new_password
                        if character in numbers:
                            number_count += 1
                    if number_count < 3: #  if there is less than 3 numbers found in new_password
                        print("Password must have atleast 3 numbers.")
                    else:
                        for character in new_password:  # for each character in new_password
                            if character in special_characters:
                                special_character_count += 1
                        if special_character_count < 1:  # if there is less than 1 special character in new_password
                            print("Password must have atleast 1 special character.")
                        else:
                            break
            break
        elif random_or_chosen == "3":
            break
        else:
            print("Please enter the number representing the choice.")

    websites.append(new_website)  # adds new_website to websites
    usernames.append(new_username)  # adds new_username to usernames
    passwords.append(new_password)  # adds new_password to passwords

'''
def add_password():
    Function description: allows user to add a website, username, and password to the lists, this password can be randomly generated or self selected
    Appends:
        new_website to websites
        new_username to usernames
        new_password to passwords
'''

def change_password():
    while True:
        website = str.lower(input("Enter website or 'quit' to quit: "))

        if website in websites:
            new_username = str.lower(input("Enter new username: "))

            while True:
                new_password = input("Enter password: ")

                number_count = 0
                special_character_count = 0
                
                if len(new_password) < 8:  # if the length of the password is less than 8
                    print("Password must have 8 or more characters for security.")
                else:
                    for character in new_password: # for each character in new_password
                        if character in numbers:
                            number_count += 1
                    if number_count < 3: #  if there is less than 3 numbers found in new_password
                        print("Password must have atleast 3 numbers.")
                    else:
                        for character in new_password:  # for each character in new_password
                            if character in special_characters:
                                special_character_count += 1
                        if special_character_count < 1:  # if there is less than 1 special character in new_password
                            print("Password must have atleast 1 special character.")
                        else:
                            break
            usernames[websites.index(website)] = new_username  # updates the old username in usernames with new username using index of the website
            passwords[websites.index(website)] = new_password  # updates the old password in passwords with new password using index of the website
            break
        elif website == "quit":
            break
        else:
            print("Please enter a website in the list.")
        
'''
def change_password():
    Function description: allows user to change the username and password for a website

    Updates:
        Username and password in respective lists

'''
    
def access_password():

    while True:
        website = str.lower(input("Enter website you want the username and password to or 'quit' to quit: "))

        if website in websites:
                    print(f"Username: {usernames[websites.index(website)]}, Password: {passwords[websites.index(website)]}") # prints the parallel value of website in websites from passwords and usernames
        elif website == "quit":
            break
        else:
            print("Enter website or 'quit' to quit")
         
'''
def access_password():
    Function description: allows user to find the username and password for a website

    Prints:
        Username and Password
'''                


def print_list():            
    for i in range(len(websites)):  # for every integer in the length of the list websites
        print(f"website: {websites[i]}, username: {usernames[i]}, password: {passwords[i]}") # print each parallel element from lists.

'''
def print_list():
    Function description: prints list of websites along with their respective username and password

'''


def main():

    while True:
        choice = str.lower(input('''
1: Add password
2: Change Password
3: Access password
4: Password list
5: Exit

Please enter choice: '''))

        if choice == "1":
            add_password()
        elif choice == "2":
            if len(websites) < 1:  # doesn't allow user to do this option without first having one website, username, and password
                print("No password inputed yet. Please add password.")
            else:
                change_password()
        elif choice == "3":
            if len(websites) < 1: # doesn't allow user to do this option without first having one website, username, and password
                print("No password inputed yet. Please add password.")
            else:
                access_password()
        elif choice == "4":
            if len(websites) < 1: # doesn't allow user to do this option without first having one website, username, and password
                print("No password inputed yet. Please add password.")
            else:
                print_list()
        elif choice == "5":
            sys.exit()
        else:
            print("Please enter the number representing the choice.")



main()
    
    
