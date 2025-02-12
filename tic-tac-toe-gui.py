import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.human_turn = False
        self.create_widgets()
        self.ask_start()

    def create_widgets(self):
        # Create buttons grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.master, text=' ', font=('Arial', 20), width=5, height=2,
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)
        # Status label
        self.status_label = tk.Label(self.master, text="", font=('Arial', 14))
        self.status_label.grid(row=3, columnspan=3)

    def ask_start(self):
        response = messagebox.askyesno("Start", "Do you want to start first?")
        if response:
            self.human_turn = True
            self.status_label.config(text="Your turn (X)")
        else:
            self.human_turn = False
            self.status_label.config(text="Computer's turn (O)")
            self.master.after(500, self.computer_move)

    def handle_click(self, row, col):
        if self.board[row][col] == ' ' and self.human_turn:
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X', state=tk.DISABLED)
            if self.check_winner(self.board, 'X'):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
                return
            elif self.is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            self.human_turn = False
            self.status_label.config(text="Computer's turn (O)")
            self.master.after(500, self.computer_move)

    def computer_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O', state=tk.DISABLED)
            if self.check_winner(self.board, 'O'):
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
                return
            elif self.is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            self.human_turn = True
            self.status_label.config(text="Your turn (X)")

    def find_best_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    new_board = [row.copy() for row in self.board]
                    new_board[i][j] = 'O'
                    score = self.minimax(new_board, False, -float('inf'), float('inf'))
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, is_maximizing, alpha, beta):
        if self.check_winner(board, 'O'):
            return 10
        elif self.check_winner(board, 'X'):
            return -10
        elif self.is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, False, alpha, beta)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, True, alpha, beta)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def check_winner(self, board, player):
        # Check rows and columns
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def is_board_full(self, board):
        for row in board:
            if ' ' in row:
                return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)
        self.ask_start()

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()