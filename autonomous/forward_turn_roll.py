#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Forward Turn intake'

    def initialize(self):
        pass

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)
        self.motor5.set(0)

    @timed_state(duration=1, next_state='drive_right')
    def drive_forward(self):
        self.myRobot.tankDrive(.7, .7)
        self.motor5.set(.5)


    @timed_state(duration=1, next_state='stop')
    def drive_right(self):
        self.myRobot.tankDrive(0, .7)
        self.motor5.set(0)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
        self.motor5.set(0)
