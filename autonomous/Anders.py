#!/usr/bin/env python3
#helloperson
from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Anders'

    def initialize(self):

        self.speed = -.4

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0, 0)

    @timed_state(duration=1.28, next_state='turn_right')
    def drive_forward(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=2.8, next_state='drive_forward2')
    def turn_right(self):
        self.myRobot.tankDrive(.8, .48)

    @timed_state(duration=1.1, next_state='turn_left')
    def drive_forward2(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=2.15, next_state='drive_forward3')
    def turn_left(self):
        self.myRobot.tankDrive(.5, .8)

    @timed_state(duration=0.9, next_state='turn_left2')
    def drive_forward3(self):
        self.myRobot.tankDrive(.8, .8)

    @timed_state(duration=1.78, next_state='drive_forward4')
    def turn_left2(self):
        self.myRobot.tankDrive(.5, .8)

    @timed_state(duration=1.77, next_state='stop')
    def drive_forward4(self):
        self.myRobot.tankDrive(1, 1)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0, 0 )
