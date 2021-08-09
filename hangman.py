import random


class Hangman:
    """ Starts the game and runs it."""

    word: str
    log_inputs:set[str] = set()
    correct_inputs: set[str] = set()
    false_inputs: set[str] = set()
    game_ended: bool = False
    win_condition: bool = False
    tries_remaining: int = 9

    def __init__(self):
        with open('words.txt', 'r') as f:
            content = f.readlines()

            self.word = random.sample(content, 1)[0][0:-1]

    def register_user_input(self, input) -> None:

        self.log_inputs.add(input)

        if input in self.word:
            self.correct_inputs.add(input)
        elif input not in self.false_inputs:
            self.tries_remaining -= 1
            self.false_inputs.add(input)

    def check_game_status(self) -> bool:

        finished_word = True
        for char in self.word:
            if char not in self.correct_inputs:
                finished_word = False

        if finished_word:
            self.win_condition = True
            self.game_ended = True
            return self.game_ended

        if self.tries_remaining == 0:
            self.win_condition = False
            self.game_ended = True
            return self.game_ended

        return self.game_ended


if __name__ == '__main__':
    h = Hangman()

