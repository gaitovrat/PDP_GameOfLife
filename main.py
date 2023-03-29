import pygame
import numpy as np

CELL_SIZE = 8
WIDTH = 120
HEIGHT = 90
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


def update(surface: pygame.Surface, cells: np.ndarray) -> np.ndarray:
    next = np.zeros((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        num_alive = np.sum(
            cells[row-1:row+2, column-1:column+2]) - cells[row, column]

        if cells[row, column] == 1 and num_alive < 2 or num_alive > 3:
            color = COLOR_WHITE
        elif (cells[row, column] == 1 and 2 <= num_alive <= 3) or (cells[row, column] == 0 and num_alive == 3):
            next[row, column] = 1
            color = COLOR_BLACK

        color = color if cells[row, column] == 1 else COLOR_WHITE
        pygame.draw.rect(surface, color, (column * CELL_SIZE,
                         row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

    return next


def main():
    pygame.init()
    pygame.display.set_caption("Game of life")

    surface = pygame.display.set_mode((CELL_SIZE * WIDTH, CELL_SIZE * HEIGHT))
    cells = np.zeros((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0] // CELL_SIZE

                cells[x] = 1

        cells = update(surface, cells)
        pygame.display.update()


if __name__ == '__main__':
    main()
