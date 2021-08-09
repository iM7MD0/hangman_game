import hangman


class hangman_window:
    h = hangman.Hangman()
    def input_number(self):

        letters = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            x = str(input("enter letters only: "))[0].lower()
            if x in letters:
                print(f"{x} is a valid letter.")
                self.h.register_user_input(input=x)
                print(self.h.log_inputs)
                print(self.h.correct_inputs)
                print(self.h.tries_remaining)
                continue
            else:
                print(f"{x} is not a valid letter.")


    def run_game(self):
        for i in range(len(self.h.word)):
            print("_", end="")
        print(len(self.h.word))

hangman_window().run_game()
hangman_window().input_number()

