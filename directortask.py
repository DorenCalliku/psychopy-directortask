#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Jan 24 19:03:42 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import pprint

xaxis = ['A','B','C','D']
yaxis = ['1','2','3','4']
def xy_to_AD14(x_pos, y_pos):
    return xaxis[x_pos] + yaxis[y_pos]  # A1

def from_position_to_picture_x(pos_x):
    return -0.28 + 0.14 * pos_x

def from_position_to_picture_y(pos_y):
    return 0.14 + (-0.14) * pos_y + 0.01


def from_picture_to_position_x(pic_x):
    return round((pic_x + 0.28)/0.14)

def from_picture_to_position_y(pic_y):
    return round((pic_y - 0.14 - 0.01)/(-0.14))

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'directortask_ALF_bis'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/delta/Desktop/meta/directortask/directortask.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "directortask"
directortaskClock = core.Clock()
background = visual.ImageStim(
    win=win,
    name='background', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
A1 = visual.ImageStim(
    win=win,
    name='A1', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
A2 = visual.ImageStim(
    win=win,
    name='A2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
A3 = visual.ImageStim(
    win=win,
    name='A3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
A4 = visual.ImageStim(
    win=win,
    name='A4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
B1 = visual.ImageStim(
    win=win,
    name='B1', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
B2 = visual.ImageStim(
    win=win,
    name='B2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
B3 = visual.ImageStim(
    win=win,
    name='B3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
B4 = visual.ImageStim(
    win=win,
    name='B4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
C1 = visual.ImageStim(
    win=win,
    name='C1', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
C2 = visual.ImageStim(
    win=win,
    name='C2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
C3 = visual.ImageStim(
    win=win,
    name='C3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
C4 = visual.ImageStim(
    win=win,
    name='C4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
D1 = visual.ImageStim(
    win=win,
    name='D1', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
D2 = visual.ImageStim(
    win=win,
    name='D2', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
D3 = visual.ImageStim(
    win=win,
    name='D3', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
D4 = visual.ImageStim(
    win=win,
    name='D4', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
soundfile = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='soundfile')
soundfile.setVolume(1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# USE THIS
picked = []
movingPiece = None
movements = []
current_movement = None
mouse_clicked_important = False
def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                return piece

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# set up handler to look after randomisation of conditions etc
directortask_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('materials/conditionfile_test.xlsx'),
    seed=None, name='directortask_loop')
thisExp.addLoop(directortask_loop)  # add the loop to the experiment
thisDirectortask_loop = directortask_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDirectortask_loop.rgb)
if thisDirectortask_loop != None:
    for paramName in thisDirectortask_loop:
        exec('{} = thisDirectortask_loop[paramName]'.format(paramName))

for thisDirectortask_loop in directortask_loop:
    currentLoop = directortask_loop
    # abbreviate parameter names if possible (e.g. rgb = thisDirectortask_loop.rgb)
    if thisDirectortask_loop != None:
        for paramName in thisDirectortask_loop:
            exec('{} = thisDirectortask_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "directortask"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    background.setImage(Background)
    A1.setPos((-0.28, 0.14))
    A1.setImage(box_A1)
    A2.setPos((-0.28, 0))
    A2.setImage(box_A2)
    A3.setPos((-0.28, -0.14))
    A3.setImage(box_A3)
    A4.setPos((-0.28, -0.28))
    A4.setImage(box_A4)
    B1.setPos((-0.14, 0.14))
    B1.setImage(box_B1)
    B2.setPos((-0.14, 0))
    B2.setImage(box_B2)
    B3.setPos((-0.14, -0.14))
    B3.setImage(box_B3)
    B4.setPos((-0.14, -0.28))
    B4.setImage(box_B4)
    C1.setPos((0, 0.14))
    C1.setImage(box_C1)
    C2.setPos((0, 0))
    C2.setImage(box_C2)
    C3.setPos((0, -0.14))
    C3.setImage(box_C3)
    C4.setPos((0, -0.28))
    C4.setImage(box_C4)
    D1.setPos((0.14, 0.14))
    D1.setImage(box_D1)
    D2.setPos((0.14, 0))
    D2.setImage(box_D2)
    D3.setPos((0.14, -0.14))
    D3.setImage(box_D3)
    D4.setPos((0.14, -0.28))
    D4.setImage(box_D4)

    soundfile.setSound(Sound, secs=10.0, hamming=True)
    soundfile.setVolume(1.0, log=False)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []

    gotValidClick = False  # until a click is received
    pieces = [ A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4]
    picked = []
    movingPiece = None
    
    # keep track of which components have finished
    directortaskComponents = [background, A1, A2, A3, A4, B1, B2, B3, B4, C1, C2, C3, C4, D1, D2, D3, D4, soundfile, mouse]
    for thisComponent in directortaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    directortaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    # -------Run Routine "directortask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = directortaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=directortaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background* updates
        if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background.frameNStart = frameN  # exact frame index
            background.tStart = t  # local t and not account for scr refresh
            background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
            background.setAutoDraw(True)
        if background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                background.tStop = t  # not accounting for scr refresh
                background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background, 'tStopRefresh')  # time at next scr refresh
                background.setAutoDraw(False)
        
        # *A1* updates
        if A1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A1.frameNStart = frameN  # exact frame index
            A1.tStart = t  # local t and not account for scr refresh
            A1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A1, 'tStartRefresh')  # time at next scr refresh
            A1.setAutoDraw(True)
        if A1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                A1.tStop = t  # not accounting for scr refresh
                A1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(A1, 'tStopRefresh')  # time at next scr refresh
                A1.setAutoDraw(False)
        
        # *A2* updates
        if A2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A2.frameNStart = frameN  # exact frame index
            A2.tStart = t  # local t and not account for scr refresh
            A2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A2, 'tStartRefresh')  # time at next scr refresh
            A2.setAutoDraw(True)
        if A2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                A2.tStop = t  # not accounting for scr refresh
                A2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(A2, 'tStopRefresh')  # time at next scr refresh
                A2.setAutoDraw(False)
        
        # *A3* updates
        if A3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A3.frameNStart = frameN  # exact frame index
            A3.tStart = t  # local t and not account for scr refresh
            A3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A3, 'tStartRefresh')  # time at next scr refresh
            A3.setAutoDraw(True)
        if A3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A3.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                A3.tStop = t  # not accounting for scr refresh
                A3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(A3, 'tStopRefresh')  # time at next scr refresh
                A3.setAutoDraw(False)
        
        # *A4* updates
        if A4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A4.frameNStart = frameN  # exact frame index
            A4.tStart = t  # local t and not account for scr refresh
            A4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A4, 'tStartRefresh')  # time at next scr refresh
            A4.setAutoDraw(True)
        if A4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > A4.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                A4.tStop = t  # not accounting for scr refresh
                A4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(A4, 'tStopRefresh')  # time at next scr refresh
                A4.setAutoDraw(False)
        
        # *B1* updates
        if B1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B1.frameNStart = frameN  # exact frame index
            B1.tStart = t  # local t and not account for scr refresh
            B1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B1, 'tStartRefresh')  # time at next scr refresh
            B1.setAutoDraw(True)
        if B1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                B1.tStop = t  # not accounting for scr refresh
                B1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B1, 'tStopRefresh')  # time at next scr refresh
                B1.setAutoDraw(False)
        
        # *B2* updates
        if B2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B2.frameNStart = frameN  # exact frame index
            B2.tStart = t  # local t and not account for scr refresh
            B2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B2, 'tStartRefresh')  # time at next scr refresh
            B2.setAutoDraw(True)
        if B2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                B2.tStop = t  # not accounting for scr refresh
                B2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B2, 'tStopRefresh')  # time at next scr refresh
                B2.setAutoDraw(False)
        
        # *B3* updates
        if B3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B3.frameNStart = frameN  # exact frame index
            B3.tStart = t  # local t and not account for scr refresh
            B3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B3, 'tStartRefresh')  # time at next scr refresh
            B3.setAutoDraw(True)
        if B3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B3.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                B3.tStop = t  # not accounting for scr refresh
                B3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B3, 'tStopRefresh')  # time at next scr refresh
                B3.setAutoDraw(False)
        
        # *B4* updates
        if B4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B4.frameNStart = frameN  # exact frame index
            B4.tStart = t  # local t and not account for scr refresh
            B4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B4, 'tStartRefresh')  # time at next scr refresh
            B4.setAutoDraw(True)
        if B4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B4.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                B4.tStop = t  # not accounting for scr refresh
                B4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B4, 'tStopRefresh')  # time at next scr refresh
                B4.setAutoDraw(False)
        
        # *C1* updates
        if C1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C1.frameNStart = frameN  # exact frame index
            C1.tStart = t  # local t and not account for scr refresh
            C1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C1, 'tStartRefresh')  # time at next scr refresh
            C1.setAutoDraw(True)
        if C1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                C1.tStop = t  # not accounting for scr refresh
                C1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C1, 'tStopRefresh')  # time at next scr refresh
                C1.setAutoDraw(False)
        
        # *C2* updates
        if C2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C2.frameNStart = frameN  # exact frame index
            C2.tStart = t  # local t and not account for scr refresh
            C2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C2, 'tStartRefresh')  # time at next scr refresh
            C2.setAutoDraw(True)
        if C2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                C2.tStop = t  # not accounting for scr refresh
                C2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C2, 'tStopRefresh')  # time at next scr refresh
                C2.setAutoDraw(False)
        
        # *C3* updates
        if C3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C3.frameNStart = frameN  # exact frame index
            C3.tStart = t  # local t and not account for scr refresh
            C3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C3, 'tStartRefresh')  # time at next scr refresh
            C3.setAutoDraw(True)
        if C3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C3.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                C3.tStop = t  # not accounting for scr refresh
                C3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C3, 'tStopRefresh')  # time at next scr refresh
                C3.setAutoDraw(False)
        
        # *C4* updates
        if C4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C4.frameNStart = frameN  # exact frame index
            C4.tStart = t  # local t and not account for scr refresh
            C4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C4, 'tStartRefresh')  # time at next scr refresh
            C4.setAutoDraw(True)
        if C4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C4.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                C4.tStop = t  # not accounting for scr refresh
                C4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C4, 'tStopRefresh')  # time at next scr refresh
                C4.setAutoDraw(False)
        
        # *D1* updates
        if D1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D1.frameNStart = frameN  # exact frame index
            D1.tStart = t  # local t and not account for scr refresh
            D1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D1, 'tStartRefresh')  # time at next scr refresh
            D1.setAutoDraw(True)
        if D1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > D1.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                D1.tStop = t  # not accounting for scr refresh
                D1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(D1, 'tStopRefresh')  # time at next scr refresh
                D1.setAutoDraw(False)
        
        # *D2* updates
        if D2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D2.frameNStart = frameN  # exact frame index
            D2.tStart = t  # local t and not account for scr refresh
            D2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D2, 'tStartRefresh')  # time at next scr refresh
            D2.setAutoDraw(True)
        if D2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > D2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                D2.tStop = t  # not accounting for scr refresh
                D2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(D2, 'tStopRefresh')  # time at next scr refresh
                D2.setAutoDraw(False)
        
        # *D3* updates
        if D3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D3.frameNStart = frameN  # exact frame index
            D3.tStart = t  # local t and not account for scr refresh
            D3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D3, 'tStartRefresh')  # time at next scr refresh
            D3.setAutoDraw(True)
        if D3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > D3.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                D3.tStop = t  # not accounting for scr refresh
                D3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(D3, 'tStopRefresh')  # time at next scr refresh
                D3.setAutoDraw(False)
        
        # *D4* updates
        if D4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D4.frameNStart = frameN  # exact frame index
            D4.tStart = t  # local t and not account for scr refresh
            D4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D4, 'tStartRefresh')  # time at next scr refresh
            D4.setAutoDraw(True)
        if D4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > D4.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                D4.tStop = t  # not accounting for scr refresh
                D4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(D4, 'tStopRefresh')  # time at next scr refresh
                D4.setAutoDraw(False)
        # start/stop soundfile
        if soundfile.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            soundfile.frameNStart = frameN  # exact frame index
            soundfile.tStart = t  # local t and not account for scr refresh
            soundfile.tStartRefresh = tThisFlipGlobal  # on global time
            soundfile.play(when=win)  # sync with win flip
        if soundfile.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > soundfile.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                soundfile.tStop = t  # not accounting for scr refresh
                soundfile.frameNStop = frameN  # exact frame index
                win.timeOnFlip(soundfile, 'tStopRefresh')  # time at next scr refresh
                soundfile.stop()
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())


        # ADD THIS -----------------------------------
        # function below stores the information of the picked element 
        for piece in pieces:
            if mouse.isPressedIn(piece) and movingPiece is None:
                mouse_clicked_important = True

                x, y = mouse.getPos()
                picked.append(piece)
                current_movement = {
                    "start": (x, y),
                    "start_pos": (from_picture_to_position_x(x), from_picture_to_position_y(y)),
                    "start_AD": xy_to_AD14(from_picture_to_position_x(x), from_picture_to_position_y(y)),
                    "piece": piece.name,
                }

        # function below checks if the mouse was released, this way we store the information and go to next round
        if not any(mouse.isPressedIn(piece) for piece in pieces) and mouse_clicked_important == True and movingPiece is not None:

            # where am I as a mouse - existential question
            x, y = mouse.getPos()
            current_pos = (from_picture_to_position_x(x), from_picture_to_position_y(y))
        
            # if the position changed, update my data, go to next
            if current_pos != current_movement['start_pos']:

                # current movement measurements
                current_movement['end'] = (x, y)
                current_movement['end_pos'] = current_pos
                current_movement["end_AD"] = xy_to_AD14(from_picture_to_position_x(x), from_picture_to_position_y(y)),
                movements.append(current_movement)
            
                # store info
                directortask_loop.addData('piece.moved', movingPiece.image)
                directortask_loop.addData('piece.moved.start', current_movement['start_AD'])
                directortask_loop.addData('piece.moved.end', current_movement['end_AD'])

                # update code
                mouse_clicked_important = False
                current_movement = None

                # get out of loop, go to next
                break
    
        movingPiece = movePicked(picked, mouse, movingPiece)
        # UNTIL HERE ----------------------------

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in directortaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "directortask"-------
    for thisComponent in directortaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    directortask_loop.addData('background.started', background.tStartRefresh)
    directortask_loop.addData('background.stopped', background.tStopRefresh)
    directortask_loop.addData('A1.started', A1.tStartRefresh)
    directortask_loop.addData('A1.stopped', A1.tStopRefresh)
    directortask_loop.addData('A2.started', A2.tStartRefresh)
    directortask_loop.addData('A2.stopped', A2.tStopRefresh)
    directortask_loop.addData('A3.started', A3.tStartRefresh)
    directortask_loop.addData('A3.stopped', A3.tStopRefresh)
    directortask_loop.addData('A4.started', A4.tStartRefresh)
    directortask_loop.addData('A4.stopped', A4.tStopRefresh)
    directortask_loop.addData('B1.started', B1.tStartRefresh)
    directortask_loop.addData('B1.stopped', B1.tStopRefresh)
    directortask_loop.addData('B2.started', B2.tStartRefresh)
    directortask_loop.addData('B2.stopped', B2.tStopRefresh)
    directortask_loop.addData('B3.started', B3.tStartRefresh)
    directortask_loop.addData('B3.stopped', B3.tStopRefresh)
    directortask_loop.addData('B4.started', B4.tStartRefresh)
    directortask_loop.addData('B4.stopped', B4.tStopRefresh)
    directortask_loop.addData('C1.started', C1.tStartRefresh)
    directortask_loop.addData('C1.stopped', C1.tStopRefresh)
    directortask_loop.addData('C2.started', C2.tStartRefresh)
    directortask_loop.addData('C2.stopped', C2.tStopRefresh)
    directortask_loop.addData('C3.started', C3.tStartRefresh)
    directortask_loop.addData('C3.stopped', C3.tStopRefresh)
    directortask_loop.addData('C4.started', C4.tStartRefresh)
    directortask_loop.addData('C4.stopped', C4.tStopRefresh)
    directortask_loop.addData('D1.started', D1.tStartRefresh)
    directortask_loop.addData('D1.stopped', D1.tStopRefresh)
    directortask_loop.addData('D2.started', D2.tStartRefresh)
    directortask_loop.addData('D2.stopped', D2.tStopRefresh)
    directortask_loop.addData('D3.started', D3.tStartRefresh)
    directortask_loop.addData('D3.stopped', D3.tStopRefresh)
    directortask_loop.addData('D4.started', D4.tStartRefresh)
    directortask_loop.addData('D4.stopped', D4.tStopRefresh)
    soundfile.stop()  # ensure sound has stopped at end of routine
    directortask_loop.addData('soundfile.started', soundfile.tStartRefresh)
    directortask_loop.addData('soundfile.stopped', soundfile.tStopRefresh)
    # store data for directortask_loop (TrialHandler)
    directortask_loop.addData('mouse.x', mouse.x)
    directortask_loop.addData('mouse.y', mouse.y)
    directortask_loop.addData('mouse.leftButton', mouse.leftButton)
    directortask_loop.addData('mouse.midButton', mouse.midButton)
    directortask_loop.addData('mouse.rightButton', mouse.rightButton)
    directortask_loop.addData('mouse.time', mouse.time)
    directortask_loop.addData('mouse.started', mouse.tStart)
    directortask_loop.addData('mouse.stopped', mouse.tStop)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'directortask_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
