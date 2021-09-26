from ftplib import FTP
from clint.textui import colored, puts
class FTPScan:

    def __init__(self,ip,verbosity=False):
        self.verbosity = verbosity
        self.ip = ip
        self.ftp = FTP(self.ip)
    
    def anonymous_login(self):
        resp = self.ftp.login()
        if resp =='230 Login successful.':
            puts(colored.red('FTP Anonymous Login Allowed !!'))
        else:
            puts(colored.green('FTP Anonymous Login Blocked !!'))     





