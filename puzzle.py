



from square import Square


class Board :

    def __init__ (self,array=None):
        puzzle1 = [
        [ Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
        [ Square("1"), Square("R", False, "red"), Square("0"), Square("r", True, "red"), Square("1"), Square("1"), Square("1")],
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
           [Square("1"),Square("0"),Square("0"),Square("0"),Square("0"),Square("0"),Square("0"),Square("1"),],
          [Square("1"),Square("0"),Square("1"),Square("0"),Square("0"),Square("0"),Square("r",True,"red"),Square("1"),] ,
          [Square("1"),Square("B",False,"blue"),Square("0"),Square("0"),Square("0"),Square("0"),Square("b",True,"blue"),Square("1"),],
           [Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),Square("1"),]
                     ]
        
        puzzle5 = [
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
         [Square("1"), Square("1"), Square("0"), Square("0"), Square("0"), Square("G", False, "green"), Square("1"), Square("1")],
         [Square("1"), Square("0"), Square("0"), Square("1"), Square("0"), Square("0"), Square("0"), Square("1")],
         [Square("1"), Square("r", True, "red"), Square("1"), Square("b", True, "blue"), Square("1"), Square("g", True, "green"), Square("1"), Square("1")],
         [Square("1"), Square("B", False, "blue"), Square("0"), Square("0"), Square("R", False, "red"), Square("0"), Square("1"), Square("1")],
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")]
                      ]
        
        puzzle6 = [
           [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")],
           [Square("1"), Square("G", False, "green"), Square("0"), Square("0"), Square("0"), Square("B", False, "blue"), Square("0"), Square("1")],
           [Square("1"), Square("0"), Square("1"), Square("0"), Square("1"), Square("0"), Square("1"), Square("1")],
           [Square("1"), Square("0"), Square("g", True, "green"), Square("0"), Square("b", True, "blue"), Square("0"), Square("0"), Square("1")],
           [Square("1"), Square("r", True, "red"), Square("0"), Square("R", False, "red"), Square("0"), Square("0"), Square("0"), Square("1")],
         [Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1"), Square("1")]
                            ]


        self.stack = []
        self.array = array if array is not None else puzzle6
        
        
#طباعة الرقعة
    def print_board(self):
         for row in self.array:
            for square in row:
             print(square.color, end=" ")
            print()


    

    def copy(self):
        new_array = []
        for row in self.array:
          new_row = [square.copy() for square in row]  
          new_array.append(new_row)
        return Board(new_array)

    
            #جهة اليمين

    def check_right(self,row,j):
            if j+1< len(row):
              if row[j].can_move == True :
                if row[j+1].color == '0':
                 return True
            return False
    
    def goal_right(self, row, j):
     if j+1< len(row):
        if row[j].can_move is True:
            if row[j+1].color in ['R','B','G'] and row[j].color_goal == row[j + 1].color_goal:
                return True
     return False
    
   
    
   

    def move_right(self):
                
                for row in self.array:
                 for i,square in enumerate(row):
                        if  self.check_right(row, i)==True:
                            row[i].color = '0'
                            row[i+1].can_move = True
                            if row[i].color_goal=="red":
                             row[i+1].color_goal="red"
                             row[i+1].color = 'r'
                            if row[i].color_goal=="blue":
                             row[i+1].color_goal="blue"
                             row[i+1].color = 'b'
                            if row[i].color_goal=="green":
                             row[i+1].color_goal="green"
                             row[i+1].color = 'g'

                        if self.goal_right(row,i):
                         row[i+1].color = '0'
                         row[i].color='0'

                        
                     
                self.reset_moves()
                self.stack.append(self.copy())
                new_array = [[square.copy() for square in row] for row in self.array]
                new_board = Board(new_array)
                return new_board

                       
                        

                # جهة اليسار
    def check_left(self,row,j):
            if j>0:
              if row[j].can_move == True :
                if row[j-1].color == '0' :
                 return True
            return False
    
    def goal_left(self,row,j):
            if j>0:
              if row[j].can_move == True :
                if row[j-1].color in ['R','B','G']and row[j].color_goal==row[j-1].color_goal:
                 return True
            return False
    
   



 
    def move_left(self):
     
     for row in self.array:
        for i in range(len(row)-1,0,-1):
            if self.check_left(row, i) :
                row[i].color = '0'
                row[i-1].can_move = True
                if row[i].color_goal =="red":
                    row[i- 1].color_goal = "red"
                    row[i-1].color ='r'
                if row[i].color_goal =="blue":
                    row[i-1].color_goal ="blue"
                    row[i-1].color = 'b'
                if row[i].color_goal =="green":
                    row[i-1].color_goal ="green"
                    row[i-1].color = 'g'
                
            if self.goal_left(row,i):
                       row[i-1].color = '0'
                       row[i].color='0'

            

            
     self.reset_moves()
     self.stack.append(self.copy())
     new_array = []
     for row in self.array:
       new_row = [square.copy() for square in row]  
       new_array.append(new_row)
     new_borad=Board(new_array)
     return new_borad
     
    
      # جهة الأعلى
    def check_up(self, row, col):
        if row > 0:
            if self.array[row][col].can_move:
             if self.array[row-1][col].color == '0':
                    return True
        return False
    
    def goal_up(self, row, col):
        if row > 0:
            if self.array[row][col].can_move:
              if self.array[row -1][col].color in ['R','B','G'] and self.array[row][col].color_goal == self.array[row -1][col].color_goal:
                    return True
        return False
    
    

    
    def move_up(self):
       
        for j in range(len(self.array[0])): 
          for i in range(len(self.array)- 1,0,-1):  
            if self.check_up(i, j):  
                    self.array[i][j].color = '0'  
                    self.array[i-1][j].can_move = True  
 
                    if self.array[i][j].color_goal == "red":
                        self.array[i-1][j].color_goal = "red"
                        self.array[i-1][j].color = 'r'
                    if self.array[i][j].color_goal == "blue":
                        self.array[i -1][j].color_goal = "blue"
                        self.array[i-1][j].color = 'b'
                    if self.array[i][j].color_goal == "green":
                        self.array[i -1][j].color_goal = "green"
                        self.array[i-1][j].color = 'g'
            if self.goal_up(i,j):
                       self.array[i -1][j].color = '0'
                       self.array[i][j].color='0'

           
        self.reset_moves()
        self.stack.append(self.copy())
        new_array = []
        for row in self.array:
          new_row = [square.copy() for square in row]  
          new_array.append(new_row)
        new_borad=Board(new_array)
        return new_borad
   
# جهة الأسفل
    def check_down(self, row, col):
        if row+1 < len(self.array):
             if self.array[row][col].can_move:
                if self.array[row+1][col].color =='0'  :
                    return True
        return False
    
    def goal_down(self, row, col):
        if row+1 < len(self.array):
             if self.array[row][col].can_move:
                if  self.array[row +1][col].color in ['R','B','G'] and self.array[row][col].color_goal == self.array[row+ 1][col].color_goal:
                    return True
        return False
   

   
    

    def move_down(self):
       
        for j in range(len(self.array[0])):  
         for i in range(len(self.array) -1):  
                if self.check_down(i, j):  
                    self.array[i][j].color = '0'  
                    self.array[i+1][j].can_move = True  

                    if self.array[i][j].color_goal == "red":
                        self.array[i +1][j].color_goal = "red"
                        self.array[i+1][j].color = 'r'
                    if self.array[i][j].color_goal =="blue":
                        self.array[i+1][j].color_goal = "blue"
                        self.array[i +1][j].color = 'b'
                    if self.array[i][j].color_goal == "green":
                        self.array[i +1][j].color_goal = "green"
                        self.array[i+1][j].color = 'g'
                if self.goal_down(i,j):
                       self.array[i +1][j].color = '0'
                       self.array[i][j].color='0'

               
        self.reset_moves()
        self.stack.append(self.copy())
        new_array = []
        for row in self.array:
          new_row = [square.copy() for square in row]  
        new_array.append(new_row)
        new_borad=Board(new_array)
        return new_borad
    


    def reset_moves(self):
        for row in self.array:
           for square in row:
             if square.color == '0':
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
              if square.color in ['R','G','B'] :
                  all_won =False
                  break
        if all_won:
         print("winner")
        else:
         print("not winner")
        return all_won

