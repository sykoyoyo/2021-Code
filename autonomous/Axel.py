#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Axel'

    def initialize(self):

        self.speed = -.4

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)

    @timed_state(duration=4, next_state='stop')
    def drive_forward(self):
        self.myRobot.tankDrive(1, 1)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
