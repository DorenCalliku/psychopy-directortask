#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Dec 21 00:37:40 2021
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

# --------- UPDATE ------------
from utils import extract_experiment_steps, position_elements
structure = extract_experiment_steps('materials/experiment.xlsx')

elements_names = set(
    [
        str(j)
        for _, val in structure.items()
        for j in val['elements'] if j is not None
    ]
)
# ------- END UPDATE --------

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Directortask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'results/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='directortask.py',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_1 = visual.TextStim(win=win, name='text_1',
    text="Cette expérience étudie la capacité des gens à suivre des instructions sur l'ordinateur.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='<appuyez sur la barre d’espace pour continuer>',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Voici un exemple de ce que vous allez voir:',
    font='Open Sans',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='On va vous présentez une grille avec plusieurs objets situés dans les cases.\nUn \'directeur\', qui se trouve de l\'autre côté de la grille, qui vous donnera des instructions sur quel objets déplacer et dans quelle direction. \nComme vous pouvez le voir, il y a plusieurs cases recouvertes. Vous avez la possibilité de voir les objets qui se situent dans les cases, mais le directeur non."',
    font='Open Sans',
    pos=(0, -0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='materials/imgs/slideinstructor1.png', mask=None,
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_2 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='<appuyez sur la barre d’espace pour continuer>',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Voici le point de vue du directeur: ',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='materials/imgs/slideinstructor2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='<appuyez sur la barre d’espace pour continuer>',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()

image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='materials/imgs/igp1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

pictures = position_elements(win, structure['testtrials'] )
for i, name in enumerate(pictures):
    globals()[f"pic{i+1}"] = pictures[name]

mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
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

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [text_1, key_resp, text_4]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_1* updates
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        text_1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_1.started', text_1.tStartRefresh)
thisExp.addData('text_1.stopped', text_1.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instructions2Components = [text, text_2, image, key_resp_2, text_5]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instructions3Components = [text_3, image_2, key_resp_3, text_6]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(100.000000)
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
pieces = [ pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8]
picked = []
movingPiece = None

# keep track of which components have finished
trialComponents = [image_3, pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, mouse]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    
    # *pic1* updates
    if pic1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic1.frameNStart = frameN  # exact frame index
        pic1.tStart = t  # local t and not account for scr refresh
        pic1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic1, 'tStartRefresh')  # time at next scr refresh
        pic1.setAutoDraw(True)
    if pic1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic1.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic1.tStop = t  # not accounting for scr refresh
            pic1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic1, 'tStopRefresh')  # time at next scr refresh
            pic1.setAutoDraw(False)
    
    # *pic2* updates
    if pic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic2.frameNStart = frameN  # exact frame index
        pic2.tStart = t  # local t and not account for scr refresh
        pic2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic2, 'tStartRefresh')  # time at next scr refresh
        pic2.setAutoDraw(True)
    if pic2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic2.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic2.tStop = t  # not accounting for scr refresh
            pic2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic2, 'tStopRefresh')  # time at next scr refresh
            pic2.setAutoDraw(False)
    
    # *pic3* updates
    if pic3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic3.frameNStart = frameN  # exact frame index
        pic3.tStart = t  # local t and not account for scr refresh
        pic3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic3, 'tStartRefresh')  # time at next scr refresh
        pic3.setAutoDraw(True)
    if pic3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic3.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic3.tStop = t  # not accounting for scr refresh
            pic3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic3, 'tStopRefresh')  # time at next scr refresh
            pic3.setAutoDraw(False)
    
    # *pic4* updates
    if pic4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic4.frameNStart = frameN  # exact frame index
        pic4.tStart = t  # local t and not account for scr refresh
        pic4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic4, 'tStartRefresh')  # time at next scr refresh
        pic4.setAutoDraw(True)
    if pic4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic4.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic4.tStop = t  # not accounting for scr refresh
            pic4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic4, 'tStopRefresh')  # time at next scr refresh
            pic4.setAutoDraw(False)
    
    # *pic5* updates
    if pic5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic5.frameNStart = frameN  # exact frame index
        pic5.tStart = t  # local t and not account for scr refresh
        pic5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic5, 'tStartRefresh')  # time at next scr refresh
        pic5.setAutoDraw(True)
    if pic5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic5.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic5.tStop = t  # not accounting for scr refresh
            pic5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic5, 'tStopRefresh')  # time at next scr refresh
            pic5.setAutoDraw(False)
    
    # *pic6* updates
    if pic6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic6.frameNStart = frameN  # exact frame index
        pic6.tStart = t  # local t and not account for scr refresh
        pic6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic6, 'tStartRefresh')  # time at next scr refresh
        pic6.setAutoDraw(True)
    if pic6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic6.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic6.tStop = t  # not accounting for scr refresh
            pic6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic6, 'tStopRefresh')  # time at next scr refresh
            pic6.setAutoDraw(False)
    
    # *pic7* updates
    if pic7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic7.frameNStart = frameN  # exact frame index
        pic7.tStart = t  # local t and not account for scr refresh
        pic7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic7, 'tStartRefresh')  # time at next scr refresh
        pic7.setAutoDraw(True)
    if pic7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic7.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic7.tStop = t  # not accounting for scr refresh
            pic7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic7, 'tStopRefresh')  # time at next scr refresh
            pic7.setAutoDraw(False)
    
    # *pic8* updates
    if pic8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pic8.frameNStart = frameN  # exact frame index
        pic8.tStart = t  # local t and not account for scr refresh
        pic8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic8, 'tStartRefresh')  # time at next scr refresh
        pic8.setAutoDraw(True)
    if pic8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pic8.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            pic8.tStop = t  # not accounting for scr refresh
            pic8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pic8, 'tStopRefresh')  # time at next scr refresh
            pic8.setAutoDraw(False)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
thisExp.addData('pic1.started', pic1.tStartRefresh)
thisExp.addData('pic1.stopped', pic1.tStopRefresh)
thisExp.addData('pic2.started', pic2.tStartRefresh)
thisExp.addData('pic2.stopped', pic2.tStopRefresh)
thisExp.addData('pic3.started', pic3.tStartRefresh)
thisExp.addData('pic3.stopped', pic3.tStopRefresh)
thisExp.addData('pic4.started', pic4.tStartRefresh)
thisExp.addData('pic4.stopped', pic4.tStopRefresh)
thisExp.addData('pic5.started', pic5.tStartRefresh)
thisExp.addData('pic5.stopped', pic5.tStopRefresh)
thisExp.addData('pic6.started', pic6.tStartRefresh)
thisExp.addData('pic6.stopped', pic6.tStopRefresh)
thisExp.addData('pic7.started', pic7.tStartRefresh)
thisExp.addData('pic7.stopped', pic7.tStopRefresh)
thisExp.addData('pic8.started', pic8.tStartRefresh)
thisExp.addData('pic8.stopped', pic8.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()

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
