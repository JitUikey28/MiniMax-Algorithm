import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x450")
        self.window.configure(bg="#333333")
        self.title_label = tk.Label(self.window, text="Tic Tac Toe", font=('Arial', 24, 'bold'), bg="#333333", fg="white")
        self.title_label.pack(pady=20)
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        self.board = ['' for _ in range(9)]
        self.current_player = "X"
        self.buttons = [tk.Button(self.board_frame, text='', font=('Arial', 24), width=5, height=2,
                                  bg="#ffffff", fg="#333333", activebackground="#ffcccb",
                                  command=lambda i=i: self.on_button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col, padx=5, pady=5)

     
        self.status_label = tk.Label(self.window, text="Player X's Turn", font=('Arial', 16), bg="#333333", fg="white")
        self.status_label.pack(pady=10)

        self.window.mainloop()

 
    def on_button_click(self, i):
        if self.buttons[i]['text'] == '' and self.current_player == "X":
            self.buttons[i]['text'] = self.current_player
            self.buttons[i].config(fg="#4CAF50")  # Green color for 'X'
            self.board[i] = self.current_player
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            elif '' not in self.board:
                self.show_draw()
            else:
                self.current_player = "O"
                self.status_label.config(text="Player O's Turn")
                self.window.after(500, self.computer_move)  # Small delay for the computer's move

    def computer_move(self):
        best_move = self.minimax(self.board, 0, True)
        self.board[best_move] = "O"
        self.buttons[best_move]['text'] = "O"
        self.buttons[best_move].config(fg="#F44336")  # Red color for 'O'

        if self.check_winner("O"):
            self.show_winner("O")
        elif '' not in self.board:
            self.show_draw()
        else:
            self.current_player = "X"
            self.status_label.config(text="Player X's Turn")

    #use minimax: +1 for a win O for AI, -1 for win for X  for human and 0 is draw
    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner_minimax(board)
        if winner == "X":
            return -1
        if winner == "O":
            return 1
        if '' not in board:
            return 0

        if is_maximizing:
            best_score = -math.inf
            best_move = None
            for i in range(9):
                if board[i] == '':
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    if score > best_score:
                        best_score = score
                        best_move = i
            if depth == 0:
                return best_move
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == '':
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    if score < best_score:
                        best_score = score
            return best_score
    def check_winner(self, player):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        for comb in win_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] == player:
                return True
        return False
    def check_winner_minimax(self, board):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        for comb in win_combinations:
            if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
                return board[comb[0]]
        return None
    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()
    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()
    def reset_game(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button['text'] = ''
        self.current_player = "X"
        self.status_label.config(text="Player X's Turn")

if __name__ == "__main__":
    TicTacToe()
