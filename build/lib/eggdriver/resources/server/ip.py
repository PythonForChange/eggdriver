import socket, urllib.request

class Device():
    @property
    def hostname(self):
        return socket.gethostname()
    @property
    def ipAddress(self):
        privateIp = socket.gethostbyname(self.hostname)
        publicIp = urllib.request.urlopen("https://ident.me").read().decode("utf8")
        return [privateIp, publicIp]
    def getPublicIp(self, webName):
        return socket.getaddrinfo(webName, 80)