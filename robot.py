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
        #Drive Motors
        self.motor1 = ctre.WPI_TalonSRX(1)  # Initialize the TalonSRX on device 1.
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        self.motor5 = ctre.WPI_TalonFX(5)   #Shooter Motor

        self.motor6 = ctre.WPI_TalonFX(6)   #Intake Motor

        self.motor7 = ctre.WPI_VictorSPX(7) #Intake Arm

        self.motor8 = ctre.WPI_VictorSPX(8) #Belt Drive

        self.joy = wpilib.Joystick(0) #this is a controller, also acceptable to use Joystick
        #self.arm = wpilib.Solenoid(1) #calling a solenoid to be used with Pneumatics


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
            'myRobot': self.myRobot,
            'motor5': self.motor5, #again a speed control not setup yet
            #'arm': self.arm #pneumatics arm that is not setup on bot yet
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

#Runs Robot on Arcade Drive and pulls


        self.myRobot.arcadeDrive(-1*self.joy.getRawAxis(1), self.joy.getRawAxis(0))


#Below is an example code to be used for when a button is pressed
#do something

#Shooter Commands
        if self.joy.getRawButton(1): #Start Shooter Motors
            self.motor5.set(.70)
            self.motor6.set(-.40) #Value Between -1 and 1 for speeds

        else:
            if self.joy.getRawButton(2): #Turn Intake motors on and Belt
                self.motor5.set(.25)
                self.motor8.set(.5)
                self.motor6.set(-.2)

            else:
                if self.joy.getRawButton(3): #FIRE ZE LAZERZ!
                    self.motor5.set(.5)
                    self.motor6.set(-.4)
                    self.motor8.set(-.5)

                else: #Relax....  take a rest
                    self.motor6.set(0)
                    self.motor5.set(0)
                    self.motor8.set(0)
#Arm out
        if self.joy.getRawButton(4): #Move arm out
            self.motor7.set(1)

        else:
            if self.joy.getRawButton(5):#Move arm in
                self.motor7.set(-1)

            else: #Rest Arm
                self.motor7.set(0)

#Raise and Lower arm
        if self.joy.getRawButton(8):
            self.motor8.set(1)

        else:
            if self.joy.getRawButton(9):
                self.motor8.set(-1)

            else:
                self.motor8.set(0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
