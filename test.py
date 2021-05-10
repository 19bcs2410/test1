from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask(__name__)



socketio = SocketIO(app)




@app.route('/')
def homepage():
   
    return render_template('test.html')


    




if __name__ == '__main__':
    socketio.run(app,debug=True)