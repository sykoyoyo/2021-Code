#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

<<<<<<< HEAD
    MODE_NAME = 'Drive anders'
=======
    MODE_NAME = 'Drive Anders'
>>>>>>> 2add47de88fffd73fbff2409cd7e7590d958ac63

    def initialize(self):

        self.speed = -.4

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)

    @timed_state(duration=1, next_state='turn_left')
    def drive_forward(self):
        self.myRobot.tankDrive(.8, .8)

<<<<<<< HEAD
    @timed_state(duration=1, next_state='turn_right')
=======
    @timed_state(duration=2, next_state='turn_right')
>>>>>>> 2add47de88fffd73fbff2409cd7e7590d958ac63
    def turn_left(self):
        self.myRobot.tankDrive(.8, 0)

    @timed_state(duration=1, next_state='turn_right2')
    def turn_right(self):
        self.myRobot.tankDrive(0, .8)

    @timed_state(duration=1, next_state='stop')
<<<<<<< HEAD
    def turn_right2(self):
=======
    def turn_right(self):
>>>>>>> 2add47de88fffd73fbff2409cd7e7590d958ac63
        self.myRobot.tankDrive(0, .8)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
