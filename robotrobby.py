#!/usr/bin/env python3

import wpilib
from wpilib.drive import DifferentialDrive
import ctre
import wpilib.drive
import
import wpilib.buttons


class MyRobot(wpilib.TimedRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):


        self.left1 = ctre.WPI_TalonSRX(1)  # Initialize the TalonSRX on device 1.
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)
        self.joy = wpilib.Joystick(0)

        self.left = wpilib.SpeedControllerGroup(self.left1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

        self.myRobot = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)


        self.topshooter = ctre.WPI_TalonSRX(5)
        self.bottomshooter = ctre.WPI_TalonSRX(6)

        self.shoot = wpilib.buttons.JoystickButton(self.joy, 3)



    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""

        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if (self.timer<2):
            self.myRobot.tankDrive(-0.5, -0.5, True)
        elif (2<self.timer<4):
            self.myRobot.tankDrive(0, -0.5, True)
        else:
            self.myRobot.tankDrive(0, 0, True)


    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)


    def teleopPeriodic(self):
        """Runs Robot on Tank Drive like a skid steer, two joysticks"""

        self.myRobot.arcadeDrive(self.joy.getRawAxis(1), self.joy.getRawAxis(0), True)

        if (self.shoot.get()):
            self.topshooter.set(.75, True)
            self.bottomshooter.set(-.75, True)
        else:
            self.topshooter.set(0)
            self.bottomshooter.set(0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
