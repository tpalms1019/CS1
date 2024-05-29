
'''
Author: Teddy Palmer
Date: 11/6/23
Description: The code below simulates and narrates a morning routine with interactive choices.
Challenges: Use of time variable and having it update throughout changing the experience dependent on choices made by the user, use of while loop,
str.lower making the user's input lowercase so that it works with the if statements, use of elif and else for the user to have other choices and to tell them
if the input is invalid and to try again through the while loop, while loops within if statements.
Bugs: None
Sources: Ms. Marciano, Mr. Abanto
'''

# starts story by displaying two messages
print("Alarm!")  
print("Time reads 0700 hours")

# sets variable time at 700 which will be used to let user know the time depending on responses
time = 700

# infinite loop while condition True is true
while True:
    snooze = str.lower(input("Do you want to snooze the alarm? ")) # sets snooze as a variable equal to the response of the question and converts it to lower case" with the str.lower

    if time >= 730: # if time variable is greater than or equal to 730 
        print("Wake up! You're late! ") # then display text 
        break  #manually breaks while loop
    if snooze == "yes" or snooze == "sure":  # if snooze is yes, ye, or sure, following code will happen
        print("Go back to sleep") # displays text depending on if if statement happens
        time += 10  # adds 10 to variable time
        print("Alarm! It is 0"+str(time))  # concatenates 0 and variable time as a string
    elif snooze == "no": # otherwise if snooze is no
        print("Wake up!") # displays text depending on if elif statement happens
        break  #manually breaks while loop
    else: # if snooze is not one of the above options then this code happens
        print("Invalid, yes or no answer please. ") # displays text depending on if else statement happens

# infinite loop while condition True is true
while True:
    brush_teeth = str.lower(input("Do you want to brush your teeth? ")) # sets brush_teeth as a variable equal to the response of the question and converts it to lower case" with the str.lower

    if brush_teeth == "ok" or brush_teeth == "yes" or brush_teeth == "sure":  # if brush_teeth is yes, ok, or sure, following code will happen
        print("Great you have decent hygiene. ") # displays text depending on if if statement happens
        time += 5 # adds 5 to time variable
        break  #manually breaks while loop
    elif brush_teeth == "no": # otherwise if brush_teeth is no
        print("You're terrible. Fine do what you want. ") # then display text depending on if elif statement happens
        break  #manually breaks while loop
    else: # if brush_teeth is not one of the above options then this code happens
        print("Invalid, yes or no answer please (I will judge you if you say no). ") # displays text depending on if else statement happens

if time >= 730:  # if time variable is greater than or equal to 730
    while True: # Then go through infinite loop while condition True is true
        shower = str.lower(input("It is 0"+str(time)+". You are late. If you want to shower, you better do it as fast as you can. ")) # sets shower as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if shower == "ok" or shower == "yes" or shower == "sure": # if shower is yes, ok, or sure, following code will happen
            print("Awesome, take a really short shower, make it quick. ") # displays text depending on if if statement happens
            time += 5
            break  #manually breaks while loop
        elif shower == "no": # otherwise shower is no, following code will happen
            print("That's fair. You are pretty late. ") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if shower is not one of the above options then this code happens
            print("Invalid, yes or no answer please. ") # displays text depending on if else statement happens
else: # otherwise following code happens
    while True: # infinite loop while condition True is true
        shower = str.lower(input("It is 0"+str(time)+". If you want to shower, you can. ")) # sets shower as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if shower == "ok" or shower == "yes" or shower == "sure": # if shower is yes, ok, or sure, following code will happen
            print("Awesome, take a shower. ") # displays text depending on if if statement happens
            time += 10
            break  #manually breaks while loop
        elif shower == "no":  # otherwise shower is no, following code will happen
            print("You lazy bum. Get on with it then. ") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if shower is not one of the above options then this code happens
            print("Invalid, yes or no answer please. ") # displays text depending on if else statement happens
            

