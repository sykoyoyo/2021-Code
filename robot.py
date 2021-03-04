#!/usr/bin/env python3

import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.drive
import ctre
from robotpy_ext.autonomous import AutonomousModeSelector


#Import is pulling all the libraries and API's you need for your code,
#The most common ones are posted above that we will use for now.


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        wpilib.CameraServer.launch() #launch webcam CameraServer
        #Drive Motors
        self.motor1 = ctre.WPI_TalonSRX(1)  # Initialize the TalonSRX on device 1.
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        self.motor5 = ctre.WPI_TalonFX(5)   #intake Motor

        self.motor6 = ctre.WPI_TalonFX(6)   #Shooter Motor

        self.motor7 = ctre.WPI_VictorSPX(7) #Intake Arm

        self.motor8 = ctre.WPI_VictorSPX(8) #Belt Drive

        self.joy = wpilib.Joystick(0)
        self.stick = wpilib.Joystick(1) #this is a controller, also acceptable to use Joystick

        self.intake = wpilib.DoubleSolenoid(0,1)
        self.balls = wpilib.DoubleSolenoid(2,3)

        self.left = wpilib.SpeedControllerGroup(self.motor1, self.motor2)
        self.right = wpilib.SpeedControllerGroup(self.motor3, self.motor4)

#This is combining the Speed controls from above to make a left and right
#for the drive chassis. Note that self.motor1 and self.motor2 are combined to make self.left
#then self.motor3 and self.motor4 are combined to make self.right. This is done to Make
#the differential drive easier to setup

        self.myRobot = wpilib.drive.DifferentialDrive(self.left, self.right)
#Here is our DifferentialDrive, Ultimately stating, Left side and Right side of chassis
#An Alternative to DifferentialDrive is this:
        #self.robodrive = wpilib.RobotDrive(self.motor1, self.motor4, self.motor3, self.motor2)
        #where motor 1 & 4 are left, and 2 & 3 are right
        self.myRobot.setExpiration(0.1)


#These components here are for Autonomous Modes, and allows you to call parts and
#components here to be used IN automodes. For example- Our chassis above is labeled
#'self.myRobot', below in the self.components, If we want to use our chassis to drive
#in Autonomous, we need to call it in the fashion below.  It is also encouraged to
#reuse the naming of the components from above to avoid confusion below. i.e.
#'Chassis': self.myRobot, In autonomous creation, I would then be using the variable
#self.chassis.set() instead of self.myRobot.set() when doing commands.

        self.components = {
            'myRobot': self.myRobot, #Chassis Driving
            'motor5': self.motor5, #A speed control that is used for intake
            'intake': self.intake #pneumatics arm that is not setup on bot yet
        }

        self.automodes = AutonomousModeSelector('autonomous', self.components)

#This line is to label where our automodes folder is and what devices used,
#('Insert folder name here', What compenents used in your auto codes (See above)


    def autonomousInit(self):

#This function is run once each time the robot enters autonomous mode.
        pass

    def autonomousPeriodic(self):

#This function is called periodically during autonomous.

        self.automodes.run()


    def teleopInit(self):

#Executed at the start of teleop mode

        self.myRobot.setSafetyEnabled(True)


    def teleopPeriodic(self):

#Runs Robot on Arcade Drive


        self.myRobot.tankDrive(-.5*self.stick.getRawAxis(1), self.stick.getRawAxis(5)*-.5)


#Below is an example code to be used for when a button is pressed
#to do something

#Intake Commands

        if self.joy.getRawButton(2): #Turn Intake motors on and intake Belt
                self.motor5.set(.25)
                self.motor6.set(.1)

        elif self.joy.getRawButton(7): #Relax....  take a rest and stop motors
                self.motor6.set(0)
                self.motor5.set(0)

#Motor shooting Speeds Below
        if self.stick.getRawButton(1): #Low Goal - Face On (Distance 0)
                self.motor5.set(.60)
                self.motor6.set(-.40)

        elif self.stick.getRawButton(2): #7.5-12.5 Ft Shot
                self.motor5.set(.85)
                self.motor6.set(-.15)

        elif self.stick.getRawButton(3): #12.5-17.5 ft Shot
                self.motor5.set(.60)
                self.motor6.set(-.40)

        elif self.stick.getRawButton(4): #17.5 - 22.5 ft Shot
                self.motor5.set(.7)
                self.motor6.set(-.7)

        elif self.stick.getRawButton(5): #Stop motors
                self.motor5.set(0)
                self.motor6.set(0)

#Arm out and Feed Balls

        if self.joy.getRawButton(4): #Arm Out
            self.intake.set(wpilib.DoubleSolenoid.Value.kForward)

        elif self.joy.getRawButton(5): #Arm in
            self.intake.set(wpilib.DoubleSolenoid.Value.kReverse)

        elif self.stick.getRawButton(6):
            self.balls.set(wpilib.DoubleSolenoid.Value.kReverse)

        elif self.stick.getRawButton(5):
            self.balls.set(wpilib.DoubleSolenoid.Value.kForward)




if __name__ == "__main__":
    wpilib.run(MyRobot)
