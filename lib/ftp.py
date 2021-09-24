from ftplib import FTP
class FTPScan:

    def __init__(self,verbosity,ip):
        self.verbosity = verbosity
        self.ip = ip
        self.ftp = self.FTP(ip)
    
    def anonymous_login(self):
        resp = self.ftp.login()
        if resp =='230 Login successful':
            print("FTP Anonymous Login Allowed !!")





