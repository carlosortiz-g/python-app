from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return  jsonify({ 
    	'hostname': socket.gethostname(),
    	'time': datetime.datetime.now().strftime("%I:%M:%p on %B %d, %Y"),
        'message': 'Estas haciendo un gran trabajo!!!',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')
def health():
    return  jsonify({ 'status': 'UP'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")


