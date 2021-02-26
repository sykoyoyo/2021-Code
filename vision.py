#!/usr/bin/env python3

import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.drive
import ctre
from robotpy_ext.autonomous import AutonomousModeSelector
from networktables import NetworkTables
import wpilib.drive.PIDController


#Import is pulling all the libraries and API's you need for your code,
#The most common ones are posted above that we will use for now.


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        #Limelight Pulling of information - NetworkTables
        table = NetworkTables.getTable("limelight")
        tx = table.getNumber('tx',None) #Horizontal Offset From Crosshair To Target
        ty = table.getNumber('ty',None) #Vertical Offset From Crosshair To Target
        ta = table.getNumber('ta',None) #Target Area (0% of image to 100% of image)
        ts = table.getNumber('ts',None) #Skew or rotation (-90 degrees to 0 degrees)
        tv = table.getNumber('tv',None) #Whether the limelight has any valid targets (0 or 1)


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

#Runs Robot on Arcade Drive


        self.myRobot.arcadeDrive(-1*self.joy.getRawAxis(1), self.joy.getRawAxis(0))

        print ta
        print tv
        print tx
        print ts
        print ty

#Below is an example code to be used for when a button is pressed
#to do something

#Shooter Commands
        if self.joy.getRawButton(1): #Start Shooter Motors
            self.motor5.set(.60)
            self.motor6.set(-.40) #Value Between -1 and 1 for speeds

        else:
            if self.joy.getRawButton(2): #Turn Intake motors on and intake Belt
                self.motor5.set(.25)
                self.motor6.set(.2)

            else:
                if self.joy.getRawButton(7): #Relax....  take a rest and stop motors
                    self.motor6.set(0)
                    self.motor5.set(0)
#Arm out
        self.intake.set(wpilib.DoubleSolenoid.Value.kReverse)

        if self.joy.getRawButton(4):
            self.intake.toggle()


#Vision Options
#Figure out how far away (distance)
#Figure out RPM
#WPI on how to pull those for Readout
#
    float KpDistance = -0.1f  #Proportional control constant for distance
    float current_distance = Estimate_Distance()  #see the 'Case Study: Estimating Distance'

    if self.joy.GetRawButton(6):

        float distance_error = desired_distance - current_distance
        driving_adjust = KpDistance * distance_error

        left_command += distance_adjust
        right_command += distance_adjust



if __name__ == "__main__":
    wpilib.run(MyRobot)
