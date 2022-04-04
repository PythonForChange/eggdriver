from eggdriver.resources.server.ip import Device
import subprocess, sys, os, threading

class PythonThread (threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
    def run(self):
        os.chdir(self.root)
        subprocess.check_call([sys.executable, '-m', 'http.server', str(self.port)])

class NgrokThread (threading.Thread):
    def __init__(self, port, root):
        threading.Thread.__init__(self)
        self.root = root
        self.port = port
    def run(self):
        # Using ngrok https://ngrok.com/download
        os.chdir(self.root)
        os.system("ngrok http " + str(self.port))

class Server():
    def __init__(self, port = 7000):
        self.root = os.getcwd()
        self.port = port
    def localhost(self):
        os.chdir(self.root)
        device = Device()
        ip = device.ipAddress[0]
        print(f"Running on:\t{ip}:{self.port}")
        subprocess.check_call([sys.executable, '-m', 'http.server', str(self.port)])
    def ngrok(self, ngrokRoot = "C:\\"):
        pThread = PythonThread(self.port)
        nThread = NgrokThread(self.port, ngrokRoot)
        executeThreads([pThread, nThread])
        
def executeThreads(threads):
    [i.start() for i in threads]
    [i.join() for i in threads]