if time >= 740: # if time variable is greater than or equal to 740
    while True: # Then go through infinite loop while condition True is true
        shirt_length = str.lower(input("You are late. it is 0"+str(time)+". What are you wearing today for a shirt, short or long sleeved? ")) # sets get_dressed_shirt as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if shirt_length == "short": # if get_dressed_shirt is short, following code will happen
            print("Great. Short-sleeved is a good pick.") # displays text depending on if if statement happens
            break  #manually breaks while loop
        elif shirt_length == "long":  # otherwise get_dressed_pants is long, following code will happen
            print("Great. long-sleeved is a good pick.") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if get_dressed_shirt is not one of the above options then this code happens
            print("Invalid, please answer with 'short' or 'long'") # displays text depending on if else statement happens
else: # otherwise following code happens
    while True: # infinite loop while condition True is true
        shirt_length = str.lower(input("What are you wearing today for a shirt, short or long sleeved? ")) # sets get_dressed_shirt as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if shirt_length == "short": # if get_dressed_shirt is short, following code will happen
            print("Great. Short-sleeved is a good pick though you may get cold.") # displays text depending on if if statement happens
            break  #manually breaks while loop
        elif shirt_length == "long":  # otherwise get_dressed_shirt is long, following code will happen
            print("Great. Long-sleeved is a good pick, but don't complain if you are too hot.") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if get_dressed_shirt is not one of the above options then this code happens
            print("Sorry only two options, please answer with 'short' or 'long'.") # displays text depending on if else statement happens

# infinite loop while condition True is true
while True:
    shorts_or_pants = str.lower(input("Now are you going to wear shorts or pants? ")) # sets get_dressed_pants as a variable equal to the response of the question

    if shorts_or_pants == "shorts": # if get_dressed_pants is shorts, following code will happen
        print("Solid pick. Don't complain when you are cold though.") # displays text depending on if if statement happens
        break  #manually breaks while loop
    elif shorts_or_pants == "pants": # otherwise get_dressed_pants is pants, following code will happen
        print("Solid pick, but don't complain if you aren't comfortable") # displays text depending on if elif statement happens
        break  #manually breaks while loop
    else: # if get_dressed_pants is not one of the above options then this code happens
        print("Sorry only two options, please answer with 'shorts' or 'pants'.") # displays text depending on if else statement happens

time += 2 # adds 2 to time variable

if time >= 740: # if time variable is greater than or equal to 740
    while True: # then go through infinite loop while condition True is true
        breakfast = str.lower(input("It is 0"+str(time)+". You are late. You don't have time for breakfast. Go rush to school. ")) # sets breakfast as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if breakfast == "ok" or breakfast == "yes": # if breakfast is yes or ok, following code will happen
            print("That's great and all but you are still late. Go.") # displays text depending on if if statement happens
            break  #manually breaks while loop
        elif breakfast == "no": # otherwise breakfast is no, following code will happen
            print("I already told you that you do not have time. You made your own decisions which led to you not having time for breakfast. Go to school.") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if breakfast is not one of the above options then this code happens
            print("That doesn't mean anything to me, but you have to go to school, so it doesn't matter. Get a move on.") # displays text depending on if else statement happens
            break  #manually breaks while loop
else: #otherwise following code happens
    while True: # infinite loop while condition True is true
        breakfast = str.lower(input("It is 0"+str(time)+". You have time to eat some food. Sorry but you only have two options: cereal or scrambled eggs. ")) # sets breakfast as a variable equal to the response of the question and converts it to lower case" with the str.lower

        if breakfast == "cereal": # if breakfast is cereal, following code will happen
            print("Great choice. Go to school and try to have good day.") # displays text depending on if if statement happens
            break  #manually breaks while loop
        elif "egg" in breakfast: # otherwise breakfast is eggs, scrambled eggs, or egg, following code will happen
            print("In my opinion cereal is better, but eggs are still a good choice. Go to school and try to have a good day.") # displays text depending on if elif statement happens
            break  #manually breaks while loop
        else: # if breakfast is not one of the above options then this code happens
            print("Only two options: 'cereal' or 'eggs'. Pick one.") # displays text depending on if else statement happens

print("End") # displays text
        


        
