def saveToFile(data,filename):
	with open(filename, 'a',encoding = "UTF-8") as file:
		file.write(data+'\n')
		file.close
	return data

def openFile(filename):
	with open(filename,"r",encoding = "UTF-8") as file:
		data = file.read()
		dataList = data.split("\n")
		return dataList