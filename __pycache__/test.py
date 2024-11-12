# class Board:
#     def __init__(self, size, grid):
#         self.size = size
#         self.grid = grid
#         self.movable_squares = self.find_movable_squares()

#     def find_movable_squares(self):
#         movable_squares = []
#         for i in range(self.size):
#             for j in range(self.size):
#                 if self.grid[i][j] == 'M':
#                     movable_squares.append((i, j))
#         return movable_squares

#     def is_valid_move(self, row, col, direction):
#         if direction == 'up':
#             new_row = row - 1
#             new_col = col
#         elif direction == 'down':
#             new_row = row + 1
#             new_col = col
#         elif direction == 'left':
#             new_row = row
#             new_col = col - 1
#         else:  # 'right'
#             new_row = row
#             new_col = col + 1

#         if new_row < 0 or new_row >= self.size or new_col < 0 or new_col >= self.size:
#             return False
#         if self.grid[new_row][new_col] == 'S':
#             return False
#         return True

#     def move_square(self, row, col, direction):
#         if not self.is_valid_move(row, col, direction):
#             return None

#         if direction == 'up':
#             new_row = row - 1
#             new_col = col
#         elif direction == 'down':
#             new_row = row + 1
#             new_col = col
#         elif direction == 'left':
#             new_row = row
#             new_col = col - 1
#         else:  # 'right'
#             new_row = row
#             new_col = col + 1

#         new_grid = [row[:] for row in self.grid]
#         new_grid[row][col] = '.'
#         new_grid[new_row][new_col] = 'M'
#         new_board = Board(self.size, new_grid)
#         new_board.movable_squares.remove((row, col))
#         new_board.movable_squares.append((new_row, new_col))
#         return new_board