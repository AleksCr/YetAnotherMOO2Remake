from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import lbx_parser
app = Flask(__name__)
socketio = SocketIO(app)

print('test')
parser = lbx_parser.LBXReader()
parser.read('TECHNAME.LBX')

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})
    print('my event')

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)
    print('my broadcast event')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')