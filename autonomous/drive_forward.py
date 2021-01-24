#!/usr/bin/env python3

from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):
    #Required first two lines of Text!


    MODE_NAME = 'Drive Forward Long' - #This is the name the Auto is called
    DEFAULT = True  #only ONE Auto can have this- Makes it the default if none are chosen.  If you have more than one Auto with it on there, it will not work

    def initialize(self):
        #you could add timers here or additional sensors etc
        pass


    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    #@timed_state is required( Duration is length in seconds of first move,
    #next_state - says which line to go to AFTER completing this one,
    #first=True - Start here for automodes)

    def drive_wait(self):
        #def required - but then you use a Name for this move.
        #In this instance pick something that would match it's objective for
        #this one it is waiting, so "Drive wait"

        self.myRobot.tankDrive(0,0)
        #What does the robot do, Now you call your variables from robot.py
        #that were setup for Auto, and call them here.
        #Tank Drive (left, right)


    @timed_state(duration=4, next_state='stop')
    def drive_forward(self):
        self.myRobot.tankDrive(-1,-1)

        #This is a complete autonomous command, Note the Duration 4 seconds,
        #Next command is stop, Naming is Drive forward, and tank drive 1,1


    @state()
    def stop(self):
        self.myRobot.tankDrive(0,0)

        #This is the last statement given, and is a Stop command.
