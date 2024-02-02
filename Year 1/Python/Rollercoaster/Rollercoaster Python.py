# Importing random for random list picker
import random

# Setting constants
FRIENDLIMIT = 5
FOODRIDELIMIT = 2

# Defining the main function
def main():
    
    # Defining the friends list
    friends_list = []
    
    # Calling the friends() function to add friends into the list
    friends(friends_list)

    # Initializing rides and their correlated ride prices
    ride1 = 'Leviathan'
    ride1_price = 15.00
    ride2 = 'Behemoth'
    ride2_price = 5.00
    ride3 = 'Snoopy Land'
    ride3_price = 25.00
    ride4 = 'Riptide'
    ride4_price = 7.50
    # Putting them into a list so they can be removed by del
    total_rides = [ride1, ride2, ride3, ride4]
    ride_prices = [ride1_price, ride2_price, ride3_price, ride4_price]

    # Initializing foods and their correlated food prices
    food1 = 'Hamburger'
    food1_price = 3.50
    food2 = 'Hotdog'
    food2_price = 2.25
    food3 = 'Pizza'
    food3_price = 8.00
    food4 = 'Caviar'
    food4_price = 500.00
    # Putting them into a list so they can be removed by del
    total_foods = [food1, food2, food3, food4]
    food_prices = [food1_price, food2_price, food3_price, food4_price]

    # Setting empty values in order to use the variable later on
    total_ride_price = 0
    ride_accumulator = 0
    chosen_rides = []

    # Calling (and returning) the rides() function with 5 arguments
    total_ride_price, chosen_rides = rides(ride_accumulator, total_rides, chosen_rides, ride_prices, total_ride_price)
   
    # Setting empty values in order to use the variable later on
    total_food_price = 0
    food_accumulator = 0
    chosen_foods = []

    # Calling (and returning) the foods() function with 5 arguments
    total_food_price, chosen_foods = foods(food_accumulator, total_foods, chosen_foods, food_prices, total_food_price)

    #Adding total trip price by adding rides + foods
    total_trip_price = total_ride_price + total_food_price
    
    # Stating the rides and foods chosen
    print(f'\nYou Chose The Following 2 Rides: {chosen_rides}.')
    print(f'You Chose The Following 2 Foods: {chosen_foods}.')

    # Stating the total costs of all 3: rides, food, both
    print(f'\nThe total cost of your rides is ${total_ride_price}.')
    print(f'The total cost of your food is ${total_food_price}.')
    print(f'The total cost of your entire trip is ${total_trip_price}.')

    # Telling the user they are eligible for a prize if total price > 0
    if total_trip_price > 0:
        print('Congratulations, you are eligibile for a prize!')

    # Calling the random_winner function to determine the winner at random and giving 1 argument of the friends_list
    random_winner(friends_list)

# Function for appending and asking user for friend names
def friends(friends_list):
    friend_index = 1
    # While loop until 5 (5 friends)
    while len(friends_list) != FRIENDLIMIT:
        names = input(f'Please enter friend #{friend_index}: ')
        names_spaces = names.isspace() # Setting T/F value in case no friend has been input
        # If names_space is T, prompt user to put in a valid name
        if names_spaces == True or names == "":
            print("Please put a proper name")
        # Appending items on the friends list
        else:
            friends_list.append(names)
            friend_index += 1

# Function for choosing rides
def rides(ride_accumulator, total_rides, chosen_rides, ride_prices, total_ride_price):

    # While loop until 2 (2 rides chosen)
    while ride_accumulator != FOODRIDELIMIT:
        # Try in case user enters one instead of 1, etc...
        try:
        # User input for which ride
            ride_answer = input(f'\nPlease pick a ride out of the following remaining rides\n'
                                f'\nPrices:\n'
                                '\nLeviathan: $15.00\nBehemoth: $5.00\nSnoopy Land: $25.00\nRiptide: $7.50 \n'
                                f'\nRides Left To Choose: (type 1, 2, 3, 4): {total_rides}: ')
            # In case the user enters an empty value
            ride_spaces = ride_answer.isspace()
            # Checking if the user enters an empty value
            if ride_spaces == True or ride_answer == "":
                print("\nPlease choose a ride in the selection.")
            elif ride_spaces == False:
                ride_number = int(ride_answer)
                # In case user chose 0
                if ride_number == 0:
                    print("\nPlease choose a number from the selection.")
                # Due to index, ride_number - 1 in order to use the proper value
                elif (ride_number-1) < len(total_rides):
                    chosen_rides.append(total_rides[ride_number-1]) # Appending chosen ride into a list
                    del total_rides[ride_number-1] # Deleting the ride selected
                    total_ride_price += ride_prices[ride_number-1] # Adding the ride price of ride selected into a variable
                    del ride_prices[ride_number-1] # Deleting the ride price selected
                    ride_accumulator += 1 # +1 ride selected into the accumulator
                else:
                    print("\nPlease choose a ride in the selection.")
        except ValueError:
            print("\nPlease input a regular integer (1,2,3,4).")
    return total_ride_price, chosen_rides # Returning total_ride_price for total prices and chosen_rides for the deleted but selected rides

# Function for choosing foods 
def foods(food_accumulator, total_foods, chosen_foods, food_prices, total_food_price):
    # While loop until 2 (2 foods chosen)
    while food_accumulator != FOODRIDELIMIT:
        # Try in case user enters one instead of 1, etc...
        try:
            food_answer = input(f'\nPlease pick a food out of the following remaining foods\n'
                                f'\nPrices:\n'
                                '\nHamburger: $3.50\nHotdog: $2.25\nPizza, $8.00\nCaviar: $500.00 \n'
                                f'\nFoods Left To Choose: (type 1, 2, 3, 4): {total_foods}: ')
            # In case the user enters an empty value
            food_spaces = food_answer.isspace()
            # Checking if the user enters an empty value
            if food_spaces == True or food_answer == "":
                print("\nPlease choose a food in the selection.")
            elif food_spaces == False:
                food_number = int(food_answer)
                # In case user chose 0
                if food_number == 0:
                    print("\nPlease choose a number from the selection.")
                # Due to index, ride_number - 1 in order to use the proper value
                elif (food_number-1) < len(total_foods):
                    chosen_foods.append(total_foods[food_number-1]) # Appending chosen food into alist
                    del total_foods[food_number-1] # Deleting the food selected
                    total_food_price += food_prices[food_number-1] # Adding the food price of food selected in a variable
                    del food_prices[food_number-1] # Deleting the food price selected
                    food_accumulator += 1 # +1 food selected into the accumulator
                else:
                   print("\nPlease choose a food in the selection.")
        except ValueError:
            print("\nPlease input a regular integer (1,2,3,4).")
    return total_food_price, chosen_foods # Returning total_food_price for total prices and chosen_foods for the deleted but selected rides

# Function for choosing a random winner
def random_winner(friends_list):
    # Initializing a variable that will pick the list of 5 friends through an index number (0,1,2,3,4)
    random_friend_winner = random.randint(0,4)
    
    # Showing the user who out of their friends won
    print(f'\nCongratulations, {friends_list[random_friend_winner]} has won the prize!')
    
main()
