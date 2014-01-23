import zipfile,sys,os
List = os.listdir(os.getcwd())

def makezip(L,filename):
	f = zipfile.ZipFile(filename, 'w' ,zipfile.ZIP_DEFLATED) 
	for i in L:
		f.write(i)
	f.close() 

def makeList(List):
	LList={}
	for i in List:
		key_i = i[:2]
		if key_i in LList:
			LList[key_i].append(i)
		else:
			LList[key_i]=[i]
	return LList

def ziptt(dic):
	key_List = dic.keys()
	for i in key_List:
		makezip(dic[i],i+'.zip')
