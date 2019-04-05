#import ezhack as ez
import ezhacker as ezk
import datetime
# Nighthawk Interface script.
from flask import Flask


app = Flask(__name__)
fileName = "metaspoop"
host = ezk.Host("192.168.1.93",fileName)
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
#ip = []

@app.route("/")
def ping():
    return ("Server is online. " + str(datetime.datetime.now()))

@app.route("/scan_for_hosts")
def scan():
    ip = ezk.scan_for_hosts()
    return str(ip)

@app.route("/scan_target/<host_index>")
def scan_host(host_index):
	ips = ezk.scan_for_hosts()
	ip = ips[int(host_index)]
	host = ezk.Host(ip,fileName)
	print(ip)
	ezk.scan_target(host)

	with open(fileName + '.xml', 'r') as file:
		data = file.read()
		return data

# TODO: figure out a smoother way to call these functions without calling the
# entire stack again.
@app.route("/lookup_exploit")
def lookup_exploit():
	result = ezk.lookup_exploit(host)
	print(result)
	#return ezk.lookup_exploit(host)
	#host.ip_addr
	return "ran searchsploit"
#	with open(fileName + '.json', 'r') as file:
#		data = file.read()
#		return data


if __name__ == '__main__':
    #main()
    app.run(debug=True,host='0.0.0.0',port=5001)
