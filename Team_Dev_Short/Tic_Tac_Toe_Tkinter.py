import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, symbol):
        self.current_player = symbol
        self.buttons = []
        self.scores = {"X": 0, "O": 0}

        self.game_window = tk.Tk()
        self.game_window.title("Крестики-нолики (Tic Tac Toe)")
        self.game_window.configure(bg="#f0f0f0")
        self.game_window.geometry("350x600")
        # self.game_window.resizable(False, False)

        # Current Player Label
        self.turn_label = tk.Label(self.game_window, text=f"Ходит: {self.current_player}", font=("Arial", 18), bg="#f0f0f0")
        self.turn_label.pack(pady=10)

        # Board Frame
        self.board_frame = tk.Frame(self.game_window, bg="#f0f0f0")
        self.board_frame.pack()

        self.create_buttons()

        # Score Label
        self.score_label = tk.Label(self.game_window, text="Счет: X - 0 | O - 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # History
        self.history_label = tk.Label(self.game_window, text="История побед:", font=("Arial", 14), bg="#f0f0f0")
        self.history_label.pack()

        self.history_text = tk.Text(self.game_window, height=5, width=30, font=("Arial", 10), bg="white", relief=tk.SUNKEN, bd=1)
        self.history_text.pack(pady=5)

        # Reset Button
        reset_button = tk.Button(self.game_window, text="Сброс игры", font=("Arial", 14), bg="#ff4d4d", fg="white", activebackground="#ff3333", width=20, command=self.reset_game)
        reset_button.pack(pady=10)

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Arial", 24), width=5, height=2, bg="#ffffff", activebackground="#d9d9d9",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] != "":
            return

        self.buttons[row][col]['text'] = self.current_player

        if self.check_winner():
            self.scores[self.current_player] += 1
            self.score_label['text'] = f"Счет: X - {self.scores['X']} | O - {self.scores['O']}"
            self.history_text.insert(tk.END, f"Игрок {self.current_player} победил!\n")
            if self.scores[self.current_player] == 3:
                messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} выиграл игру!")
                self.game_window.quit()
            self.reset_board()
        elif self.check_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            self.reset_board()

        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label['text'] = f"Ходит: {self.current_player}"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        return all(btn['text'] != "" for row in self.buttons for btn in row)

    def reset_board(self):
        for row in self.buttons:
            for btn in row:
                btn['text'] = ""

    def reset_game(self):
        self.scores = {"X": 0, "O": 0}
        self.score_label['text'] = "Счет: X - 0 | O - 0"
        self.history_text.delete(1.0, tk.END)
        self.reset_board()
        self.current_player = "X"
        self.turn_label['text'] = f"Ходит: {self.current_player}"

    def start_game(self):
        self.game_window.mainloop()


def choose_symbol():
    window = tk.Tk()
    window.title("Выбор символа")
    window.geometry("400x200")
    window.configure(bg="#f0f0f0")

    tk.Label(window, text="Что выбираете?", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
    btn_frame = tk.Frame(window, bg="#f0f0f0")
    btn_frame.pack()

    tk.Button(btn_frame, text="X", font=("Arial", 20), width=5, height=2, bg="#4CAF50", fg="white", activebackground="#45a049",
              command=lambda: start_game("X", window)).grid(row=0, column=0, padx=20)

    tk.Button(btn_frame, text="O", font=("Arial", 20), width=5, height=2, bg="#2196F3", fg="white", activebackground="#1e88e5",
              command=lambda: start_game("O", window)).grid(row=0, column=1, padx=20)

    window.mainloop()

def start_game(symbol, window):
    window.destroy()
    game = TicTacToe(symbol)
    game.start_game()

choose_symbol()





# import tkinter as tk
# from tkinter import messagebox
#
# """
# Tic Tac Toe Game
# Player First selects X or O
# After each win , one player gets a 1 point
# Players who select symbol starts first and after each set new player starts its turn first
# After 3 wins , the game ends
# """
#
# class TicTacToe:
#     def __init__(self, symbol):
#         self.current_player = symbol
#         self.buttons = []
#         self.scores = {"X": 0, "O": 0}
#         self.game_window = tk.Tk()
#         self.game_window.title("Крестики-нолики")
#         self.game_window.geometry("300x500")
#         self.create_buttons()
#         self.score_label = tk.Label(self.game_window, text="Счет: 'X' - 0, 'O' - 0", font=("Arial", 16))
#         self.score_label.grid(row=4, column=0, columnspan=3)
#         self.history_label = tk.Label(self.game_window, text="История побед:", font=("Arial", 16))
#         self.history_label.grid(row=5, column=0, columnspan=3)
#         self.history_text = tk.Text(self.game_window, height=5, width=20)
#         self.history_text.grid(row=6, column=0, columnspan=3)
#
#     def create_buttons(self):
#         for i in range(3):
#             row = []
#             for j in range(3):
#                 btn = tk.Button(self.game_window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: self.on_click(r, c))
#                 btn.grid(row=i, column=j)
#                 row.append(btn)
#             self.buttons.append(row)
#
#         reset_button = tk.Button(self.game_window, text="Сброс", font=("Arial", 16), width=10, height=1, command=self.reset_game)
#         reset_button.grid(row=3, column=0, columnspan=3)
#
#     def on_click(self, row, col):
#         if self.buttons[row][col]['text'] != "":
#             return
#
#         self.buttons[row][col]['text'] = self.current_player
#
#         if self.check_winner():
#             self.scores[self.current_player] += 1
#             self.score_label['text'] = f"Счет: X - {self.scores['X']}, O - {self.scores['O']}"
#             self.history_text.insert(tk.END, f"Игрок {self.current_player} победил!\n")
#             if self.scores[self.current_player] == 3:
#                 messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} выиграл игру!")
#                 self.game_window.quit()
#             self.reset_board()
#         elif self.check_draw():
#             messagebox.showinfo("Игра окончена", "Ничья!")
#             self.reset_board()
#
#         self.current_player = "O" if self.current_player == "X" else "X"
#
#     def check_winner(self):
#         for i in range(3):
#             if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
#                 return True
#             if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
#                 return True
#
#         if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
#             return True
#         if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
#             return True
#
#         return False
#
#     def check_draw(self):
#         for row in self.buttons:
#             for btn in row:
#                 if btn['text'] == "":
#                     return False
#         return True
#
#     def reset_board(self):
#         for row in self.buttons:
#             for btn in row:
#                 btn['text'] = ""
#
#     def reset_game(self):
#         self.scores = {"X": 0, "O": 0}
#         self.score_label['text'] = "Счет: X - 0, O - 0"
#         self.history_text.delete(1.0, tk.END)
#         self.reset_board()
#
#     def start_game(self):
#         self.game_window.mainloop()
#
# def choose_symbol():
#     window = tk.Tk()
#     window.title("Выбор символа")
#     window.geometry("500x200")
#
#     tk.Label(window, text="Что выбираете?", font=("Arial", 16)).grid(row=0, column=0)
#     tk.Button(window, text="X", font=("Arial", 20), width=5, height=2, command=lambda: start_game("X",window)).grid(row=0, column=1)
#     tk.Button(window, text="O", font=("Arial", 20), width=5, height=2, command=lambda: start_game("O",window)).grid(row=0, column=2)
#
#     window.mainloop()
#
# def start_game(symbol,window):
#     window.destroy()
#     game = TicTacToe(symbol)
#     game.start_game()
#
# choose_symbol()
#
