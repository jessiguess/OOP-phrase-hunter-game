import random
from string import ascii_lowercase

from phrase import Phrase

class Game():
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('another one bites the dust'), Phrase('two birds with one stone'), Phrase('texas sized'), Phrase('all dressed up with nowhere to go'), Phrase('not my first rodeo')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("\n", ("-" * 36), "\n  Welcome to the Phrase Hunter Game!\n", "-" * 36)
        
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print("\nNumber missed: {}".format(self.missed))
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
        self.game_over()
        
        while True:
            try:
                new_game1 = input("Would you like to play again? Type y/n: ").lower()
                if new_game1 != "y" and new_game1 != "n":
                    raise ValueError()
            except ValueError:
                print("Please enter y or n.")
            else:
                if new_game1 == "y":
                    self.new_game()
                    break
                else:
                    print("Goodbye")
                    break
                
        
    def get_guess(self):
        letters = ascii_lowercase
        while True:
            try:
                self.guess = input("\nEnter a letter: ").lower()
                if len(self.guess) < 0 or len(self.guess) > 1:
                    raise ValueError()
                elif self.guess not in letters:
                    raise ValueError()
            except ValueError:
                print("Please choose only one letter.")
            else:
                return self.guess
            
    def game_over(self):
        if self.missed == 5:
            print("\nSorry, you've used all your guesses!\n\n--GAME OVER--\n")
        else:
            print("\n**CONGRATULATIONS**\nYou Win!")
            
    def new_game(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases.remove(self.active_phrase)
        if len(self.phrases) == 0:
            print("Sorry, there are no more phrases to guess :(\nGoodbye!")
        else:
            self.active_phrase = self.get_random_phrase()
            self.start()