#!/usr/bin/env python3
#hello
from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Anders'

    def initialize(self):

        self.speed = -.4

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)

    @timed_state(duration=1.7, next_state='turn_left')
    def drive_forward(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=2, next_state='turn_right')
    def turn_left(self):
        self.myRobot.tankDrive(.8, .6)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
