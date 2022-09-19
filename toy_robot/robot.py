import logging
from enum import Enum
from typing import Optional, NamedTuple

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# Boundaries for the 5x5 tabletop
MIN_TABLE_INDEX: int = 0
MAX_TABLE_INDEX: int = 4

# Used for turning robot, -1 to the left, 1 to the right
LEFT_WEIGHT = -1
RIGHT_WEIGHT = 1


class Coordinates(NamedTuple):
    """
    Represents X,Y coordinates
    """
    x: int
    y: int

    def __str__(self):
        return f"{self.x},{self.y}"


class Direction(Enum):
    """
    Directions that the robot can face
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


# Dictionaries of directions and the coordinates required to move in that direction
MOVE_COORD_WEIGHT: dict = {
    Direction.NORTH: Coordinates(0, 1),  # move 1 along the Y axis
    Direction.EAST: Coordinates(1, 0),  # move 1 along the X axis
    Direction.SOUTH: Coordinates(0, -1),  # move -1 along the Y axis
    Direction.WEST: Coordinates(-1, 0)  # move -1 along the X axis
}


class Robot:
    """
    Toy robot, that can be placed and moved around a tabletop.
    """

    def __init__(self):
        self.location: Optional[Coordinates] = None
        self.direction: Optional[Direction] = None

    def place(self, x: int, y: int, facing: Direction):
        """
        Place robot on the tabletop at given coordinates in the given direction.

        This command is ignored if the location is outside the bounds of the tabletop.

        :param x: X coordinate
        :param y: Y coordinate
        :param facing: direction robot is facing
        """
        if self.is_off_table(x, y):
            logger.debug("Ignoring PLACE {%s}, {%s}, {%s}", x, y, facing.value)
            return
        else:
            self.location = Coordinates(x, y)
            self.direction = facing

    def move(self):
        """
        Move robot forward 1 unit in whatever direction it is facing.

        This command is ignored if the robot ends up outside the bounds of the tabletop, or
        the robot has not been placed.
        """
        if not self.location:
            logger.debug("Robot not placed, ignoring MOVE")
            return
        else:
            coord_weight = MOVE_COORD_WEIGHT.get(self.direction)
            new_x, new_y = (self.location.x + coord_weight.x,
                            self.location.y + coord_weight.y)
            if self.is_off_table(new_x, new_y):
                logger.debug("Ignoring MOVE to {%s}, {%s}, {%s}", new_x, new_y, self.direction.value)
                return
            else:
                self.location = Coordinates(new_x, new_y)

    def left(self):
        """
        Rotate the robot on the spot 90 degrees to the left.

        This command is ignored if the robot has not been placed.
        """
        self._turn(LEFT_WEIGHT)

    def right(self):
        """
        Rotate the robot on the spot 90 degrees to the right.

        This command is ignored if the robot has not been placed.
        """
        self._turn(RIGHT_WEIGHT)

    def _turn(self, weight: int):
        """
        Rotate the robot to the next cardinal direction based on the given weight.
        Right turns NORTH -> EAST -> SOUTH -> WEST -> NORTH
        Left turns NORTH -> WEST -> SOUTH -> EAST -> NORTH

        This command is ignored if the robot has not been placed.

        :param weight: weight of turn (either left -1 or right 1)
        """
        if not self.direction:
            logger.debug("Robot not placed, ignoring TURN")
            return
        else:
            # use remainder to loop back round to North=0 or West=3
            new_direction = (self.direction.value + weight) % len(Direction)
            self.direction = Direction(new_direction)

    def report(self):
        """
        Print the current location of the robot in the format X,Y,DIRECTION

        This command is ignored if the robot has not been placed.
        """
        if not self.direction:
            return
        print(f"{self.location},{self.direction.name}")

    @staticmethod
    def is_off_table(x: int, y: int) -> bool:
        """
        Checks whether the given coordinates are outside the bounds of the table

        :return: is coordinates off the table
        """
        return x < MIN_TABLE_INDEX or y < MIN_TABLE_INDEX or x > MAX_TABLE_INDEX or y > MAX_TABLE_INDEX
