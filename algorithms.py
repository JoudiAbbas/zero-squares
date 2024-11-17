from collections import deque

# DFS
def Dfs(board):
     stack = [(board, "Initial_Board")] 
     visited = set()  
     visited_count = -1

     while stack:
        current_board, move_name = stack.pop()
        board_state = tuple(tuple(square.color for square in row)
                             for row in current_board.array)
        if board_state in visited:
            continue
        visited.add(board_state)
        visited_count += 1

        print(f"{visited_count}: {move_name}")
        current_board.print_board()

        if current_board.check_win():
            print("🏆 Solution Found!")
            solution_path = []
            while current_board:
                solution_path.append((current_board, move_name))
                current_board = current_board.parent
                if current_board: 
                    move_name = current_board.move_name
            solution_path.reverse()
            for step, (board, move) in enumerate(solution_path):
                print(f"Step {step} {move}:")
                board.print_board()
            print(f"💡 Total boards visited: {visited_count}")
            print(f"🎯 Total Steps in Solution : {len(solution_path) - 1}")
            return solution_path

        for move, next_board in current_board.Next_state():
            next_board.parent = current_board  
            next_board.move_name = move 
            stack.append((next_board, move))

     print("\nNo solution found.")
     print(f"Total boards visited: {visited_count}")
     return None




# BFS
def Bfs(board):
     queue = deque([(board,"Initial_Board")]) 
     visited = set()   
     visited_count = -1  
     initial_state = tuple(tuple(square.color for square in row)
                          for row in board.array)
     visited.add(initial_state)

     while queue:
        current_board, move_name = queue.popleft()
        visited_count += 1
        print(f"{visited_count}: {move_name}")
        current_board.print_board()


        if current_board.check_win():
            print("🏆 Solution Found!")
            solution_path = []
            while current_board:
                solution_path.append((current_board, move_name))
                current_board = current_board.parent
                if current_board: move_name = current_board.move
            solution_path.reverse()

            for step, (board, move) in enumerate(solution_path):
                print(f"Step {step}:{move}")
                board.print_board()
            print(f"💡 Total boards visited: {visited_count}")
            print(f"🎯 Total Steps in Solution : {len(solution_path) - 1}")
            return solution_path

        for move, next_board in current_board.Next_state():
            board_state = tuple(tuple(square.color for square in row)
                                for row in next_board.array)
            if board_state not in visited:
                visited.add(board_state)
                next_board.parent = current_board 
                next_board.move = move 
                queue.append((next_board, move))

     print("\nNo solution found.")
     print(f"Total boards visited:{visited_count}")
     return None


