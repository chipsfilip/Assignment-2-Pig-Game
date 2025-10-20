import random

# holding each players points and name
class Player:

    def __init__(self, name):
        self.high_score = 0 # high score for that specific player, 0 to begin with
        self.name = name

    # add points to the player
    def add_points(self, points_to_add):
        self.high_score += points_to_add

# holding dice-throw
class Dice:
    
    # roll dice between 1-6, return number
    def roll_dice(self):
        return random.randint(1, 6)

# main logic of the game
class Game:

    def __init__(self, players):
        self.players = players
        self.winning_goal = 100
        self.dice = Dice()
        self.current_player_index = 0 # current player's index in the player list (players) begins with 0
        self.how_many_players = len(self.players)

    # returns the current player
    def current_player(self):
        return self.players[self.current_player_index]
    
    # go to the next player in the list of players
    def next_player(self):
        if self.current_player_index + 1 >= self.how_many_players: # go back to the first player in the list
            self.current_player_index = 0
        else: # otherwise increase current player index by 1
            self.current_player_index += 1

    # ask if the person wants to hold or continue rolling, return yes or no
    def hold(self):
        answer = input('Do you want to hold? (enter "y" for yes or "n" for no)').lower() # lower to convert capital Y and N

        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Invalid input, try again.')
            return self.hold() # ask again
        
    
    # do roll_dice function and add return value 2-6 to variable turn_score
    # it it returns 1, make turn_score = 0
    # add dice value to turn_score
    # ask if they want to try again, if yes -> roll dice again, if not -> add turn score to high score
    def turn(self):
        turn_score = 0
        player = self.current_player()

        print(f"It's {player.name}'s turn. Their current high score is: {player.high_score}")

        while True:
            dice_value = self.dice.roll_dice()

            print(f'{player.name} rolled the dice.')

            if dice_value == 1:
                print("It's a 1, you lose your round points.")

                turn_score = 0
                break
            else:
                print(f"It's a {dice_value}")

                turn_score += dice_value

                print(f'The round score is: {turn_score}')

                # ask if they want to hold
                if self.hold():
                    player.add_points(turn_score)
                    print(f'{player.name} holds. Their high score is now: {player.high_score}')
                    break
        
        self.next_player()
    
    # tallying of all peoples high score and checking 
    # if someone has won or not
    def has_won(self):
        for player in self.players:
            if player.high_score >= self.winning_goal:
                print(f'{player.name} was the first to achieve 100 points. {player.name} is the winner of the game. Congratulations!')
                return True
        
        return False
    
    # game loop
    def play_game(self):
        print('The game has started. Welcome to the Pig Dice game!')
        while not self.has_won():
            self.turn()

# main class creating the players + the game, and running the game
class Main: 
    if __name__ == '__main__':
        player_one = Player('Player 1')
        player_two = Player('Player 2')
        game_instance = Game([player_one, player_two])
        game_instance.play_game()