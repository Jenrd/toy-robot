import logging
from typing import Optional

from robot import Robot, Direction

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

REPORT_COMMAND = "REPORT"
RIGHT_COMMAND = "RIGHT"
LEFT_COMMAND = "LEFT"
MOVE_COMMAND = "MOVE"
PLACE_COMMAND = "PLACE"

QUIT_CHAR = "Q"

SPACE_DELIMITER = " "
COMMA_DELIMITER = ","


def robot_controller():
    """
    Main Entry Point - Robot controller, takes user inputs as commands to move robot around a 5x5 table,
    ignores invalid commands.
    """
    logger.info("Robot Controller starting...")
    robot: Robot = Robot()
    command: Optional[str] = None

    while command != QUIT_CHAR:
        # make command UPPERCASE and strip whitespace
        user_input = input("Input Command: ").upper().strip()
        try:
            input_parts = user_input.split(SPACE_DELIMITER)
            command = input_parts[0]
            if len(input_parts) == 2 and command == PLACE_COMMAND:  # PLACE
                # Split out coordinates and direction
                x, y, direction = input_parts[1].split(COMMA_DELIMITER)
                robot.place(int(x), int(y), Direction[direction])
            elif len(input_parts) == 1:
                if command == MOVE_COMMAND:  # MOVE
                    robot.move()
                elif command == LEFT_COMMAND:  # LEFT
                    robot.left()
                elif command == RIGHT_COMMAND:  # RIGHT
                    robot.right()
                elif command == REPORT_COMMAND:  # REPORT
                    robot.report()
        except Exception as e:
            # If user passes something we can't parse log error at debug level and move on
            logger.debug(str(e))

    logger.info("Shutting down Robot Controller...")


if __name__ == '__main__':
    robot_controller()
