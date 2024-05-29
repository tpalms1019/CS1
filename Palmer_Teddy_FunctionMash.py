'''
Author: Teddy Palmer
Date: 4/23/24
Description: The code below creates and runs a variety of functions through one main function.
Challenges: Used try except to do integer function, made a function that takes a string and reverses it, made a function that checks if a word is a palindrome, made a function that takes in a name of any length and returns initials, made a function that asks the user what number sided die they want to roll and prints a random number from the given range 
Bugs: None found
Sources: Ms. Marciano, Mr. Abonto
'''


import random  # brings in the random library for use of random functions

alphabet = ["a", "b", "c", "d", "e"]  # creates list of letters in alphabet

def chorus():  # defines function that prints chorus of a song
    print("I used to hear a simple song")
    print("That was until you came along")

def symphony():  # defines function that prints a line of a song
    print("And now I hear a symphony")

def song():  # defines function that prints the lyrics to a song
    chorus()  # executes chorus function
    print("Now in it's place is something new")
    print("I hear it when I look at you")
    print()
    print("With simple songs I wanted more")
    print("Perfection is so quick to bore")
    print("You are more beautiful by far")
    print("Our flaws are who we really are")
    print()
    chorus()  # executes chorus function
    print("You took my broken melody")
    symphony() # executes symphony function
    print("Ah-ah oh-ooh-oh ah-ah")
    print()
    symphony()  # executes symphony function
    print()

def add(num1, num2):  # defines function that takes 2 numbers and adds them
    print(num1 + num2)

def print_list(list1):  # defines function that takes a list and prints every element in that list individually
    for element in list1:  # goes through each element in list1 and does following code for each
        print(element)

def element_in_list(list1, element1):  # defines function that takes a list and an element and returns a boolean determined by whether the element is in the list
    if element1 in list1:
        return True   # gives function value 'True'
    else:
        return False   # gives function value 'False'

def integer(number):  # defines function that takes in a parameter and returns a boolean determined by whether that parameter is an integer
    try:  # allows for system to try code looking for certain values
        number = int(number)   # makes the string 'number' an integer
        return True  # gives function value 'True'
    except ValueError:  # if the 'try' finds an error then do following code
        return False  # gives function value 'False'

def random_number():  # defines function that prompts the user for two numbers and prints a random number between the two.
    while True:  # infinite loop while condition True is true
        num1 = input("Enter num1: ")
        num2 = input("Enter num2: ")

        if integer(num1) and integer(num2):  # if both numbers are integers
            if int(num1) + 1 >= int(num2):  # then check if number 1 plus 1 is greater than number to
                print("The first number needs to be less than the second, and you need there to be an integer in between them.")
            else:  # otherwise
                print(random.randrange(int(num1) + 1, int(num2)))
                break  # ends while loop
        else:  # otherwise
            print("Invalid. Please input integers.")

def replace_letters(word, letter1, letter2):  # defines function that takes a string and two characters, then replaces every instance in the string of the first character with the second
    updated_word = ""  # sets up new variable as string.
    for letter in word: # goes through each letter in word and does following code for each
        if letter == letter1:  # if the letter is the letter in the word then
            updated_word += letter2  # add the other letter to updated_word
        else:  # otherwise
            updated_word += letter  # add the same letter to updated_word
 
    return updated_word  # gives the function the value of updated_word

def reverse(word):  # defines function that takes a string and reverses it
    reversed_word = ""  # sets up new variable as string.
    for letter in word:  # goes through each letter in word and does following code for each
        reversed_word = letter + reversed_word  # adds letter to the beginning of reversed_word

    return reversed_word  # gives the function the value of reversed_word

def palindrome(word):  # defines function that takes a string and checks whether it's a palindrome
    if word == reverse(word):
        return True   # gives function value 'True'
    else:
        return False   # gives function value 'False'

def initials(full_name):  # defines function that takes a name and returns the initials, regardless of amount of names in full name
    initials = ""  # sets up new variable as string.
    all_names = full_name.split()  # splits a sentence string into word strings
    for name in all_names:  # goes through each name in all_names and does following code for each
        initials += name[0]  # adds the first letter to initials

    return initials  # gives the function the value of initials

def roll_dice():  # defines function that asks user for a number of sides for a die and prints random number in range of die
    while True:  # infinite loop while condition True is true
        total_sides = input("Enter a number of sides for a dice roll: ")

        if integer(total_sides):  # if integer function returns 'True'
            print(f"You rolled a {random.randint(1, int(total_sides))}")
            break  # ends infinite loop
        else:  # otherwise
            print("Invalid. Please input an integer")
            

def main():  # defines function that executes all functions
    song()  # executes song function
    add(5, 11)  # executes add function
    print_list(alphabet)  # executes print_list function
    print(element_in_list(alphabet, "a"))  # displays value returned from element_in_list
    print(element_in_list(alphabet, "s"))  # displays value returned from element_in_list
    number = input("Enter number: ")
    print(integer(number))  # displays value returned from integer 
    random_number()  # executes random_number function
    print(replace_letters("hello", "l", "w"))  # displays value returned from replace_letters
    print(reverse("hello"))   # displays value returned from reverse
    print(palindrome("racecar"))   # displays value returned from palindrome
    print(initials("Teddy Palmer"))   # displays value returned from initials
    roll_dice()  # executes roll_dice function
    
main()  # executes main function
