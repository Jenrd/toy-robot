from unittest import TestCase

from toy_robot.robot import Robot, Direction, Coordinates


class TestRobot(TestCase):
    def test_right(self):
        # Arrange
        robot: Robot = Robot()
        robot.direction = Direction.NORTH

        # Act
        robot.right()
        # Assert
        self.assertEqual(Direction.EAST, robot.direction)

        # Act
        robot.right()
        # Assert
        self.assertEqual(Direction.SOUTH, robot.direction)

        # Act
        robot.right()
        # Assert
        self.assertEqual(Direction.WEST, robot.direction)

        # Act
        robot.right()
        # Assert
        self.assertEqual(Direction.NORTH, robot.direction)

    def test_left(self):
        # Arrange
        robot: Robot = Robot()
        robot.direction = Direction.WEST

        # Act
        robot.left()
        # Assert
        self.assertEqual(Direction.SOUTH, robot.direction)

        # Act
        robot.left()
        # Assert
        self.assertEqual(Direction.EAST, robot.direction)

        # Act
        robot.left()
        # Assert
        self.assertEqual(Direction.NORTH, robot.direction)

        # Act
        robot.left()
        # Assert
        self.assertEqual(Direction.WEST, robot.direction)

    def test_is_off_table_false(self):
        for x in range(0, 5):
            for y in range(0, 5):
                self.assertFalse(Robot.is_off_table(x, y), f"Expected coordinate {x}, {y} to be on the table")

    def test_is_off_table_true(self):
        for x in [-2, -1, 5, 6]:
            for y in range(-2, 7):
                self.assertTrue(Robot.is_off_table(x, y), f"Expected coordinate {x}, {y} to be off the table")

        for x in range(-2, 7):
            for y in [-2, -1, 5, 6]:
                self.assertTrue(Robot.is_off_table(x, y), f"Expected coordinate {x}, {y} to be off the table")

    def test_move_north(self):
        # Arrange
        robot: Robot = Robot()
        robot.place(2, 0, Direction.NORTH)

        # Act / Assert
        for i in range(1, 5):
            robot.move()
            self.assertEqual(Coordinates(2, i), robot.location)
            self.assertEqual(Direction.NORTH, robot.direction)

        # Act
        robot.move()

        # Assert
        self.assertEqual(Coordinates(2, 4), robot.location)
        self.assertEqual(Direction.NORTH, robot.direction)

    def test_move_east(self):
        # Arrange
        robot: Robot = Robot()
        robot.place(0, 1, Direction.EAST)

        # Act / Assert
        for i in range(1, 5):
            robot.move()
            self.assertEqual(Coordinates(i, 1), robot.location)
            self.assertEqual(Direction.EAST, robot.direction)

        # Act
        robot.move()

        # Assert
        self.assertEqual(Coordinates(4, 1), robot.location)
        self.assertEqual(Direction.EAST, robot.direction)

    def test_move_south(self):
        # Arrange
        robot: Robot = Robot()
        robot.place(3, 4, Direction.SOUTH)

        # Act / Assert
        for i in range(3, -1, -1):
            robot.move()
            self.assertEqual(Coordinates(3, i), robot.location)
            self.assertEqual(Direction.SOUTH, robot.direction)

        # Act
        robot.move()

        # Assert
        self.assertEqual(Coordinates(3, 0), robot.location)
        self.assertEqual(Direction.SOUTH, robot.direction)

    def test_move_west(self):
        # Arrange
        robot: Robot = Robot()
        robot.place(4, 0, Direction.WEST)

        # Act / Assert
        for i in range(3, -1, -1):
            robot.move()
            self.assertEqual(Coordinates(i, 0), robot.location)
            self.assertEqual(Direction.WEST, robot.direction)

        # Act
        robot.move()

        # Assert
        self.assertEqual(Coordinates(0, 0), robot.location)
        self.assertEqual(Direction.WEST, robot.direction)

    def test_place_on_table(self):
        # Arrange
        robot: Robot = Robot()
        for direction in Direction:
            for x in range(0, 5):
                for y in range(0, 5):
                    # Act
                    robot.place(x, y, direction)

                    # Assert
                    self.assertEqual(Coordinates(x, y), robot.location)
                    self.assertEqual(direction, robot.direction)

    def test_place_off_table(self):
        # Arrange
        robot: Robot = Robot()

        for direction in Direction:
            for x in [-2, -1, 5, 6]:
                for y in range(-2, 7):
                    # Act
                    robot.place(x, y, direction)

                    # Assert
                    self.assertIsNone(robot.location)
                    self.assertIsNone(robot.direction)

            for x in range(-2, 7):
                for y in [-2, -1, 5, 6]:
                    # Act
                    robot.place(x, y, direction)

                    # Assert
                    self.assertIsNone(robot.location)
                    self.assertIsNone(robot.direction)
