def Dfs_recursive(board, visited=None, move_name="Initial_Board", parent=None, visited_count=[-1]):
    if visited is None:
        visited = set()
    board_state = tuple(tuple(square.color for square in row)
                        for row in board.array)
    if board_state in visited:
        return None

    visited.add(board_state)
    visited_count[0] += 1
    print(f"{visited_count[0]}:{move_name}")
    board.print_board()

    if board.check_win():
        print("🏆 Solution Found!")
        solution_path = []
        while board:
            solution_path.append((board, move_name))
            board = board.parent
            if board:
                move_name = board.parent_move 
        solution_path.reverse()
        for step, (board, move) in enumerate(solution_path):
            print(f"{step}:{move}")
            board.print_board()
        print(f"💡 Total boards visited: {visited_count[0]}")
        print(f"🎯 Total Steps in Solution : {len(solution_path) - 1}")
        return solution_path

    board.parent = parent
    board.parent_move = move_name

    for move, next_board in board.Next_state():
        solution = Dfs_recursive(next_board, visited, move, board, visited_count)
        if solution:  
            return solution

    return None


