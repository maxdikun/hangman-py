import random


class WordChooser:
    def __init__(self, filename: str) -> None:
        with open(filename, "rt") as file:
            self.data = file.read().split("\n")
            if len(self.data) < 0:
                raise RuntimeError("File doesn't contain words")

    def choose(self) -> str:
        c = random.randint(0, len(self.data) - 1)
        return self.data[c]


class HangmanGame:
    def __init__(self, word: str) -> None:
        self.word = word
        self.used = dict()
        self.limit = len(set(word)) // 2
        self.mistakes = 0

    def increment(self, letter: str) -> None:
        if self.status() != "PLAYING":
            return

        right = letter in self.word
        self.used[letter] = right
        if not right:
            self.mistakes += 1

    def status(self) -> str:
        if self.mistakes == self.limit:
            return "DEFEAT"
        elif all([x in self.used for x in list(self.word)]):
            return "VICTORY"
        else:
            return "PLAYING"


def print_state(game: HangmanGame) -> None:
    def mask(letter: str) -> str:
        return letter if letter in game.used else "*"

    masked_word = "".join(map(mask, game.word))
    print(f"WORD IS: [{masked_word}]\t\t{game.mistakes}:{game.limit}")


def run_game(word: str) -> None:
    game = HangmanGame(word)
    while game.status() == "PLAYING":
        print_state(game)
        letter = input("Input:")
        if len(letter) != 1:
            print("Should enter only one letter")
            continue
        game.increment(letter)
    else:
        if game.status() == "VICTORY":
            print(f"You've won!The word was: {word}")
        else:
            print(f"You've lost! HAHHAHA! The word was: {word}")


def main() -> None:
    word_chooser = WordChooser("words.txt")

    while True:
        user_input = input("Do you want to play hangman?(y/n)")
        if user_input == "y":
            run_game(word_chooser.choose())
        elif user_input == "n":
            break
        else:
            print("I did not understand, what you've answered")


if __name__ == "__main__":
    main()
