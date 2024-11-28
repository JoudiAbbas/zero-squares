from collections import deque
from copy import deepcopy
from square import Square
from algorithms import Bfs
# from algorithms import Dfs
from DFS_r import Dfs_recursive 


class Board :

    def __init__ (self,array=None,parent=None, move_name="Initial",move=None):
        puzzle1 = [
        [ Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
        [ Square("1"), Square("r", True, "red"), Square("0"), Square("0"), Square("R", False, "red"), Square("1"), Square("1")],
        [ Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")]
        ]
        puzzle2 = [
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),],
           [Square("1"),Square("r",True,"red"),Square("0"),Square("0"),Square("G",False,"green"),Square("1"),Square("1"),],
           [Square("1"),Square("g",True,"green"),Square("0"),Square("0"),Square("R",False,"red"),Square("1"),Square("1"),],
           [Square("1"),Square("b",True,"blue"),Square("0"),Square("0"),Square("B",False,"blue"),Square("1"),Square("1"),],
          [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1")] 
                     ]

        puzzle3 = [
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),],
           [Square("1"),Square("r",True,"red"),Square("0"),Square("0"),Square("R",False,"red"),Square("1"),Square("1"),],
           [Square("1"),Square("b",True,"blue"),Square("0"),Square("0"),Square("B",False,"blue"),Square("1"),Square("1"),],
          [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1")] 
                     ]
        puzzle4 = [
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1")],
           [Square("1"),Square("1"),Square("0"),Square("R",False,"red"),Square("0"),Square("0"),Square("0"),Square("1"),],
           [Square("1"),Square("r",True,"red"),Square("0"),Square("b",True,"blue"),Square("0"),Square("0"),Square("0"),Square("1"),],
          [Square("1"),Square("0"),Square("1"),Square("0"),Square("0"),Square("0"),Square("0"),Square("1"),] ,
          [Square("1"),Square("B",False,"blue"),Square("0"),Square("0"),Square("0"),Square("0"),Square("0"),Square("1"),],
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),]
                     ]
        
        puzzle5 = [
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
         [Square("1"), Square("1"), Square("0"), Square("0"), Square("0"), Square("G", False, "green"), Square("1"), Square("1")],
         [Square("1"), Square("0"), Square("0"), Square("1"), Square("0"), Square("0"), Square("0"), Square("1")],
         [Square("1"), Square("r", True, "red"), Square("1"), Square("b", True, "blue"), Square("1"), Square("g", True, "green"), Square("0"), Square("1")],
         [Square("1"), Square("B", False, "blue"), Square("0"), Square("0"), Square("R", False, "red"), Square("0"), Square("1"), Square("1")],
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")]
                      ]
        
        puzzle6 = [
           [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
           [Square("1"), Square("g", True, "green"), Square("G", False, "green"), Square("0"), Square("0"), Square("B", False, "blue"), Square("0"), Square("1")],
           [Square("1"), Square("0"), Square("1"), Square("0"), Square("1"), Square("0"), Square("1"), Square("1")],
           [Square("1"), Square("r", True, "red"), Square("0"), Square("0"), Square("b", True, "blue"), Square("0"), Square("0"), Square("1")],
           [Square("1"), Square("0"), Square("0"), Square("R", False, "red"), Square("0"), Square("0"), Square("0"), Square("1")],
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")]
                            ]
        puzzle7 = [
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),],
           [Square("1"),Square("R",False,"red"),Square("0"),Square("b",True,"blue"),Square("1"),],
           [Square("1"),Square("0"),Square("0"),Square("0"),Square("1"),],
           [Square("1"),Square("0"),Square("0"),Square("0"),Square("1"),],
          [Square("1"),Square("1"),Square("1"),Square("1"),Square("1")] 
                     ]
        puzzle8 = [
            [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
            [Square("1"), Square("r", True, "red"), Square("0"), Square("0"), Square("G", False, "green",True), Square("0"), Square("1")],
            [Square("1"), Square("g", True, "green"), Square("0"), Square("0"), Square("0"), Square("1"), Square("1")],
            [Square("1"), Square("b", True, "blue"), Square("0"), Square("R", False, "red",True), Square("B", False, "blue",True), Square("1"), Square("1")],
            [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")] 
        ]


        self.stack = []
        self.array = array if array is not None else puzzle3
        self.parent=parent
        self.move_name= move_name
        self.move=move
        
#طباعة الرقعة
    def print_board(self):
         for row in self.array:
            for square in row:
             print(square.color, end=" ")
            print()


    
    def copy(self):
         return Board(deepcopy(self.array), parent=self)


    
            #جهة اليمين

    def check_right(self,row,j):
            if j+1< len(row):
              if row[j].can_move == True :
                if row[j+1].color == '0' :
                 return True
                if row[j+1].color in ['R','B','G'] and row[j].color_goal != row[j + 1].color_goal:
                 return True
            return False
    
    def goal_right(self, row, j):
     if j+1< len(row):
        if row[j].can_move is True:
            if row[j+1].color in ['R','B','G'] and row[j].color_goal == row[j + 1].color_goal:
                return True
     return False
    
    
    def move_right(self):
     movable_squares = []
     for row in self.array:
        for i, square in enumerate(row):
            if self.check_right(row, i):
                 movable_squares.append((row, i))

     for row, i in reversed(movable_squares):
        while self.check_right(row, i):
            if row[i+1].color in ['R','B','G'] and row[i].color_goal != row[i + 1].color_goal:
              if not row[i+1].is_temp_occupied:
                  row[i+1].is_temp_occupied= True
                  row[i+1].original_color= row[i+1].color
                  row[i+1].original_color_goal=row[i+1].color_goal
                  
            row[i+1].color = row[i].color
            row[i+1].can_move = True
            row[i+1].color_goal = row[i].color_goal

            if row[i].is_temp_occupied:
               row[i].color = row[i].original_color
               row[i].color_goal = row[i].original_color_goal
               row[i].is_temp_occupied = False
            else:
                row[i].color = '0'
                row[i].can_move = False
                row[i].color_goal = None

            i += 1

     for row in self.array:
        for i, square in enumerate(row):
            if self.goal_right(row, i):
                row[i + 1].color = '0'
                if row[i].is_goal:
                    row[i].color = row[i].original_color
                    row[i].color_goal = row[i].original_color_goal
                else:
                    row[i].color = '0'
                   

     self.reset_moves()
     self.stack.append(self.copy())
     new_array = [[square.copy() for square in row] for row in self.array]
     new_board = Board(new_array, parent=self)
     return new_board
    





                # جهة اليسار
    def check_left(self,row,j):
            if j>0:
              if row[j].can_move == True :
                if row[j-1].color == '0' :
                 return True
                if row[j-1].color in ['R','B','G']and row[j].color_goal!=row[j-1].color_goal:
                 return True 
            
            return False



    def goal_left(self,row,j):
            if j>0:
              if row[j].can_move == True :
                if row[j-1].color in ['R','B','G']and row[j].color_goal==row[j-1].color_goal:
                 return True
            return False
    
   
    def move_left(self):
     movable_squares = []
     for row in self.array:
        for i in range(len(row)-1,0,-1):
            if self.check_left(row, i) :
                 movable_squares.append((row,i))
                
     for row, i in reversed(movable_squares):
        while self.check_left(row, i):
            if row[i-1].color in ['R','B','G'] and row[i].color_goal != row[i-1].color_goal:
              if not row[i-1].is_temp_occupied:
                  row[i-1].is_temp_occupied= True
                  row[i-1].original_color= row[i-1].color
                  row[i-1].original_color_goal=row[i-1].color_goal
                  
            row[i-1].color = row[i].color
            row[i-1].can_move = True
            row[i-1].color_goal = row[i].color_goal
            if row[i].is_temp_occupied:
               row[i].color = row[i].original_color
               row[i].color_goal = row[i].original_color_goal
               row[i].is_temp_occupied = False
            else:
                row[i].color = '0'
                row[i].can_move = False
                row[i].color_goal = None
            i -= 1
                            
     for row in self.array:
        for i in range(len(row)-1,0,-1):      
            if self.goal_left(row,i):
                       row[i-1].color = '0'
                       if row[i].is_goal:
                        row[i].color = row[i].original_color
                        row[i].color_goal = row[i].original_color_goal
                       else:
                        row[i].color = '0'
                   
     self.reset_moves()
     self.stack.append(self.copy())
     new_array = []
     for row in self.array:
       new_row = [square.copy() for square in row]  
       new_array.append(new_row)
       new_board = Board(new_array, parent=self)
     return new_board
     

    
      # جهة الأعلى
    def check_up(self, row, col):
        if row > 0:
            if self.array[row][col].can_move:
             if self.array[row-1][col].color == '0':
                    return True
             if self.array[row -1][col].color in ['R','B','G'] and self.array[row][col].color_goal != self.array[row -1][col].color_goal:
                    return True
        return False
    
    def goal_up(self, row, col):
        if row > 0:
            if self.array[row][col].can_move:
              if self.array[row -1][col].color in ['R','B','G'] and self.array[row][col].color_goal == self.array[row -1][col].color_goal:
                    return True
        return False
    
    
    
    def move_up(self):
        movable_squares=[]
        for j in range(len(self.array[0])): 
          for i in range(len(self.array)- 1,0,-1):  
            if self.check_up(i, j):  
                    movable_squares.append((i,j))

        for i, j in reversed(movable_squares):
            while self.check_up(i, j): 
             if self.array[i-1][j].color in ['R','B','G'] and self.array[i][j].color_goal != self.array[i-1][j].color_goal:
              if not self.array[i-1][j].is_temp_occupied:
                  self.array[i-1][j].is_temp_occupied= True
                  self.array[i-1][j].original_color= self.array[i-1][j].color
                  self.array[i-1][j].original_color_goal=self.array[i-1][j].color_goal
                  
             self.array[i-1][j].color = self.array[i][j].color
             self.array[i-1][j].can_move = True
             self.array[i-1][j].color_goal = self.array[i][j].color_goal
             if self.array[i][j].is_temp_occupied:
               self.array[i][j].color = self.array[i][j].original_color
               self.array[i][j].color_goal =self.array[i][j].original_color_goal
               self.array[i][j].is_temp_occupied = False
             else:
               self.array[i][j].color = '0'
               self.array[i][j].can_move = False
               self.array[i][j].color_goal = None
             i -= 1
               

        for j in range(len(self.array[0])): 
          for i in range(len(self.array)- 1,0,-1):
            if self.goal_up(i,j):
                self.array[i-1][j].color = '0'
                if self.array[i][j].is_goal:
                   self.array[i][j].color = self.array[i-1][j].original_color
                   self.array[i][j].color_goal = self.array[i-1][j].original_color_goal
                else:
                    self.array[i][j].color = '0'

        self.reset_moves()
        self.stack.append(self.copy())
        new_array = []
        for row in self.array:
          new_row = [square.copy() for square in row]  
          new_array.append(new_row)
        new_board = Board(new_array, parent=self)
        return new_board
   


# جهة الأسفل
    def check_down(self, row, col):
        if row+1 < len(self.array):
             if self.array[row][col].can_move:
                if self.array[row+1][col].color =='0'  :
                    return True
                if  self.array[row +1][col].color in ['R','B','G'] and self.array[row][col].color_goal != self.array[row+ 1][col].color_goal:
                    return True
        return False
    
    def goal_down(self, row, col):
        if row+1 < len(self.array):
             if self.array[row][col].can_move:
                if  self.array[row +1][col].color in ['R','B','G'] and self.array[row][col].color_goal == self.array[row+ 1][col].color_goal:
                    return True
        return False
   

    def move_down(self):
        movable_squares=[]
        for j in range(len(self.array[0])):  
         for i in range(len(self.array) -1):  
                if self.check_down(i, j):  
                 movable_squares.append((i,j))

        for i, j in reversed(movable_squares):
         while self.check_down(i, j): 
            if self.array[i+1][j].color in ['R','B','G'] and self.array[i][j].color_goal != self.array[i+1][j].color_goal:
                if not self.array[i-1][j].is_temp_occupied:
                  self.array[i+1][j].is_temp_occupied= True
                  self.array[i+1][j].original_color= self.array[i+1][j].color
                  self.array[i+1][j].original_color_goal=self.array[i+1][j].color_goal
                  
            self.array[i+1][j].color = self.array[i][j].color
            self.array[i+1][j].can_move = True
            self.array[i+1][j].color_goal = self.array[i][j].color_goal
            if self.array[i][j].is_temp_occupied:
               self.array[i][j].color = self.array[i][j].original_color
               self.array[i][j].color_goal =self.array[i][j].original_color_goal
               self.array[i][j].is_temp_occupied = False
            else:
               self.array[i][j].color = '0'
               self.array[i][j].can_move = False
               self.array[i][j].color_goal = None
            i += 1

        for j in range(len(self.array[0])):  
          for i in range(len(self.array) -1):  
                if self.goal_down(i,j):
                       self.array[i +1][j].color = '0'
                       if self.array[i][j].is_goal:
                        self.array[i][j].color = self.array[i+1][j].original_color
                        self.array[i][j].color_goal = self.array[i+1][j].original_color_goal
                       else:
                        self.array[i][j].color = '0'

               
        self.reset_moves()
        self.stack.append(self.copy())
        new_array = []
        for row in self.array:
          new_row = [square.copy() for square in row]  
        new_array.append(new_row)
        new_board = Board(new_array, parent=self) 
        return new_board
    



    def reset_moves(self):
        for row in self.array:
           for square in row:
              if square.color in ['0','R','B','G']:
                    square.can_move = False


#يرد الحالات الممكنة
    def Next_state(self):
        next_states = []

        right_board = self.copy()
        right_board.move_right()
        next_states.append(("right",right_board))

        left_board = self.copy()
        left_board.move_left()
        next_states.append(("left",left_board))

        up_board = self.copy()
        up_board.move_up()
        next_states.append(("up", up_board))

        down_board = self.copy()
        down_board.move_down()
        next_states.append(("down",down_board))

        return next_states
    
    #يعيد الحركات التي قمت بفعلها
    def get_moves_stack(self):
        return self.stack
    

     # تحقق من الربح
    def check_win(self):
        all_won = True
        for row in self.array:
            for square in row:
              if square.color in ['r','g','b'] :
                  all_won =False
                  break
        if all_won:
         print("winner")
        else:
         print("not winner")
        return all_won
    
    # BFS
    def solve_bfs(self):
        return Bfs(self)

    # DFS
    def solve_dfs(self):
        return Dfs_recursive(self)

 