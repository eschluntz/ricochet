BOARD_SIZE = 16
DEBUG = True

# (X, Y) location robot is trying to get to
default_goal = (6,1)
default_robot = "red"

# dict from robot color to (x,y) tuple
starting_robots = {
    "red": (0,0), 
    "green":(6,3), 
    "blue":(1,6), 
    "yellow":(10,10)
}

# x, y tuples
# we use .5 to denote a wall between two spaces for the robot
global_walls = [
    (3.5, 0),  # all vertical walls
    (13.5, 0),
    (10.5, 1),
    (3.5, 2),
    (1.5, 3),
    (14.5, 3),
    (5.5, 4),
    (3.5, 5),
    (10.5, 5),
    (11.5, 6),
    (6.5, 7),
    (8.5, 7),
    (6.5, 8),
    (8.5, 8),
    (1.5, 9),
    (11.5, 9),
    (5.5, 10),
    (3.5, 11),
    (9.5, 11),
    (14.5, 12),
    (7.5, 13),
    (4.5, 14),
    (10.5, 14),
    (2.5, 15),
    (8.5, 15),
    
    (0, 5.5),  # all horizontal walls
    (0, 11.5),
    (1, 9.5),
    (2, 2.5),
    (3, 4.5),
    (3, 10.5),
    (4, 2.5),
    (5, 4.5),
    (5, 13.5),
    (6, 10.5),
    (7, 6.5),
    (7, 8.5),
    (7, 12.5),
    (8, 6.5),
    (8, 8.5),
    (9, 10.5),
    (10, 4.5),
    (11, 0.5),
    (11, 14.5),
    (12, 6.5),
    (12, 8.5),
    (14, 3.5),
    (14,12.5),
    (15,5.5),
    (15, 13.5)
]