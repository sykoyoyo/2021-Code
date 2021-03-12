#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state
import wpilib

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Competition_Backup'

    def initialize(self):
        self.balls.set(wpilib.DoubleSolenoid.Value.kForward)

    @timed_state(duration=0.1, next_state='backwards', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)

    @timed_state(duration=1.5, next_state='stop_1')
    def backwards(self):
        self.myRobot.tankDrive(-0.7, -0.7)

    @timed_state(duration=0.2, next_state='spinmotors')
    def stop_1(self):
        self.myRobot.tankDrive(0, 0)

    @timed_state(duration=2, next_state='fire')
    def spinmotors(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.6)
        self.motor6.set(-.4)

    @timed_state(duration=5, next_state='Return')
    def fire(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.6)
        self.motor6.set(-.4)
        self.balls.toggle()

    @timed_state(duration=1.35)
    def Return(self):
        self.myRobot.tankDrive(-.5, -.5)
        self.motor5.set(0)
        self.motor6.set(0)
        self.balls.toggle()
