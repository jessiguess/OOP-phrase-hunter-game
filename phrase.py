class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for letter in self.phrase:
            if guesses == letter:
                print(f"{letter}", end="")
            else:
                print("_ ")
