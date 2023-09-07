import os
import time

import requests
from flask import Flask, jsonify, render_template
from wakeonlan import send_magic_packet

app = Flask(__name__)

SERVER_IP = '192.168.1.85'
SERVER_MAC = '40.a8.f0.a3.42.83'

def is_device_powered_on():
    """
    Check if a device on the local network is powered on.

    :param ip_address: The IP address or hostname of the device.
    :return: True if the device is powered on and reachable, False otherwise.
    """
    # Use the 'ping' command to check if the device is reachable
    response = os.system(f"ping -c 1 {SERVER_IP}")  # -c 1 means send only 1 ping packet

    # Check the response code
    if response == 0:
        return True  # Device is powered on and reachable
    else:
        return False  # Device is not reachable or powered off

def wake_up_server():
    send_magic_packet(SERVER_MAC, ip_address='192.168.1.255',)
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({'online':is_device_powered_on()})

@app.route('/boot')
def boot():
    if is_device_powered_on():
        return ''
    print('Trying to boot')
    wake_up_server()
    while not is_device_powered_on():
        time.sleep(5)
    return ''

if __name__== '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5465)