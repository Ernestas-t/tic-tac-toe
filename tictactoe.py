from tkinter import *
import random


class TicTacToe(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic-Tac-Toe')
        self.config(padx=50, pady=50, bg='black')

        self.board = {}
        self.move_count = 0

        self.winner = ''
        self.is_running = True

        self.create_board()

    def check_horizontal(self):
        for row in range(3):
            button_row = []
            for column in range(3):
                button_row.append(self.board[(row, column)].cget('text'))
            if button_row[0] == button_row[1] == button_row[2] and '' not in button_row:
                self.winner = button_row[0]

    def check_vertical(self):
        for column in range(3):
            button_column = []
            for row in range(3):
                button_column.append(self.board[(row, column)].cget('text'))
            if button_column[0] == button_column[1] == button_column[2] and '' not in button_column:
                self.winner = button_column[0]

    def check_principal_diagonal(self):
        button_diagonal = []
        for row in range(3):
            for column in range(3):
                if row == column:
                    button_diagonal.append(self.board[(row, column)].cget('text'))
        if button_diagonal[0] == button_diagonal[1] == button_diagonal[2] and '' not in button_diagonal:
            self.winner = button_diagonal[0]

    def check_secondary_diagonal(self):
        button_diagonal = []
        for row in range(3):
            for column in range(3):
                if (row + column) == (3 - 1):
                    button_diagonal.append(self.board[(row, column)].cget('text'))
        if button_diagonal[0] == button_diagonal[1] == button_diagonal[2] and '' not in button_diagonal:
            self.winner = button_diagonal[0]

    def check_winner(self):
        self.check_horizontal()
        self.check_vertical()
        self.check_secondary_diagonal()
        self.check_principal_diagonal()
        if self.winner != '':
            label = Label(text=f'{self.winner} Wins!', font=('Arial', 26, 'bold'), bg='black', fg='white')
            label.grid(row=4, columnspan=3)
            self.is_running = False
        elif self.move_count == 9:
            label = Label(text=f'It\'s a Draw', font=('Arial', 26, 'bold'), bg='black', fg='white')
            label.grid(row=4, columnspan=3)
            self.is_running = False

    def move(self, row, col):
        button = self.board[(row, col)]
        if button.cget('text') == '' and self.is_running == True:
            button.config(text='X')
            self.move_count += 1
            self.check_winner()
            self.computer_move()

    def computer_move(self):
        if self.move_count < 8 and self.winner == '':
            choice = (random.randint(0, 2), random.randint(0, 2))
            while self.board[choice].cget('text') == 'X' or self.board[choice].cget('text') == 'O':
                choice = (random.randint(0, 2), random.randint(0, 2))
            button = self.board[choice]
            button.config(text='O')
            self.move_count += 1
        self.check_winner()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                grid_button = Button(height=4, width=9, command=lambda r=row, c=col: self.move(r, c),
                                     font=('Arial', 12))
                grid_button.grid_propagate(False)
                self.board[(row, col)] = grid_button
                grid_button.grid(row=row, column=col, padx=5, pady=5)
        game_label = Label(text='Tic Tac Toe', font=('Arial', 26, 'bold'), bg='black', fg='white', pady=5)
        game_label.grid(row=3, columnspan=3)
