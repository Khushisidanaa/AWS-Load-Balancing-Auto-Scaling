from flask import Flask, request, jsonify
from subprocess import Popen
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start the stress_cpu.py script without blocking
    Popen(["python", "stress_cpu.py"])
    return jsonify(message="CPU stress test initiated"), 202

@app.route('/', methods=['GET'])
def get_private_ip():
    # Return the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return jsonify(ip_address=private_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)  # Replace with your actual port
