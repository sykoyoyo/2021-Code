#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state
import wpilib

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Competition_Backup'

    def initialize(self):
        pass

    @timed_state(duration=0.2, next_state='backwards', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)
        self.balls.set(wpilib.DoubleSolenoid.Value.kForward)
        self.intake.set(wpilib.DoubleSolenoid.Value.kReverse)


    @timed_state(duration=1, next_state='stop_1')
    def backwards(self):
        self.myRobot.tankDrive(-0.9, -0.9)

    @timed_state(duration=0.2, next_state='spinmotors')
    def stop_1(self):
        self.myRobot.tankDrive(0, 0)


    @timed_state(duration=1.3, next_state='fire')
    def spinmotors(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.75)
        self.motor6.set(-.5)

    @timed_state(duration=2, next_state='Return')
    def fire(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.75)
        self.motor6.set(-.5)
        self.balls.set(wpilib.DoubleSolenoid.Value.kReverse)

    @timed_state(duration=.8, next_state='more')
    def Return(self):
        self.myRobot.tankDrive(-.25, -.75)
        self.motor5.set(0)
        self.motor6.set(0)
        self.balls.set(wpilib.DoubleSolenoid.Value.kForward)
        self.intake.set(wpilib.DoubleSolenoid.Value.kForward)

    @timed_state(duration=1.75, next_state='collect')
    def more(self):
        self.myRobot.tankDrive(.65, .65)
        self.motor5.set(.15)

    @timed_state(duration=1.15, next_state='stop2')
    def collect(self):
        self.myRobot.tankDrive(-.75, -.25)
        self.motor5.set(.15)

    @timed_state(duration=0.88, next_state='stop3')
    def stop2(self):
        self.myRobot.tankDrive(.5, .5)
        self.motor5.set(.15)
        self.intake.set(wpilib.DoubleSolenoid.Value.kReverse)

    @timed_state(duration=0.5, next_state='spinmotors2')
    def stop3(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(0)

    @timed_state(duration=2, next_state='fire2')
    def spinmotors2(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.8)
        self.motor6.set(-.6)

    @timed_state(duration=2, next_state='end')
    def fire2(self):
        self.myRobot.tankDrive(0, 0)
        self.motor5.set(.8)
        self.motor6.set(-.6)
        self.balls.set(wpilib.DoubleSolenoid.Value.kReverse)

    @timed_state(duration=.95)
    def end(self):
        self.myRobot.tankDrive(-.6, -.3)
        self.motor5.set(0)
        self.motor6.set(0)
        self.balls.set(wpilib.DoubleSolenoid.Value.kForward)
        self.intake.set(wpilib.DoubleSolenoid.Value.kReverse)
