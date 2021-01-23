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
        #self.motor5 = ctre.TalonFX(5)
        self.joy = wpilib.Joystick(0)

        #self.arm = wpilib.Solenoid(1)

        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

        self.myRobot = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)


        self.components = {
            'myRobot': self.myRobot,
            #'motor5': self.motor5,
            #'arm': self.arm
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

        self.myRobot.arcadeDrive(-1*self.joy.getRawAxis(1), self.joy.getRawAxis(0))
        """
        if self.joy.getAButton():
            self.arm.set(True)
            self.motor5.set(.25)
        else:
            self.arm.set(False)
            if self.joy.getXButton():
                self.motor5.set(-1)
            else:
                self.motor5.set(0)
                    """

if __name__ == "__main__":
    wpilib.run(MyRobot)
