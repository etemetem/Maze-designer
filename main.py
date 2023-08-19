import tkinter as tk
from tkinter import ttk
import customtkinter

CELL_SIZE = 0.0625
WALL_WIDTH = 2
WALL_COLOR = "black"
EMPTY_COLOR = "white"
FILLED_COLOR = "black"

TOP = 1
RIGHT = 2
BOTTOM = 4
LEFT = 8

class Cell:
    def __init__(self):
        self.value = 0
        self.walls = 0

def toggle_wall(cell, wall):
    if cell.walls & wall:
        cell.walls -= wall
    else:
        cell.walls += wall

def update_cell_color(cell, button):
    if cell.walls > 0:
        button.config(style="Wall.TButton")
    else:
        button.config(style="Empty.TButton")

def toggle_wall_click(cell, button, wall):
    toggle_wall(cell, wall)
    if wall == TOP:
        cell.value += 1
    elif wall == RIGHT:
        cell.value += 2
    elif wall == BOTTOM:
        cell.value += 4
    elif wall == LEFT:
        cell.value += 8
    update_cell_color(cell, button)

def clear_cells(grid):
    for row in grid:
        for cell in row:
            cell.value = 0
            cell.walls = 0

def show_cell_values(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    print("Cell Values:")
    
    for j in range(num_cols):
        col_values = [grid[i][j].value for i in range(num_rows)]
        print(col_values)

def create_grid(root, rows, columns):
    grid = []
    for i in range(rows):
        row = []
        for j in range(columns):
            cell = Cell()
            frame = tk.Frame(root)
            frame.place(relx=CELL_SIZE*i, rely=CELL_SIZE*j, relwidth=CELL_SIZE, relheight=CELL_SIZE)
            
            style = ttk.Style()
            style.configure("Wall.TButton", background=WALL_COLOR)
            style.configure("Empty.TButton", background=EMPTY_COLOR)
            
            top_button = ttk.Button(frame, width=WALL_WIDTH, style="Empty.TButton")
            top_button.place(relx=0,rely=0,relheight=0.15,relwidth=1)

            left_button = ttk.Button(frame, width=WALL_WIDTH, style="Empty.TButton")
            left_button.place(relx=0,rely=0.15,relheight=0.70,relwidth=0.15)

            right_button = ttk.Button(frame, width=WALL_WIDTH, style="Empty.TButton")
            right_button.place(relx=0.85,rely=0.15,relheight=0.70,relwidth=0.15)

            bottom_button = ttk.Button(frame, width=WALL_WIDTH, style="Empty.TButton")
            bottom_button.place(relx=0,rely=0.85,relheight=0.15,relwidth=1)

            top_button.config(command=lambda c=cell, w=TOP, b=top_button: toggle_wall_click(c, b, w))
            left_button.config(command=lambda c=cell, w=LEFT, b=left_button: toggle_wall_click(c, b, w))
            right_button.config(command=lambda c=cell, w=RIGHT, b=right_button: toggle_wall_click(c, b, w))
            bottom_button.config(command=lambda c=cell, w=BOTTOM, b=bottom_button: toggle_wall_click(c, b, w))
            
            row.append(cell)
        grid.append(row)
    return grid

def main():
    root = tk.Tk()
    root.title("Wall Grid")
    frame = tk.Frame()
    frame.place(relx=0, rely=0, relheight=1, relwidth=0.75)

    rows = 16
    columns = 16

    grid = create_grid(frame, rows, columns)
    
    show_button = customtkinter.CTkButton(root, text="Show Cell Values", command=lambda: show_cell_values(grid))
    show_button.place(relx=0.8, rely=0.15, relwidth=0.2)
    
    clear_button = customtkinter.CTkButton(root, text="Clear Cells", command=lambda: clear_cells(grid))
    clear_button.place(relx=0.8, rely=0.2, relwidth=0.2)
    
    data_entry = tk.Text(root, height=10, width=30)
    data_entry.place(relx=0.8, rely=0.4)
    
    root.mainloop()

if __name__ == "__main__":
    main()
