import tkinter as tk
from tkinter import messagebox, ttk
import random

LANGUAGES = {
    "DE": {
        "title": "Sudoku AI",
        "solve": "Lösen (Start AI)",
        "new": "Neues Spiel",
        "theme": "Design wechseln",
        "lang": "Sprache / Language",
        "status_ready": "Bereit.",
        "status_gen": "Generiere Puzzle...",
        "status_solve": "AI denkt nach...",
        "status_done": "Gelöst!",
        "status_fail": "Keine Lösung gefunden.",
        "header": "Backtracking Algorithmus"
    },
    "EN": {
        "title": "Sudoku AI Visualizer",
        "solve": "Solve (Start AI)",
        "new": "New Game",
        "theme": "Toggle Theme",
        "lang": "Language",
        "status_ready": "Ready.",
        "status_gen": "Generating puzzle...",
        "status_solve": "AI is thinking...",
        "status_done": "Solved!",
        "status_fail": "No solution found.",
        "header": "Backtracking Algorithm"
    },
    "FA": {
        "title": "حل‌کننده هوشمند سودوکو",
        "solve": "حل خودکار",
        "new": "بازی جدید",
        "theme": "تغییر پوسته",
        "lang": "تغییر زبان",
        "status_ready": "آماده",
        "status_gen": "در حال ساخت...",
        "status_solve": "هوش مصنوعی در حال فکر...",
        "status_done": "حل شد!",
        "status_fail": "راه حلی پیدا نشد.",
        "header": "الگوریتم بازگشت‌به‌عقب"
    }
}

THEMES = {
    "light": {
        "bg": "#f0f2f5",
        "fg": "#333333",
        "grid_bg": "#ffffff",
        "line": "#343a40",
        "text_fixed": "#000000",
        "text_temp": "#007bff",
        "text_solve": "#28a745",
        "btn_bg": "#e0e0e0",
        "btn_fg": "#000000",
        "highlight": "#e8f0fe"
    },
    "dark": {
        "bg": "#121212",
        "fg": "#ffffff",
        "grid_bg": "#1e1e1e",
        "line": "#555555",
        "text_fixed": "#e0e0e0",
        "text_temp": "#bb86fc",
        "text_solve": "#03dac6",
        "btn_bg": "#333333",
        "btn_fg": "#ffffff",
        "highlight": "#2c2c2c"
    }
}

