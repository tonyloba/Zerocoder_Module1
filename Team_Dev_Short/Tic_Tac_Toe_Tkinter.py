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
        self.game_window.geometry("350x650")
        # self.game_window.resizable(False, False)
        self.game_window.maxsize(False, False)


        self.turn_label = tk.Label(self.game_window, text=f"Ходит: {self.current_player}", font=("Arial", 18), bg="#f0f0f0")
        self.turn_label.pack(pady=10)

        self.board_frame = tk.Frame(self.game_window, bg="#f0f0f0")
        self.board_frame.pack()

        self.create_buttons()

        self.score_label = tk.Label(self.game_window, text="Счет: X - 0 | O - 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.history_label = tk.Label(self.game_window, text="История побед:", font=("Arial", 14), bg="#f0f0f0")
        self.history_label.pack()

        self.history_text = tk.Text(self.game_window, height=5, width=30, font=("Arial", 10), bg="white", relief=tk.SUNKEN, bd=1)
        self.history_text.pack(pady=5)

        reset_button = tk.Button(self.game_window, text="Сброс игры", font=("Arial", 14), bg="#ff4d4d", fg="white",
                                 activebackground="#ff3333", width=20, command=self.reset_game)
        reset_button.pack(pady=10)

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Arial", 24), width=5, height=2, bg="#ffffff",
                                activebackground="#d9d9d9", command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] != "":
            return

        self.buttons[row][col]['text'] = self.current_player

        winner, winning_cells = self.check_winner()
        if winner:
            self.scores[self.current_player] += 1
            self.score_label['text'] = f"Счет: X - {self.scores['X']} | O - {self.scores['O']}"
            self.history_text.insert(tk.END, f"Игрок {self.current_player} победил!\n")
            self.highlight_winner(winning_cells)

            if self.scores[self.current_player] == 3:
                self.show_end_game_menu()
            else:
                self.game_window.after(1000, self.reset_board)
                self.switch_player()

        elif self.check_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            self.history_text.insert(tk.END, f"Ничья!\n")
            self.highlight_draw()
            self.game_window.after(1000, self.reset_board)
            self.switch_player()

        else:
            self.switch_player()

    def switch_player(self):
        """Меняет текущего игрока и обновляет надпись"""
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label['text'] = f"Ходит: {self.current_player}"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True, [(i, 0), (i, 1), (i, 2)]
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True, [(0, i), (1, i), (2, i)]

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True, [(0, 0), (1, 1), (2, 2)]
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True, [(0, 2), (1, 1), (2, 0)]

        return False, []

    def check_draw(self):
        return all(btn['text'] != "" for row in self.buttons for btn in row)

    def highlight_winner(self, winning_cells):
        for row, col in winning_cells:
            self.buttons[row][col].config(bg="#90EE90")  # Зеленый цвет
        self.game_window.after(1000, self.reset_board)

    def highlight_draw(self):
        for row in self.buttons:
            for btn in row:
                btn.config(bg="#d3d3d3")  # Серый цвет
        self.game_window.after(1000, self.reset_board)

    def reset_board(self):
        for row in self.buttons:
            for btn in row:
                btn['text'] = ""
                btn.config(bg="white")

    def reset_game(self):
        self.scores = {"X": 0, "O": 0}
        self.score_label['text'] = "Счет: X - 0 | O - 0"
        self.history_text.delete(1.0, tk.END)
        self.reset_board()
        self.current_player = "X"
        self.turn_label['text'] = f"Ходит: {self.current_player}"

    def show_end_game_menu(self):
        menu = tk.Toplevel(self.game_window)
        menu.title("Конец игры")
        menu.geometry("300x150")
        menu.configure(bg="#f0f0f0")

        tk.Label(menu, text=f"Игрок {self.current_player} выиграл игру!", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        tk.Button(menu, text="Играть снова", font=("Arial", 12), bg="#4CAF50", fg="white",
                  command=lambda: [menu.destroy(), self.reset_game()]).pack(pady=5)
        tk.Button(menu, text="Выйти", font=("Arial", 12), bg="#ff4d4d", fg="white",
                  command=self.game_window.quit).pack(pady=5)

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

    tk.Button(btn_frame, text="X", font=("Arial", 20), width=5, height=2, bg="#4CAF50", fg="white",
              command=lambda: start_game("X", window)).grid(row=0, column=0, padx=20)

    tk.Button(btn_frame, text="O", font=("Arial", 20), width=5, height=2, bg="#2196F3", fg="white",
              command=lambda: start_game("O", window)).grid(row=0, column=1, padx=20)

    window.mainloop()

def start_game(symbol, window):
    window.destroy()
    game = TicTacToe(symbol)
    game.start_game()

choose_symbol()

