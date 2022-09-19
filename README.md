Toy Robot
========

Overview
========
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units. There are
no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be
prevented from falling to destruction. Any movement that would result in the robot falling from the table must be
prevented, however further valid movement commands must still be allowed.

Features
========
Following commands can be given to the robot:

| Command       | Description                                      |
|---------------|--------------------------------------------------|
| `PLACE X,Y,F` | Place at coordinates X,Y facing direction F      |
| `MOVE`        | Move one unit in direction robot is facing       |
| `LEFT`        | Turn on the spot 90 degrees to the left          |
| `RIGHT`       | Turn on the spot 90 degrees to the right         |
| `REPORT`      | Print location and direction of robot to console |
| `Q`           | Quit the application                             |

Running
========

```shell
python ./toy_robot/main.py
```
