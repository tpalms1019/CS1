'''
Author: Teddy Palmer
Date: 3/29/24
Description: The code below allows the user to experience ordering at a french restaurant that gives you random full course meals.
Challenges (not sure exactly what you count as challenge or not so there may be some missing or may be some that aren't challenges and I didn't realize): Full course meals meaning I have a more parallel lists, use of try-except, use of sys.exit, included pricing for meals, included total cost of all meals, ensure user enters a number, ensures user enters a reasonably number, the fantastic french theme (not really a challenge)
Bugs: None found
Sources: Ms. Marciano
'''

import sys # brings in the sys library for reference
import random # brings in the random library for use of random functions

starter_dish = ["Baked Camembert", "Pork Rillettes", "Crab Fondue", "Chicken Terrine", "Puff Pastry Wreath with Brie", "Scallops", "Salmon Canapes", "Escargot", "Gougere", "Potato Salad", "Pate", "Cheese Souffle"] # makes a list of starter dishes parallel to the other below lists
main_dish = ["Beef Bourguignon", "Ratatouille", "Croque Madame", "Salmon en Papillote", "Bouillabaisse", "Steak Frites", "Pot-au-feu", "Meuniere", "Chicken Fricassee", "Duck Confit", "Steak Tartare", "Cassoulet"] # makes a list of main dishes parallel to the other below lists
side_dish = ["Green Beans Almondine", "Petits Pois à la Française", "French Tomato Mustard Tart", "Vichy Carrots", "Warm French Goat Cheese Salad", "Provençal Vegetable Tian", "Pommes Frites", "Potatoes au Gratin", "French Lentil Salad ", "Provence-Style Tomatoes", "Lyonnaise Potatoes", "Cherry Tomato Gratin"] # makes a list of side dishes parallel to the other below lists
dessert = ["Plum Galette", " Chocolate Mousse", "Chocolate Tart", "Millefeuille", "Cherry and Chocolate Bûche de Noël", "Mango-Basil Vacherin", "Cream Puffs with Chocolate Sauce", "Apricot Pâte de Fruit", "Macarons", "Fresh Raspberry Tart", "Alain Ducasse's Gougères", "Vanilla–Brown Butter Sablé Cookies"] # makes a list of desserts parallel to the other below lists
cost_main_dish = [62, 43, 56, 53, 57, 61, 63, 59, 47, 54, 51, 60] # makes a list of costs of main dishes parallel to the other below lists


print("Hello. I am your waiter Francis.") # displays text

print("") # displays text for spacing to improve user experience

while True: # infinite loop while condition True is true
    while True: # infinite loop while condition True is true
        try: # allows for system to try code looking for certain values
            menu_count = int(input("This restaurant is against the concept of choosing what food you want, so how many full course meals will you be ordering today? ")) # sets menu_count as a variable equal to the response of the question and ensures input is an integer 
            break # manually breaks while loop
        except ValueError: # if the 'try' finds an error then do following code
            print("I'm sorry. I don't understand what you mean. Please provide me a number.") # display text

    print("") # displays text for spacing to improve user experience
    
    if menu_count > 10:  # if menu_count is greater than 10, following code will happen
        print("I simply do not believe that you will eat that much food. Provide me a lower number please. ") # displays text
    elif menu_count < 1:  # if menu_count is less than 1, following code will happen
        print("Then why are you here. Leave.") # displays text
        sys.exit() # directly ends the code
    else: # otherwise following code will happen
        print("Fantastic I will get your order to you right away.") # displays text
        break # manually breaks while loop

print("") # displays text for spacing to improve user experience

total_cost = 0 # sets total_cost equal to 0

print("I will now list off your meals in order starting with the starter dish, then the main dish followed by the side dish, and finally the dessert. I will also let you know the cost of each meal at the end.") 

print("") # displays text for spacing to improve user experience

for i in range(menu_count): # goes through each element in menu_count and does following code for each
    print(f"Your starter is {random.choice(starter_dish)}") # displays a random element from list starter_dish along with other text using f string
    dish = random.choice(main_dish) # sets variable dish equal to a random element from list main_dish
    print(f"Your main dish is {dish}") # displays text from variable dish along with other text using f string
    print(f"Along side your main dish is {random.choice(side_dish)}") # displays a random element from list side_dish along with other text using f string
    print(f"And for dessert you will be having {random.choice(dessert)}") # displays a random element from list dessert along with other text using f string
    print(f"The cost is ${cost_main_dish[main_dish.index(dish)]}.") # displays the cost of the main dish from list cost_main_dish along with other text using f string
    total_cost += cost_main_dish[main_dish.index(dish)] # adds cost of main dish to total_cost
    print("") # displays text for spacing to improve user experience

print("Enjoy!") # displays text 
print("") # displays text for spacing to improve user experience
print("[After eating]") # displays text 
print(f"The total cost of your meals was ${total_cost}. We already charged you. I hope you enjoyed your time here.") # displays value of list total_cost using an f string


