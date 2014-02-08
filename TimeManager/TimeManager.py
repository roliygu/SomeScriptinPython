import time

def CTimetoMytime(s):
	return (int(s[8:10]), int(s[11:13]), int(s[14:16]))

def MytimeMinus(a, b):
	return (a[0]-b[0])*24*60+(a[1]-b[1])*60+(a[2]-b[2])
class Task:
	def __init__(self):
		L = getCurrentTask()
		self.name = L[0]
		self.kind = int(L[1])
		self.startTime = (int(L[2]), int(L[3]), int(L[4]))
	def overTask(self):
		self.endTime = CTimetoMytime(time.ctime())
		self.allTime = MytimeMinus(self.endTime, self.startTime)
	def output(self):
		file=open('.//file//AllTask','a')
		string = self.name+' '+str(self.kind)+' '+str(self.startTime)+' '+str(self.endTime)+' '+str(self.allTime)
		file.write(string)
		file.write('\n')
		file.close()

def newTask():
	name = raw_input("input name: ")
	kind = raw_input("input kind: ")
	startTime = CTimetoMytime(time.ctime())
	file=open('.//file//CurrentTask','w')
	string = name+' '+kind+' '+str(startTime[0])+' '+str(startTime[1])+' '+str(startTime[2])
	file.write(string)
	file.close()


def getCurrentTask():
	file=open('.//file//CurrentTask')
	stringCurren = file.read()
	file.close()
	return stringCurren.split(' ')

def timeStatistics():
	file=open('.//file//AllTask')
	lineString = file.readlines()
	StudyTime=0
	NoStudyTime=0
	for i in lineString:
		i=i[:-1]
		L=i.split(' ')
		if int(L[1])==0:
			NoStudyTime+=int(L[-1])
		elif int(L[1])==1:
			StudyTime+=int(L[-1])
	file.close()
	file=open('.//file//AllTask','a')
	Percen = str(StudyTime*1.0/((StudyTime+NoStudyTime)*1.0)*100)
	Percen = Percen[:4]
	file.write('the Percentage of the StudyTime in all the time is '+
		Percen+'%.')
	StudyHour = str(StudyTime*1.0/60)
	StudyHour = StudyHour[:4]+'h'
	file.write('total StudyTime is '+StudyHour)
	file.close()