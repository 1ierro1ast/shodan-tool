import subprocess, sys

def install(module):
	subprocess.call(["pip","install",module])
	subprocess.call(["pip3","install",module])
	return "success"

def main():
	print(install("shodan"))

if __name__ == "__main__":
	sys.exit(main())
