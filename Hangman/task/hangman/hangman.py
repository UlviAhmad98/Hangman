class Hangman:

    def __init__(self):
        self.words = ["python", "java", "swift", "javascript"]
        self.victory_count = 0
        self.lost_count = 0

    def play(self):    
        import random
        generator = random.choice(self.words)
        hidden_word = list("-" * len(generator))
        letters = set(generator)
        attempts = 8
        suggested_letters = []
        while attempts > 0:
            print("".join(hidden_word))
            entry = input("Input a letter: ")
            if len(entry) != 1:
                print("Please, input a single letter.")
            elif entry.isdigit() or entry.isupper() or not entry.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif entry.isalpha() and entry.islower() and len(entry) == 1:
                for i in range(len(generator)):
                    if generator[i] == entry:
                        hidden_word[i] = entry
                if entry not in letters:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                elif entry in suggested_letters:
                    print("You've already guessed this letter.") 
                print()
                suggested_letters.append(entry)
            if "-" not in hidden_word:
                print(f"You guessed the word {generator}!")
                print("You survived!")
                self.victory_count += 1
                break
            elif attempts == 0:
                print()
                print("You lost!")
                self.lost_count += 1

    def results(self):
        print(f"You won: {self.victory_count} times")
        print(f"You lost: {self.lost_count} times")

    def gameset(self):
        print("H A N G M A N")
        while True:
            print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
            player_input = input()
            if player_input == "play":
                self.play()
            elif player_input == "results":
                self.results()
            elif player_input == "exit":
                exit()
            else:
                pass


hangman = Hangman()
hangman.gameset()
