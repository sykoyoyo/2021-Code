#!/usr/bin/env python3

import wpilib
from wpilib.drive import DifferentialDrive
import ctre
import wpilib.drive
from robotpy_ext.autonomous import AutonomousModeSelector



class MyRobot(wpilib.TimedRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):


        self.motor1 = ctre.WPI_TalonSRX(1)  # Initialize the TalonSRX on device 1.
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)
        self.joy = wpilib.XboxController(0)

        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

        self.myRobot = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        self.components = {
            'myRobot': self.myRobot,
        }

        self.automodes = AutonomousModeSelector('autonomous', self.components)


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.automodes.run()


    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)


    def teleopPeriodic(self):
        """Runs Robot on Tank Drive like a skid steer, two joysticks"""

        self.myRobot.arcadeDrive(self.joy.getY(), self.joy.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)
