from ftplib import FTP
class FTPScan:

    def __init__(self,ip,verbosity=False):
        self.verbosity = verbosity
        self.ip = ip
        self.ftp = FTP(self.ip)
    
    def anonymous_login(self):
        resp = self.ftp.login()
        if resp =='230 Login successful.':
            print("FTP Anonymous Login Allowed !!")
        else:
            print("Failed")     





