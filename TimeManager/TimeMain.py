import sys,os
sys.path+=[os.getcwd()]
from TimeManager import *

def commonTask():
	cTack = Task()
	cTack.overTask()
	cTack.output()
	newTask()

commonTask()
#timeStatistics()