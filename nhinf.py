#import ezhack as ez
import ezhacker as ezk
import datetime
# Nighthawk Interface script.
from flask import Flask


app = Flask(__name__)
host = ezk.Host("192.168.1.93","metaspoop")
#host = ezk.Host("134.129.92.202","metaspoop")

#192.168.1.93
#134.129.92.202
def main():
	ip = ezk.scan_for_hosts()
	print(str(ip))
	# ezk.scan_target(host)
    #ezk.scan_target("192.168.1.3") # default is aggressive scan
	ezk.lookup_exploit(host)
    #payload = build_payload(host) # default is reverse shell
    #session = exploit_target(host)
    #drop_payload(payload,session)
    #priv = handle_host(cmd="id")
    #print(priv)

@app.route("/")
def ping():
    return "Server is online. " + str(datetime.datetime.now())

@app.route("/")
def scan():
    ip = ezk.scan_for_hosts()
    return str(ip)

if __name__ == '__main__':
    main()
