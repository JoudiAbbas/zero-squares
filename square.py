class Square :
   def __init__ (self,color,can_move=False,color_goal=""):
       self.color=color
       self.can_move=can_move
       self.color_goal=color_goal
       
   def copy(self):
         new_square = Square(self.color, self.can_move, self.color_goal) 
         return new_square
   
   






