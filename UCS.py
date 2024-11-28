
from heapq import heappush, heappop

def ucs(initial_board):
    visited = set()  
    priority_queue = []  
    heappush(priority_queue, (0, initial_board, "Initial_Board"))  
    visited_count = -1  

    while priority_queue:
        current_cost, current_board, move_name = heappop(priority_queue)
        board_state = tuple(tuple(square.color for square in row)
                             for row in current_board.array)
        if board_state in visited:
            continue
        visited.add(board_state)
        visited_count += 1
        print(f"{visited_count}:{move_name} (Cost: {current_cost})")
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
                print(f"{step}:{move}")
                board.print_board()
            print(f"💡 Total boards visited: {visited_count}")
            print(f"🎯 Total Steps in Solution : {len(solution_path) - 1}")
            return solution_path

        for move_name, next_board, move_cost in current_board.Next_state():
            next_board.parent = current_board  
            next_board.move_name = move_name 
            next_cost = current_cost + move_cost
            board_state = tuple(tuple(square.color for square in row) 
                                for row in next_board.array)
            if board_state not in visited:
                heappush(priority_queue, (next_cost, next_board, move_name))

    print("\nNo solution found.")
    print(f"Total boards visited: {visited_count}")
    return None