class SudokuPro:
    def __init__(self, root):
        self.root = root
        self.current_lang = "DE"
        self.current_theme = "light"
        self.colors = THEMES[self.current_theme]
        
        self.grid_data = [[0]*9 for _ in range(9)]
        self.initial_mask = [[False]*9 for _ in range(9)]
        
        self.setup_window()
        self.create_widgets()
        self.apply_theme()
        self.generate_new_game()

    def setup_window(self):
        self.root.title("Sudoku Pro")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

    def create_widgets(self):
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.header_label = tk.Label(self.main_container, font=("Segoe UI", 16, "bold"), pady=15)
        self.header_label.pack()

        self.canvas = tk.Canvas(self.main_container, width=360, height=360, highlightthickness=0)
        self.canvas.pack(pady=10)

        self.controls_frame = tk.Frame(self.main_container)
        self.controls_frame.pack(fill=tk.X, padx=20, pady=10)

        self.btn_solve = tk.Button(self.controls_frame, command=self.start_solver, 
                                   font=("Segoe UI", 11, "bold"), height=2, borderwidth=0)
        self.btn_solve.pack(fill=tk.X, pady=5)

        self.btn_new = tk.Button(self.controls_frame, command=self.generate_new_game, 
                                 font=("Segoe UI", 10), height=1, borderwidth=0)
        self.btn_new.pack(fill=tk.X, pady=5)

        self.settings_frame = tk.Frame(self.main_container)
        self.settings_frame.pack(fill=tk.X, padx=20, pady=5)

        self.btn_theme = tk.Button(self.settings_frame, command=self.toggle_theme, 
                                   font=("Segoe UI", 9), borderwidth=0)
        self.btn_theme.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

        self.btn_lang = tk.Button(self.settings_frame, command=self.toggle_language, 
                                  font=("Segoe UI", 9), borderwidth=0)
        self.btn_lang.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=2)

        self.status_label = tk.Label(self.main_container, font=("Segoe UI", 10))
        self.status_label.pack(side=tk.BOTTOM, pady=15)

    def apply_theme(self):
        c = THEMES[self.current_theme]
        self.colors = c
        
        self.main_container.configure(bg=c["bg"])
        self.root.configure(bg=c["bg"])
        self.controls_frame.configure(bg=c["bg"])
        self.settings_frame.configure(bg=c["bg"])
        
        self.header_label.configure(bg=c["bg"], fg=c["fg"])
        self.status_label.configure(bg=c["bg"], fg=c["fg"])
        
        self.canvas.configure(bg=c["grid_bg"])
        
        buttons = [self.btn_solve, self.btn_new, self.btn_theme, self.btn_lang]
        for btn in buttons:
            btn.configure(bg=c["btn_bg"], fg=c["btn_fg"], activebackground=c["highlight"], activeforeground=c["fg"])
            
        self.update_texts()
        self.draw_grid()

    def update_texts(self):
        t = LANGUAGES[self.current_lang]
        self.root.title(t["title"])
        self.header_label.configure(text=t["header"])
        self.btn_solve.configure(text=t["solve"])
        self.btn_new.configure(text=t["new"])
        self.btn_theme.configure(text=t["theme"])
        self.btn_lang.configure(text=t["lang"])
        
    def draw_grid(self):
        self.canvas.delete("all")
        c = self.colors
        w = 360
        cell = w // 9

        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            color = c["line"]
            self.canvas.create_line(0, i*cell, w, i*cell, fill=color, width=width)
            self.canvas.create_line(i*cell, 0, i*cell, w, fill=color, width=width)

        for r in range(9):
            for c_idx in range(9):
                val = self.grid_data[r][c_idx]
                if val != 0:
                    x = c_idx * cell + cell/2
                    y = r * cell + cell/2
                    
                    if self.initial_mask[r][c_idx]:
                        color = c["text_fixed"]
                    else:
                        color = c["text_solve"]
                    
                    self.canvas.create_text(x, y, text=str(val), font=("Helvetica", 16, "bold"), fill=color, tags="nums")

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()

    def toggle_language(self):
        langs = ["DE", "EN", "FA"]
        idx = langs.index(self.current_lang)
        self.current_lang = langs[(idx + 1) % len(langs)]
        self.update_texts()
        self.status_label.configure(text=LANGUAGES[self.current_lang]["status_ready"])

    def generate_new_game(self):
        self.status_label.configure(text=LANGUAGES[self.current_lang]["status_gen"], fg=self.colors["fg"])
        self.root.update()
        
        self.grid_data = [[0]*9 for _ in range(9)]
        self.fill_diagonal()
        self.solve_logic(visualize=False)
        self.remove_digits()
        
        self.initial_mask = [[(x != 0) for x in row] for row in self.grid_data]
        self.draw_grid()
        self.status_label.configure(text=LANGUAGES[self.current_lang]["status_ready"])

    def fill_diagonal(self):
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        num = 0
        for i in range(3):
            for j in range(3):
                while True:
                    num = random.randint(1, 9)
                    if self.is_safe_in_box(row, col, num):
                        break
                self.grid_data[row+i][col+j] = num

    def is_safe_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.grid_data[row_start+i][col_start+j] == num:
                    return False
        return True

    def remove_digits(self):
        count = 40
        while count > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.grid_data[i][j] != 0:
                self.grid_data[i][j] = 0
                count -= 1

    def start_solver(self):
        self.status_label.configure(text=LANGUAGES[self.current_lang]["status_solve"], fg="#007bff")
        if self.solve_logic(visualize=True):
            self.status_label.configure(text=LANGUAGES[self.current_lang]["status_done"], fg="#28a745")
        else:
            self.status_label.configure(text=LANGUAGES[self.current_lang]["status_fail"], fg="red")

    def is_safe(self, row, col, num):
        for x in range(9):
            if self.grid_data[row][x] == num: return False
            if self.grid_data[x][col] == num: return False
        
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid_data[i + start_row][j + start_col] == num: return False
        return True

    def solve_logic(self, visualize=False):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid_data[row][col] = num
                
                if visualize:
                    self.draw_single_update(row, col, num, self.colors["text_temp"])
                    
                if self.solve_logic(visualize):
                    return True
                
                self.grid_data[row][col] = 0
                if visualize:
                    self.draw_single_update(row, col, 0, self.colors["bg"])
        
        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid_data[i][j] == 0:
                    return (i, j)
        return None

    def draw_single_update(self, r, c, val, color):
        self.canvas.update()
        if val == 0:
            self.draw_grid()
        else:
            cell = 360 // 9
            x = c * cell + cell/2
            y = r * cell + cell/2
            self.canvas.create_text(x, y, text=str(val), font=("Helvetica", 16, "bold"), fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuPro(root)
    root.mainloop()