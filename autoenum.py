import argparse
from lib.ftp import FTPScan
from pyfiglet import Figlet
parser = argparse.ArgumentParser(prog="autoenum",description="AutoEnum\n\nEnumerating well known ports to find vulnerabilities automatically")
parser.add_argument("ip",help="Enter host IP address")
parser.add_argument("ports", help="Enter the ports separated by comma")
parser.add_argument("-v","--verbose",help="make output verbose",action="store_true")
args = parser.parse_args()
f = Figlet(font='slant')
print(f.renderText('Autoenum'))
print("\nEnumerating well known ports to find vulnerabilities automatically\n")
print("\n Ex: python3 autoenum.py 9.0.9.0 22,21 \n")
ports = args.ports.split(',')
for port in ports:
    if port == '21':
        fp = FTPScan(args.ip)
        fp.anonymous_login()
if args.verbose:
    print("Output is verbose")