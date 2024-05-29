'''
Author: Teddy Palmer
Date: 11/14/23
Description: Code that simulates the Magic 8 Ball experience by letting them ask yes or no questions.
Challenges: str.lower, while True loop, words list used to determine if the input for question is a yes-or-no question
Bugs: None
Sources: Ms. Marciano
'''


import random # brings in the random library for reference

print("Hello") # displays text

# infinite loop while condition True is true
while True:
    day = str.lower(input("How was your day? ")) # sets 'day' as a variable equal to the response of the question
    if day == "good" or day == "fine" or day == "great":  # if day is good, fine, or great, following code will happen
        print("That's swell.") # displays text
        break # manually breaks while loop
    elif day == "bad" or day == "not good": # otherwise if day is bad or not good, following code will happen
        print("That's too bad.") # displays text
        break # manually breaks while loop
    else: # if day is not one of the above options then this code happens
        print("Invalid input. please input 'good', 'bad', or 'fine'") # displays text

# creates list of answers to questions asked   
answers = ["Yes", "No", "Perhaps", "Maybe", "The time will come where the answer reveals itself.", "Never ask such a dastardly question.", "Ask again later."]

print("Now that the formalities are completed. Let's get to it.") # displays text

words = ["is", "has", "does", "do"] # creates a list of words

# infinite loop while condition True is true
while True:
    # sets 'question' as a variable equal to the response of the question
    question = str.lower(input("I, the magic 8 Ball, will answer any yes-or-no question you ask. So, what is your question? (to quit enter 'quit') "))

    if question == "quit": # if 'question' is quit, following code will happen
        print("Thank you for your time. Hopefully I have been of some assistance.") # displays text
        break # manually breaks while loop
    elif any(word in question for word in words): # otherwise if 'question' contains any string from list 'words' then this code will happen
        print(random.choice(answers)) # displays a random answer from list answers
    else: # if 'question' is not one of the above options then this code happens
        print("Please enter a yes-or-no question or 'quit'!") # displays text
                
