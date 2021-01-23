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

    @timed_state(duration=1, next_state='turn_left')
    def drive_forward(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=3, next_state='turn_right')
    def turn_left(self):
        self.myRobot.tankDrive(.8, 0)

    @timed_state(duration=4, next_state='turn_left2')
    def turn_right(self):
        self.myRobot.tankDrive(0, .8)

    @timed_state(duration=3, next_state='drive_forward2')
    def turn_left2(self):
        self.myRobot.tankDrive(.8, 0)

    @timed_state(duration=4, next_state='turn_right2')
    def drive_forward2(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=1, next_state='drive_forward3')
    def turn_right2(self):
        self.myRobot.tankDrive(0, .8)

    @timed_state(duration=0.5, next_state='stop')
    def drive_forward3(self):
        self.myRobot.tankDrive(.8, .8)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
