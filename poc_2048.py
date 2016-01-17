"""
Clone of 2048 game.
"""

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def _slide_tiles(line):
    """
    Function that slides a single row to the left without merging in 2048.
    """
    res_line = [0] * len(line)
    next_idx = 0
    for num in line:
        if num > 0:
            res_line[next_idx] = num
            next_idx += 1
    return res_line

def _merge_tiles(line):
    """
    Function that merge titles in a slided line without sliding in 2048.
    """
    res_line = line[:]
    idx = 0
    while idx < len(res_line) and res_line[idx] > 0:
        if idx < len(res_line) - 1 and res_line[idx + 1] == res_line[idx]:
            res_line[idx] *= 2
            res_line[idx + 1] = 0
            idx += 2
        else:
            idx += 1
    return res_line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    return _slide_tiles(_merge_tiles(_slide_tiles(line)))

import random
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.grid_width)] for dummy_row
                in range(self.grid_height)]
        for dummy_num in range(2):  # add two tiles
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        res_str = '['
        for row in range(self.grid_height):
            res_str += '['
            for col in range(self.grid_width):
                res_str += str(self.grid[row][col])
                if col == self.grid_width - 1:
                    res_str += ']'
                else:
                    res_str += ', '
        res_str += ']'
        return res_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_pos = [(row, col) for row in range(self.grid_height) for col in
                range(self.grid_width) if self.grid[row][col] == 0]
        row, col = random.choice(empty_pos)
        value = 2 if random.random() < 0.9 else 4
        self.grid[row][col] = value
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

if __name__ == '__main__':
    poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
