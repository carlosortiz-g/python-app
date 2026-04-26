from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return  jsonify({ 
    	'hostname': socket.gethostname(),
    	'time': datetime.datetime.now().strftime("%I:%M:%p on %B %d, %Y"),
        'message': 'Estás haciendo un gran trabajo!!!'
    })

@app.route('/api/v1/healthz')
def health():
    return  jsonify({ 'status': 'UP'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")


