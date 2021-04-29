import random

from phrase import Phrase

class Game():
    
    def __init__(self):
        self.missed = 0
        self.phrases = ['another one bites the dust', 'two birds with one stone', 'texas sized', 'all dressed up with nowhere to go', 'not my first rodeo']
        self.active_phrase = get_random_phrase()
        self.guesses = [" "]
        
    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
    
        