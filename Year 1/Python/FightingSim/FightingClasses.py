class Fighter:
    def __init__(self, name, power, enemy_power):
        self.__name = name
        self.__power = power

    def set_fighter_name(self, name):
        self.__name = name
    def get_fighter_name(self):
        return self.__name

    def set_power(self, power):
        self.__power = power
    def get_power(self):
        return self.__power

    def attack(self, power, enemy_power):
        self.__power = power
        self._enemy_power = enemy_power
        
# The game continues until one fighter's attack power is greater than the other, and the corresponding fighter is declared the winner.
# Players input their names and power levels, then they take turns attacking each other. The attack power is calculated based on the player and enemy power levels.

def main():
    print("Welcome to the Fighter Game!")
    name = input("Enter your fighter name: ")
    enemy_name =input("Enter the name of the enemy fighter: ")
    result = False

    while result == False:
        try:
            power = int(input("Enter your fighter's power level: "))
            enemy_power = int(input("Enter your enemy fighter's power level: "))

            print(f'{name}, your power level is {power}.')
            print(f'{enemy_name} has a power level of {enemy_power}.')
    
            player_power = Fighter(name, power, enemy_power)

            action = input("Type 'attack' to attack: ")
            
            while action.lower() != 'attack':
                print("Please attack.")
                action = input("Type 'attack' to attack: ")

            if action.lower() == 'attack':
                print(f'{name} attacks {enemy_name} with {power} power!')
                print(f'{enemy_name} attacks {name} with {enemy_power} power!')
                if power > enemy_power:
                    print(f'{name} wins!')
                    result = True
                elif enemy_power > power:
                    print(f'{enemy_name} wins!')
                    result = True
                elif power == enemy_power:
                    print('It is a tie! Fight again!')
                    result = False    
                else:
                    print("Please type attack next time.")
        except ValueError:
            print("Please input an integer.")
            
        
if __name__ == '__main__':
    main()

