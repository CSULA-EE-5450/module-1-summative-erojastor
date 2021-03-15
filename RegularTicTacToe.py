
class Board:
    def __init__(self):
        print('Welcome to TicTacToe')
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def board_display(self):
        print(f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print('---------')
        print(f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print('---------')
        print(f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')

    def update_cell(self, cell_num, player):
        """
        Updates the cell once the player inputs a cell number
        :param cell_num: choices of 1-9, where the player puts their x or o
        :param player: which player is making the move
        """
        if self.cells[cell_num] == ' ':
            self.cells[cell_num] = player
        else:
            print('space already taken')

    def check_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != ' ':
                used_cells += 1

        if used_cells == 9:
            return True
        else:
            return False

    def check_winner(self, player):
        """
        checks the different winning combinations
        :param player: which player is making the move
        :return: if none condition is met, return false
        """

        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True

        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True

        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True

        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True

        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True

        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True

        else:
            return False

    def reset(self):
        self.cells = self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def board_refresh():
    board.board_display()


def main():
    while True:
        board_refresh()
        player_x = int(input('\nPLayer X) Choose a box from 1-9.> '))

        board.update_cell(player_x, 'X')
        board_refresh()
        player_o = int(input('\nPlayer O) Choose a box from 1-9.> '))
        board.update_cell(player_o, 'O')

        if board.check_tie():
            print('\nTie Game\n')
            play_again = input('Would you like to play again? > (Y/N)').upper()
            if play_again == 'Y':
                board.reset()
                continue

        elif board.check_winner('X'):
            print('\nX wins\n')
            play_again = input('Would you like to play again? > (Y/N)').upper()
            if play_again == 'Y':
                board.reset()
                continue

        elif board.check_winner('O'):
            print('\nO wins\n')
            play_again = input('Would you like to play again? > (Y/N)').upper()
            if play_again == 'Y':
                board.reset()
                continue
            else:
                break


if __name__ == '__main__':
    board = Board()
    main()
