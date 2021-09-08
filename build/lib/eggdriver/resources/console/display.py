import time, os, sys, subprocess

def sleep(i: int = 100):
    	time.sleep(i/1000)

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls    
		command = 'cls'
	os.system(command)

def display(T, delta: int = 400, condition: bool = True):
	while condition:
		print(T)
		sleep(delta)
		clearConsole()

def sysCommand(command: str):
	commands = command.split()
	commands.reverse()
	# commands.append(sys.executable) Not works yet, instead:
	commands.append("py") # Just on Windows
	commands.reverse()
	subprocess.check_call(commands)