
class Square:
    def __init__(self,color,can_move=False, color_goal="",is_goal=False,original_color=None,original_color_goal=None):
        self.color = color 
        self.can_move = can_move  
        self.color_goal = color_goal  
        self.is_goal=is_goal
        self.original_color = color if original_color is None else original_color 
        self.is_temp_occupied = False 
        self.original_color_goal=color_goal if original_color_goal is None else original_color_goal

    def copy(self):
        new_square = Square(
            self.color,
            self.can_move,
            self.color_goal,
            self.original_color
        )
        new_square.is_temp_occupied = self.is_temp_occupied
        new_square.original_color_goal = self.original_color_goal
        return new_square





