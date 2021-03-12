#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state
import wpilib

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Blue Path B'

    def initialize(self):

        self.speed = -.4
        self.intake.set(wpilib.DoubleSolenoid.Value.kForward)

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)
        self.intake.set(wpilib.DoubleSolenoid.Value.kForward)

    @timed_state(duration=2.5, next_state='turn_left')
    def drive_forward(self):
        self.myRobot.tankDrive(.8,.8)
        self.motor5.set(.15)

    @timed_state(duration=1, next_state='drive_forward2')
    def turn_left(self):
        self.myRobot.tankDrive(.5,.8)

    @timed_state(duration=.5, next_state='turn_right')
    def drive_forward2(self):
        self.myRobot.tankDrive(.8,.8)

    @timed_state(duration=1, next_state='drive_forward3')
    def turn_right(self):
        self.myRobot.tankDrive(.8,.5)

    @timed_state(duration=1.5, next_state='turn_right2')
    def drive_forward3(self):
        self.myRobot.tankDrive(.8,.8)

    @timed_state(duration=1, next_state='drive_forward4')
    def turn_right2(self):
        self.myRobot.tankDrive(.8,.5)

    @timed_state(duration=1.5, next_state='turn_left2')
    def drive_forward4(self):
        self.myRobot.tankDrive(.8,.8)

    @timed_state(duration=1, next_state='drive_forward5')
    def turn_left2(self):
        self.myRobot.tankDrive(.5,.8)

    @timed_state(duration=.5, next_state='stop')
    def drive_forward5(self):
        self.myRobot.tankDrive(.8,.8)
