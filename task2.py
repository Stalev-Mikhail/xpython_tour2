#бажано, але не обов'язково запускати в консолі Windows
import pygame
import sys

pygame.init()

CELL_SIZE = 90
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def solve_maze(maze, x, y, end, visited):
    if (x, y) == end:
        return [(x, y)]
    if not is_safe(maze, x, y) or (x, y) in visited:
        return None

    visited.add((x, y))
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        path = solve_maze(maze, x + dx, y + dy, end, visited)
        if path:
            return [(x, y)] + path
    visited.remove((x, y))
    return None

def draw_maze(surface, maze, path, current_step):
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            color = BLACK if cell == 1 else WHITE
            pygame.draw.rect(surface, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if path:
        for px, py in path[:-1]:
            pygame.draw.rect(surface, GREEN, (py * CELL_SIZE, px * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if current_step < len(path):
            px, py = path[current_step]
            pygame.draw.rect(surface, RED, (py * CELL_SIZE, px * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    maze = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
    ]

    start = (int(input("Введiть координату x: ")), int(input("Введiть координату y: ")))
    end = (int(input("Введiть координату x цiлi: ")), int(input("Введiть координату y цiлi: ")))

    path = solve_maze(maze, *start, end, set())
    screen = pygame.display.set_mode((len(maze[0]) * CELL_SIZE, len(maze) * CELL_SIZE))
    pygame.display.set_caption("Розв'язувач лабiринтів")

    clock = pygame.time.Clock()
    current_step = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_maze(screen, maze, path, current_step)
        pygame.display.flip()

        if path and current_step < len(path):
            current_step += 1
        clock.tick(5)

if __name__ == "__main__":
    main()
