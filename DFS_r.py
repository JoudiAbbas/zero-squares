def Dfs(board):
        visited = set()  
        visited_count = -1
        current_board = board 
        board_state = tuple(tuple(square.color for square in row)
                             for row in current_board.array)
        if board_state not in  visited:
         visited.add(board_state)
         visited_count += 1
        print({visited_count})
        current_board.print_board()

        if current_board.check_win():
            print("🏆 Solution Found!")
            solution_path = []
            while current_board:
                solution_path.append((current_board))
                current_board = current_board.parent
                if current_board: 
                    move_name = current_board.move_name
            
            print(f"💡 Total boards visited: {visited_count}")
            print(f"🎯 Total Steps in Solution : {len(solution_path) - 1}")
            return solution_path
            
            

        for move, next_board in current_board.Next_state():
             next_board.parent = current_board  
             next_board.move_name = move 
             Dfs(next_board)
            
        print("\nNo solution found.")
        print(f"Total boards visited: {visited_count}")
        return None


