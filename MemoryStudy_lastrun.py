#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on June 16, 2022, at 16:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'MemoryStudy'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
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
    originPath='C:\\Users\\Psychology\\Documents\\ABExperiment\\MemoryStudy\\MemoryStudy_lastrun.py',
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
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Mem_Instructions"
Mem_InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Memory test instructions',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
End_Instructions = keyboard.Keyboard()

# Initialize components for Routine "MemoryTest"
MemoryTestClock = core.Clock()
# Set experiment start values for variable component Mem_curImage
Mem_curImage = ''
Mem_curImageContainer = []
trialClock = core.Clock()

MemTest = visual.TextStim(win=win, name='MemTest',
    text='Did you see this image?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
MemResponse = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Mem_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
End_Instructions.keys = []
End_Instructions.rt = []
_End_Instructions_allKeys = []
# keep track of which components have finished
Mem_InstructionsComponents = [text, End_Instructions]
for thisComponent in Mem_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Mem_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Mem_Instructions"-------
while continueRoutine:
    # get current time
    t = Mem_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Mem_InstructionsClock)
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
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10000-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *End_Instructions* updates
    waitOnFlip = False
    if End_Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_Instructions.frameNStart = frameN  # exact frame index
        End_Instructions.tStart = t  # local t and not account for scr refresh
        End_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_Instructions, 'tStartRefresh')  # time at next scr refresh
        End_Instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End_Instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End_Instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End_Instructions.status == STARTED and not waitOnFlip:
        theseKeys = End_Instructions.getKeys(keyList=['space'], waitRelease=False)
        _End_Instructions_allKeys.extend(theseKeys)
        if len(_End_Instructions_allKeys):
            End_Instructions.keys = _End_Instructions_allKeys[-1].name  # just the last key pressed
            End_Instructions.rt = _End_Instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Mem_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Mem_Instructions"-------
for thisComponent in Mem_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if End_Instructions.keys in ['', [], None]:  # No response was made
    End_Instructions.keys = None
thisExp.addData('End_Instructions.keys',End_Instructions.keys)
if End_Instructions.keys != None:  # we had a response
    thisExp.addData('End_Instructions.rt', End_Instructions.rt)
thisExp.addData('End_Instructions.started', End_Instructions.tStartRefresh)
thisExp.addData('End_Instructions.stopped', End_Instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "Mem_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Memory_conditionSheet.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "MemoryTest"-------
    continueRoutine = True
    # update component parameters for each repeat
    t = 0
    trialClock.reset()
    imageCount = 0
    MemResponse.keys = []
    MemResponse.rt = []
    _MemResponse_allKeys = []
    image.setImage(Mem_curImage)
    # keep track of which components have finished
    MemoryTestComponents = [MemTest, MemResponse, image]
    for thisComponent in MemoryTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MemoryTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MemoryTest"-------
    while continueRoutine:
        # get current time
        t = MemoryTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MemoryTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t = trialClock.getTime()
        
        Mem_curImage = "resources\\JPG" + Picture
        imageCount = imageCount + 1
        Mem_curImage = Mem_curImage + ".jpg"
        
        #C:\Users\Psychology\Documents\ABExperiment\MemoryStudy\resources\JPG
        
        # *MemTest* updates
        if MemTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MemTest.frameNStart = frameN  # exact frame index
            MemTest.tStart = t  # local t and not account for scr refresh
            MemTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MemTest, 'tStartRefresh')  # time at next scr refresh
            MemTest.setAutoDraw(True)
        if MemTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MemTest.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                MemTest.tStop = t  # not accounting for scr refresh
                MemTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(MemTest, 'tStopRefresh')  # time at next scr refresh
                MemTest.setAutoDraw(False)
        
        # *MemResponse* updates
        waitOnFlip = False
        if MemResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MemResponse.frameNStart = frameN  # exact frame index
            MemResponse.tStart = t  # local t and not account for scr refresh
            MemResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MemResponse, 'tStartRefresh')  # time at next scr refresh
            MemResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MemResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MemResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MemResponse.status == STARTED and not waitOnFlip:
            theseKeys = MemResponse.getKeys(keyList=['1''2''3''4''5''6''7'], waitRelease=False)
            _MemResponse_allKeys.extend(theseKeys)
            if len(_MemResponse_allKeys):
                MemResponse.keys = _MemResponse_allKeys[-1].name  # just the last key pressed
                MemResponse.rt = _MemResponse_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 10000-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MemoryTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MemoryTest"-------
    for thisComponent in MemoryTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('MemTest.started', MemTest.tStartRefresh)
    trials.addData('MemTest.stopped', MemTest.tStopRefresh)
    # check responses
    if MemResponse.keys in ['', [], None]:  # No response was made
        MemResponse.keys = None
    trials.addData('MemResponse.keys',MemResponse.keys)
    if MemResponse.keys != None:  # we had a response
        trials.addData('MemResponse.rt', MemResponse.rt)
    trials.addData('MemResponse.started', MemResponse.tStartRefresh)
    trials.addData('MemResponse.stopped', MemResponse.tStopRefresh)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # the Routine "MemoryTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
