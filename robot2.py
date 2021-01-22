#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
import ctre

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor1 = ctre.WPI_TalonSRX(1)
        self.left_motor2 = ctre.WPI_TalonSRX(2)
        self.right_motor1 = ctre.WPI_TalonSRX(3)
        self.right_motor2 = ctre.WPI_TalonSRX(4)
        
        self.left = wpilib.SpeedControllerGroup(self.left_motor1, self.left_motor2)
        self.right = wpilib.SpeedControllerGroup(self.right_motor1, self.right_motor2)
        
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.stick = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)
