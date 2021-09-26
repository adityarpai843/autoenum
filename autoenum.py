import argparse
from lib.ftp import FTPScan
parser = argparse.ArgumentParser(prog="autoenum",formatter_class=argparse.RawDescriptionHelpFormatter,description="AutoEnum\n\nEnumerating well known ports to find vulnerabilities automatically",epilog="Ex: python3 autoenum.py 9.0.9.0 22,21\n")
parser.add_argument("ip",help="Enter host IP address")
parser.add_argument("ports", help="Enter the ports separated by comma")
parser.add_argument("-v","--verbose",help="make output verbose",action="store_true")
args = parser.parse_args()
for port in args.ports:
    if port == '21':
        fp = FTPScan(args.ip)
        fp.anonymous_login()
if args.verbose:
    print("Output is verbose")