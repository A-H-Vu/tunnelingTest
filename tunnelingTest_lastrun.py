#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 14, 2020, at 16:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'tunnelingTest'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\tunnelingTest\\tunnelingTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialCursor = visual.Polygon(
    win=win, name='trialCursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
trialPolygon = visual.Polygon(
    win=win, name='trialPolygon',
    edges=6, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.2, depth=-4.0, interpolate=True)
trialStart = visual.Rect(
    win=win, name='trialStart',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=0.2, depth=-5.0, interpolate=True)
trialEnd = visual.Rect(
    win=win, name='trialEnd',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,1.000], fillColorSpace='rgb',
    opacity=0.2, depth=-6.0, interpolate=True)
trialText = visual.TextStim(win=win, name='trialText',
    text=None,
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
trialPolygon.vertices = [(-0.4, -0.4), (-0.4, 0.0), (-0.2, 0.4), (0.4, 0.4), (0.2, 0.0), (0.2, -0.4)]
trialStart.vertices = [(-0.4, -0.4), (0.2, -0.4), (0.2, - 0.5), (-0.4, -0.5)]
trialEnd.vertices = [(0.4, 0.4), (-0.2, 0.4), (-0.2, 0.5), (0.4, 0.5)]

trialStep = 0
steps = []
# setup some python lists for storing info about the trialMouse
trialMouse.x = []
trialMouse.y = []
trialMouse.leftButton = []
trialMouse.midButton = []
trialMouse.rightButton = []
trialMouse.time = []
gotValidClick = False  # until a click is received
trialMouse.mouseClock.reset()
# keep track of which components have finished
trialComponents = [trialMouse, trialCursor, trialPolygon, trialStart, trialEnd, trialText]
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
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if trialPolygon.contains(trialMouse):
        trialText.text = "in"
    elif trialStart.contains(trialMouse):
        trialText.text = "in"
        trialStep = 1
    elif trialEnd.contains(trialMouse) and trialStep == 1:
        trialText.text = "in"
        trialStep = 2
        continueRoutine = False 
    else:
        trialText.text = "out"
    # *trialMouse* updates
    if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialMouse.frameNStart = frameN  # exact frame index
        trialMouse.tStart = t  # local t and not account for scr refresh
        trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
        trialMouse.status = STARTED
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if trialMouse.status == STARTED:  # only update if started and not finished!
        x, y = trialMouse.getPos()
        trialMouse.x.append(x)
        trialMouse.y.append(y)
        buttons = trialMouse.getPressed()
        trialMouse.leftButton.append(buttons[0])
        trialMouse.midButton.append(buttons[1])
        trialMouse.rightButton.append(buttons[2])
        trialMouse.time.append(trialMouse.mouseClock.getTime())
    
    # *trialCursor* updates
    if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialCursor.frameNStart = frameN  # exact frame index
        trialCursor.tStart = t  # local t and not account for scr refresh
        trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
        trialCursor.setAutoDraw(True)
    if trialCursor.status == STARTED:  # only update if drawing
        trialCursor.setPos((trialMouse.getPos()[0], trialMouse.getPos()[1]), log=False)
    
    # *trialPolygon* updates
    if trialPolygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialPolygon.frameNStart = frameN  # exact frame index
        trialPolygon.tStart = t  # local t and not account for scr refresh
        trialPolygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialPolygon, 'tStartRefresh')  # time at next scr refresh
        trialPolygon.setAutoDraw(True)
    
    # *trialStart* updates
    if trialStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialStart.frameNStart = frameN  # exact frame index
        trialStart.tStart = t  # local t and not account for scr refresh
        trialStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialStart, 'tStartRefresh')  # time at next scr refresh
        trialStart.setAutoDraw(True)
    
    # *trialEnd* updates
    if trialEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialEnd.frameNStart = frameN  # exact frame index
        trialEnd.tStart = t  # local t and not account for scr refresh
        trialEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialEnd, 'tStartRefresh')  # time at next scr refresh
        trialEnd.setAutoDraw(True)
    
    # *trialText* updates
    if trialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialText.frameNStart = frameN  # exact frame index
        trialText.tStart = t  # local t and not account for scr refresh
        trialText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialText, 'tStartRefresh')  # time at next scr refresh
        trialText.setAutoDraw(True)
    
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
thisExp.addData('step', steps)
# store data for thisExp (ExperimentHandler)
thisExp.addData('trialMouse.x', trialMouse.x)
thisExp.addData('trialMouse.y', trialMouse.y)
thisExp.addData('trialMouse.leftButton', trialMouse.leftButton)
thisExp.addData('trialMouse.midButton', trialMouse.midButton)
thisExp.addData('trialMouse.rightButton', trialMouse.rightButton)
thisExp.addData('trialMouse.time', trialMouse.time)
thisExp.addData('trialMouse.started', trialMouse.tStartRefresh)
thisExp.addData('trialMouse.stopped', trialMouse.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('trialCursor.started', trialCursor.tStartRefresh)
thisExp.addData('trialCursor.stopped', trialCursor.tStopRefresh)
thisExp.addData('trialPolygon.started', trialPolygon.tStartRefresh)
thisExp.addData('trialPolygon.stopped', trialPolygon.tStopRefresh)
thisExp.addData('trialStart.started', trialStart.tStartRefresh)
thisExp.addData('trialStart.stopped', trialStart.tStopRefresh)
thisExp.addData('trialEnd.started', trialEnd.tStartRefresh)
thisExp.addData('trialEnd.stopped', trialEnd.tStopRefresh)
thisExp.addData('trialText.started', trialText.tStartRefresh)
thisExp.addData('trialText.stopped', trialText.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
