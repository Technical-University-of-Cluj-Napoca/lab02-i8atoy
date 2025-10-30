def read_maze(filename: str) -> list[list[str]]:

    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


def find_start_and_target(maze: list[list[str]]) -> tuple[tuple, tuple]:
    

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                S_coordinates = (i, j)
            elif maze[i][j] == 'T':
                T_coordinates = (i, j)
    
    return (S_coordinates, T_coordinates)


    
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    pass



def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    # construct the direction array: list[tuple[int, int]] (up, down, left, right)
    # test the position in each direction
    neighbors = []
    if maze[position[0] + 1,position[1]] == '*':
        north = (position[0] + 1, position[1])
        neighbors.append(north)
    if maze[position[0] - 1,position[1]] == '*':
        south = (position[0] - 1, position[1])
        neighbors.append(south)
    if maze[position[0],position[1] + 1] == '*':
        east = (position[0], position[1] + 1)
        neighbors.append(east)
    if maze[position[0], position[1] - 1] == '*':
        west = (position[0], position[1] - 1)   
        neighbors.append(west) 

    pass



def bfs(grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Breadth-First Search (BFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    
    if start == None or end == None:
        return False
    
    from collections import deque

    queue = deque()
    queue.append(start)
    visited = {start}
    camefrom = {}

    while len(queue):
        # if quit:
        #     pygame.quit()
        current = queue.popleft()
        if current == end:
            while current in camefrom:
                current = camefrom[current]
                current.make_path()
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                camefrom[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()

        if current != start:
            current.make_closed()
        
        
    return False



def dfs(grid: Grid, start: Spot, end: Spot) -> bool:
    """
    Depth-First Search (DFS) Algorithm.
    Args:
        draw (callable): A function to call to update the Pygame window.
        grid (Grid): The Grid object containing the spots.
        start (Spot): The starting spot.
        end (Spot): The ending spot.
    Returns:
        bool: True if a path is found, False otherwise.
    """
    if start == None or end == None:
        return False
    
    stack = [start]
    visited = {start}
    camefrom = {}

    while len(stack):
        current = stack.pop()
        if current == end:
            while current in camefrom:
                current = camefrom[current]
                current.make_path()

            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                visited.add(neighbor)
                camefrom[neighbor] = current
                stack.append(neighbor)
                neighbor.make_open()
        if current != start:
            current.make_closed()
    return False

    pass



def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # # ANSI escape code for red
    # RED = "\033[91m"
    # RESET = "\033[0m"
    # encode a character with red color: RED + char + RESET
    pass



if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt


    print(read_maze("maze1.txt"))
    
    pass