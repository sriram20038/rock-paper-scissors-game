import random

class game:
    #variables
    choices = ['r', 'p', 's']
    player_score = 0
    computer_score = 0
    draw=0    # to know how many games are draw
    

    def __init__(self):
    
        attempts = int(input("Enter the number of attempts you want to play: "))
        #game loop
        while attempts > 0:
            user_input = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
            check=self.check_choice(user_input)
            if(check):
              attempts -= 1
        
        self.show_final_scores()
    
    def check_choice(self, user_input):
        '''
            check and generate computers choice
        '''
        if user_input in self.choices:
            num=random.randint(0,2)
            computer_choice =self.choices[num]
            print("Computer choice is:", computer_choice)
            self.determine_winner(user_input, computer_choice)
            return True
        else:
            print("Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissors.\n\n")
            return False
            
    
    def determine_winner(self, user_input, computer_choice):
        '''
           used to determine the winner based on the computers choice
        '''
        if user_input == computer_choice:
            print("It's a draw!\n")
            self.draw+=1
        elif (user_input == 'r' and computer_choice == 's') or \
             (user_input == 'p' and computer_choice == 'r') or \
             (user_input == 's' and computer_choice == 'p'):
            self.player_score += 1
            print("You won!\n\n")
        else:
            self.computer_score += 1
            print("You lost!\n\n")
    
    def show_final_scores(self):
        print("Your score:", self.player_score)
        print("Computer score:", self.computer_score)
        print("draw games: ", self.draw)
        if self.player_score > self.computer_score:
            print("Congratulations, you won the game!")
        elif self.player_score < self.computer_score:
            print("You lost the game!")
        else:
            print("The game was a draw.")

# Create an instance of the Item class to start the game
g = game()
