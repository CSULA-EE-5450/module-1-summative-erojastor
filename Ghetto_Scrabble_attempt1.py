import random
from english_words import english_words_lower_set


LETTER_VALUES = {"a": 1,
                 "b": 3,
                 "c": 3,
                 "d": 2,
                 "e": 1,
                 "f": 4,
                 "g": 2,
                 "h": 4,
                 "i": 1,
                 "j": 1,
                 "k": 5,
                 "l": 1,
                 "m": 3,
                 "n": 1,
                 "o": 1,
                 "p": 3,
                 "q": 10,
                 "r": 1,
                 "s": 1,
                 "t": 1,
                 "u": 1,
                 "v": 4,
                 "w": 4,
                 "x": 8,
                 "y": 4,
                 "z": 10,
                 " ": 0}


class Tile:
    """
    Each tile has a letter and number value

    """
    def __init__(self, letter, letter_values):
        self.letter = letter.lower()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        return self.letter

    def get_score(self):
        return self.score


class Box:
    """
    Creates the box with all the tiles (100 total) that will be used in the game.
    Has 98 letters and two blank tiles worth 0 points
    """

    def __init__(self):
        self.box = []
        self.initialize_box()

    def add_to_bag(self, tile, quantity: int):
        """
        Adds a certain quantity of a certain tile to the bag
        :param tile: tile
        :param quantity: quantity
        :return:
        """
        for i in range(quantity):
            self.box.append(tile)

    def initialize_box(self):
        """
        adds the default 100 tiles into the box
        """
        global LETTER_VALUES
        self.add_to_bag(Tile("a", LETTER_VALUES), 9)
        self.add_to_bag(Tile("b", LETTER_VALUES), 2)
        self.add_to_bag(Tile("c", LETTER_VALUES), 2)
        self.add_to_bag(Tile("d", LETTER_VALUES), 4)
        self.add_to_bag(Tile("e", LETTER_VALUES), 12)
        self.add_to_bag(Tile("f", LETTER_VALUES), 2)
        self.add_to_bag(Tile("g", LETTER_VALUES), 3)
        self.add_to_bag(Tile("h", LETTER_VALUES), 2)
        self.add_to_bag(Tile("i", LETTER_VALUES), 9)
        self.add_to_bag(Tile("j", LETTER_VALUES), 9)
        self.add_to_bag(Tile("k", LETTER_VALUES), 1)
        self.add_to_bag(Tile("l", LETTER_VALUES), 4)
        self.add_to_bag(Tile("m", LETTER_VALUES), 2)
        self.add_to_bag(Tile("n", LETTER_VALUES), 6)
        self.add_to_bag(Tile("o", LETTER_VALUES), 8)
        self.add_to_bag(Tile("p", LETTER_VALUES), 2)
        self.add_to_bag(Tile("q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("r", LETTER_VALUES), 6)
        self.add_to_bag(Tile("s", LETTER_VALUES), 4)
        self.add_to_bag(Tile("t", LETTER_VALUES), 6)
        self.add_to_bag(Tile("u", LETTER_VALUES), 4)
        self.add_to_bag(Tile("v", LETTER_VALUES), 2)
        self.add_to_bag(Tile("w", LETTER_VALUES), 2)
        self.add_to_bag(Tile("x", LETTER_VALUES), 1)
        self.add_to_bag(Tile("y", LETTER_VALUES), 2)
        self.add_to_bag(Tile("z", LETTER_VALUES), 1)
        self.add_to_bag(Tile(" ", LETTER_VALUES), 2)
        random.shuffle(self.box)

    def take_from_box(self):
        """
        Takes a tile from the box and returns it to the user.
        :return: returns tile to the user
        """
        return self.box.pop()

    def get_remaining_tiles(self):
        """
        :return: returns the number of tiles left in the box
        """
        return len(self.box)


class Hand:
    def __init__(self, box):
        """
        Initializes the player's hand.
        :param box: where the tiles come from
        """
        self.hand = []
        self.box = box
        self.initialize_hand()

    def add_to_hand(self):
        self.hand.append(self.box.take_from_box())

    def initialize_hand(self):
        for _ in range(7):
            self.add_to_hand()

    def get_hand_string(self):
        return ", ".join(str(item.get_letter()) for item in self.hand)

    def get_hand_array(self):
        return self.hand

    def remove_from_hand(self, tile):
        """
        Removes a tile from the hand
        :param tile: tile played
        """
        self.hand.remove(tile)

    def get_hand_length(self):
        return len(self.hand)

    def restock_hand(self):
        while self.get_hand_length() < 7 and self.box.get_remaining_tiles() > 0:
            self.add_to_hand()


class Player:
    def __init__(self, box):
        self.name = ''
        self.hand = Hand(box)
        self.score = 0

    def player_name(self, name):
        self.name = name

    def get_player_name(self):
        return self.name

    def get_hand_str(self):
        return self.hand.get_hand_string()

    def get_hand_array(self):
        return self.hand.get_hand_array()

    def increase_score(self, increase):
        self.score += increase

    def get_score(self):
        return self.score


class Word:
    def __init__(self, word, player):
        self.word = word.lower()
        self.player = player

    def check_word(self):

        blank_tile = ''
        needed_tiles = ''
        dictionary = english_words_lower_set

        if self.word not in dictionary:
            return "word is not valid\n"

        if ' ' in self.word:
            while len(blank_tile) != 1:
                blank_tile = input('Enter a letter for the blank tile')

        for letter in needed_tiles:
            if letter not in self.player.get_hand_string() or \
                    self.player.get_hand_string.count(letter) < needed_tiles.count(letter):
                return "You don't have the tiles for this word\n"

    def calculate_word_value(self):
        word_score = 0
        for letter in self.word:
            word_score += LETTER_VALUES[letter]

        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word.upper()

    def get_word(self):
        return self.word


class Game:
    pass


if __name__ == '__main__':
    Game().run()
