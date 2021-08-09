import hangman


class hangman_window:

    def input_number(self):
        x = str(input("enter letters only: "))[0].lower()
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if x in letters:
            print(f"{x} is a valid letter.")
        else:
            print(f"{x} is not a valid letter.")

    def run_game(self):
        h = hangman.Hangman()
        print(h.word)
        for i in range(len(h.word)):
            print("_", end="")


hangman_window().input_number()
hangman_window().run_game()
