# Alexander Baldree
# Robert Breutzmann
# Maksymilian Jankowski
# Carolina Rodriguez
# Matthew Rozendaal
# 11/13/2025
# Module 6.2

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'  #  New water symbol

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
INITIAL_WATER_DENSITY = 0.10  #  Amount of water that starts on the map.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # Already updated this space.

                cell = forest[(x, y)]

                if cell == WATER:
                    #  Water never changes.
                    nextForest[(x, y)] = WATER

                elif (cell == EMPTY) and (random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE

                elif (cell == TREE) and (random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif cell == FIRE:
                    # This tree is currently burning.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = forest.get((x + ix, y + iy))
                            if neighbor == TREE:
                                # Fire spreads only to trees, not water.
                                nextForest[(x + ix, y + iy)] = FIRE
                    # Burned down → empty space.
                    nextForest[(x, y)] = EMPTY

                else:
                    # Just copy the existing object.
                    nextForest[(x, y)] = cell

        forest = nextForest
        time.sleep(PAUSE_LENGTH)

def CreateWaterInForest(forest):
    """Adds water to the forest based on INITIAL_WATER_DENSITY.
    ️    Returns the updated forest dictionary.
    ️    The water is placed starting from the center of the forest
        and expanding outwards in random directions.
    """
    total_cells = WIDTH * HEIGHT
    # Find middle of forest
    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2
    expected_water_cells = int(total_cells * INITIAL_WATER_DENSITY)

    # Place water cells around the center
    # randomly until we reach the expected number of water cells
    current_x = mid_x
    current_y = mid_y

    direction = 0  # 0: right, 1: down, 2: left, 3: up

    water_cells_placed = 0

    while water_cells_placed < expected_water_cells:

        # Get new direction
        direction = random.randint(0, 3)
        if direction == 0:  # Move right
            current_x += 1
        elif direction == 1:  # Move down
            current_y += 1
        elif direction == 2:  # Move left
            current_x -= 1
        elif direction == 3:  # Move up
            current_y -= 1

        # Ensure we stay within bounds
        current_x = max(0, min(WIDTH - 1, current_x))
        current_y = max(0, min(HEIGHT - 1, current_y))

        # Place water if the cell is empty
        if (current_x, current_y) in forest:
            continue  # Already assigned (water).
        forest[(current_x, current_y)] = WATER
        water_cells_placed += 1
    return forest


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    forest = CreateWaterInForest(forest)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            rand = random.random
            ()
            if (x, y) in forest:
                continue  # Already assigned (water).
            elif rand < INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
            elif cell == FIRE:
                bext.fg('red')
            elif cell == WATER:
                bext.fg('blue')
            else:
                bext.fg('reset')
            print(cell, end='')
        print()
    bext.fg('reset')  # Reset font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print(' Water density: {}%  '.format(INITIAL_WATER_DENSITY * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
