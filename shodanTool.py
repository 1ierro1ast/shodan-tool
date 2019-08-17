import shodan,sys,subprocess
from file import openFile,saveToFile
from config import apiKey

class shTool:

	def __init__(self,apiKey):
		self.api = shodan.Shodan(apiKey)
		self.args = sys.argv
		self.request = self.args[2]
		self.reqSave = self.args[1]
		self.results = self.api.search(self.request)
		self.splitter = "\n------------------------------------------------------\n"
		self.totalResults = "Results found: " + str(self.results['total'])+self.splitter
		

	def resultsMatch(self):
		print(self.totalResults)
		for result in self.results['matches']:
			ip = "IP: "+result['ip_str']+"\n"
			data = result['data']
			if self.reqSave == "-s":
				saveToFile(ip+data+self.splitter,"resultData.txt")
			elif self.reqSave == "-ns":
				print(ip+data+self.splitter)
			elif self.reqSave == "-ip":
				saveToFile(result['ip_str'],"foundIp.txt")
			else:
				print(self.splitter + "Unknow argument: " + self.reqSave + self.splitter)
		print("Success!")

if __name__ == "__main__":
	subprocess.call("cls", shell = True)
	tool = shTool(apiKey)
	sys.exit(tool.resultsMatch())
