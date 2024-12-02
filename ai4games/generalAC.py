import sys, random
import pygame
import numpy as np

# Settings
__screenSize__ = (900, 900)
__cellSize__ = 10
__gridDim__ = tuple(map(lambda x: int(x / __cellSize__), __screenSize__))
__colors__ = {
    0: (0, 0, 255),  # Water
    1: (194, 178, 128),  # Sand
    2: (34, 139, 34),  # Grass
}

def getColorCell(n):
    return __colors__[n]

class Grid:
    def __init__(self):
        # Start with random noise
        self._grid = np.random.choice([0, 2], size=__gridDim__, p=[0.7, 0.3])
        self._gridbis = np.zeros_like(self._grid)

    def update(self):
        """Smoothly evolve land and define borders."""
        for (x, y), _ in np.ndenumerate(self._grid):
            neighbors = [self._grid[vx, vy] for vx, vy in self.neighbor_indices(x, y)]
            if self._grid[x, y] == 0:  # Water
                if neighbors.count(2) > 2:
                    self._gridbis[x, y] = 1  # Become sand
                else:
                    self._gridbis[x, y] = 0
            elif self._grid[x, y] == 1:  # Sand
                if neighbors.count(2) >= 4:
                    self._gridbis[x, y] = 2  # Become grass
                elif neighbors.count(0) >= 4:
                    self._gridbis[x, y] = 0  # Revert to water
                else:
                    self._gridbis[x, y] = 1
            elif self._grid[x, y] == 2:  # Grass
                if neighbors.count(0) >= 4:
                    self._gridbis[x, y] = 1  # Revert to sand
                else:
                    self._gridbis[x, y] = 2
        self._grid = np.copy(self._gridbis)

    def neighbor_indices(self, x, y):
        """Get valid neighbor indices."""
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [(x + dx, y + dy) for dx, dy in offsets if 0 <= x + dx < __gridDim__[0] and 0 <= y + dy < __gridDim__[1]]

class Scene:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(__screenSize__)
        pygame.display.set_caption("Land Formation")
        self._grid = Grid()
        self._font = pygame.font.SysFont('Arial', 25)

    def draw(self):
        """Draw the grid."""
        self._screen.fill((255, 255, 255))
        for x in range(__gridDim__[0]):
            for y in range(__gridDim__[1]):
                pygame.draw.rect(self._screen, getColorCell(self._grid._grid[x, y]),
                                 (x * __cellSize__ + 1, y * __cellSize__ + 1, __cellSize__ - 2, __cellSize__ - 2))
        pygame.display.flip()

    def update(self):
        self._grid.update()

def main():
    scene = Scene()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene.update()
        scene.draw()
        clock.tick(10)  # Adjust frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
