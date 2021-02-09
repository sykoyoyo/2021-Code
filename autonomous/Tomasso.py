#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Tommaso'

    def initialize(self):
        self.speed = 0.7

    @timed_state(duration=0.5, next_state='turn_right_first_ob', first=True)
    def drive_wait(self):
        self.myRobot.tankDrive(0,0)

    @timed_state(duration=1, next_state='backwards_second_ob')
    def turn_right_first_ob(self):
        self.myRobot.tankDrive(0.3, 0.8)

    """
    @timed_state(duration=1, next_state='little_right_second_ob')
    def stop_first_ob(self):
        self.myRobot.tankDrive(0, 0)

    @timed_state(duration=0.65, next_state='backwards_second_ob')
    def little_right_second_ob(self):
        self.myRobot.tankDrive(-0.6, 0.3)"""

    @timed_state(duration=2, next_state='backwards_right_second_ob')
    def backwards_second_ob(self):
        self.myRobot.tankDrive(- 0.7, - 0.7)

    @timed_state(duration=1.45, next_state='backwards_long_second_ob')
    def backwards_right_second_ob(self):
        self.myRobot.tankDrive(- 0.7, 0.45)

    @timed_state(duration=1.8, next_state='stop')
    def backwards_long_second_ob(self):
        self.myRobot.tankDrive(- 0.7, - 0.7)

    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)
