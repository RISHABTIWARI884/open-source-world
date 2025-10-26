import random

def generate_maze(width=15, height=10):
    maze = [["#"]*width for _ in range(height)]
    for i in range(1, height-1):
        for j in range(1, width-1):
            maze[i][j] = " " if random.random() > 0.3 else "#"
    # Entrance and exit
    maze[0][1] = " "
    maze[height-1][width-2] = " "
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    maze = generate_maze()
    print_maze(maze)
