from marvelmind import MarvelmindHedge
import threading
import time
import sys
from flask import Flask, render_template
global Position
from flask_socketio import SocketIO, send, emit

hedge = MarvelmindHedge(tty="COM4", adr=2, debug=False)  # create MarvelmindHedge thread
hedge.start()  # start thread
app = Flask(__name__)
@app.route("/")
def server():
    print(hedge.IMUData())
    while True:
        return str(hedge.IMUData())x
@app.route("/test")
def test():
    print(hedge.IMUData())
    while True:
        return render_template('reload.html', row=str(hedge.IMUData()))

@app.route("/test2")
def test():
    print(hedge.IMUData())
    while True:
        row = str(hedge.IMUData())
        socketio.emit('message', {'msg': 'test', 'text':row}, broadcast =True)
        return render_template('reload.html')
if __name__=='__main__':
    app.run(debug=False)
