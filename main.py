
import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title('2048 Game')
        self.master.geometry('400x500')

        self.grid_cells = []
        self.grid_frame = tk.Frame(self.master, bg='#bbada0')
        self.grid_frame.pack()

        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.score = 0
        self.score_label = tk.Label(self.master, text='Score: 0', font=('Arial', 16), bg='#bbada0')
        self.score_label.pack(pady=10)

        self.new_game_button = tk.Button(self.master, text='New Game', font=('Arial', 14), bg='#8f7a66', fg='white', command=self.reset_game)
        self.new_game_button.pack()

        self.master.bind("<Key>", self.key_pressed)

    def init_grid(self):
        background_color_game = '#cdc1b4'
        for i in range(4):
            grid_row = []
            for j in range(4):
                cell = tk.Frame(self.grid_frame, bg=background_color_game, width=100, height=100)
                cell.grid(row=i, column=j, padx=10, pady=10)
                cell.grid_propagate(False)
                cell_text = tk.Label(cell, text='', bg=background_color_game, justify='center', font=('Arial', 32, 'bold'))
                cell_text.pack(expand=True)
                grid_row.append(cell_text)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = [[0]*4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.grid_cells[i][j].config(text='', bg='#ccc0b3')
                else:
                    self.grid_cells[i][j].config(text=str(cell_value), bg=self.get_tile_color(cell_value))

        self.score_label.config(text=f'Score: {self.score}')

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.matrix[i][j] == 0]
        if empty_cells:
            (i, j) = random.choice(empty_cells)
            self.matrix[i][j] = 2 if random.random() < 0.9 else 4

    def get_tile_color(self, value):
        colors = {
            2: '#eee4da', 4: '#ede0c8', 8: '#f2b179', 16: '#f59563',
            32: '#f67c5f', 64: '#f65e3b', 128: '#edcf72', 256: '#edcc61',
            512: '#edc850', 1024: '#edc53f', 2048: '#edc22e'
        }
        return colors.get(value, '#cdc1b4')

    def reset_game(self):
        self.init_matrix()
        self.update_grid_cells()

    def key_pressed(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            self.move_tiles(key)
            self.add_new_tile()
            self.update_grid_cells()
            self.check_game_over()

    def move_tiles(self, direction):
        if direction == 'Up':
            self.matrix = self.transpose(self.matrix)
            self.matrix = self.merge_tiles(self.matrix)
            self.matrix = self.transpose(self.matrix)
        elif direction == 'Down':
            self.matrix = self.transpose(self.matrix)
            self.matrix = self.reverse_rows(self.matrix)
            self.matrix = self.merge_tiles(self.matrix)
            self.matrix = self.reverse_rows(self.matrix)
            self.matrix = self.transpose(self.matrix)
        elif direction == 'Left':
            self.matrix = self.merge_tiles(self.matrix)
        elif direction == 'Right':
            self.matrix = self.reverse_rows(self.matrix)
            self.matrix = self.merge_tiles(self.matrix)
            self.matrix = self.reverse_rows(self.matrix)

    def transpose(self, matrix):
        return [[matrix[j][i] for j in range(4)] for i in range(4)]

    def reverse_rows(self, matrix):
        return [row[::-1] for row in matrix]

    def merge_tiles(self, matrix):
        for row in matrix:
            for i in range(3):
                if row[i] == row[i+1] and row[i] != 0:
                    row[i] *= 2
                    self.score += row[i]
                    row[i+1] = 0
        return matrix

    def check_game_over(self):
        game_over = True
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0 or (j < 3 and self.matrix[i][j] == self.matrix[i][j+1]) or (i < 3 and self.matrix[i][j] == self.matrix[i+1][j]):
                    game_over = False
                    break
        if game_over:
            game_over_label = tk.Label(self.master, text='Game Over!', font=('Arial', 24), bg='#bbada0')
            game_over_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
