from flask import Flask
from flask import request
from flask import jsonify
import socket
import datetime

hitCount = 0
startTime = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

app = Flask(__name__)

@app.route("/")
def show_details() :
    global startTime
    global hitCount
    hitCount = hitCount + 1
    return "<html>" + \
           "<head><title>Docker + Flask Demo</title></head>" + \
           "<body>" + \
           "<table>" + \
           "<tr><td> Start Time </td> <td>" +  startTime + "</td> </tr>" \
           "<tr><td> Hostname </td> <td>" + socket.gethostname() + "</td> </tr>" \
           "<tr><td> Local Address </td> <td>" + socket.gethostbyname(socket.gethostname()) + "</td> </tr>" \
           "<tr><td> Remote Address </td> <td>" + request.remote_addr + "</td> </tr>" \
           "<tr><td> Server Hit </td> <td>" + str(hitCount) + "</td> </tr>" \
           "</table>" + \
           "</body>" + \
           "</html>"

@app.route("/json")
def send_json() :
    global startTime
    global hitCount
    hitCount = hitCount + 1
    return jsonify( {'StartTime' : startTime,
                     'Hostname': socket.gethostname(),
                     'LocalAddress': socket.gethostbyname(socket.gethostname()),
                     'RemoteAddress':  request.remote_addr,
                     'Server Hit': str(hitCount)} )

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
