from flask import Flask
from flask_cors import  CORS
from flask_socketio import SocketIO
from .events import socket_bp, register_socket_events
from .routes import pages


socketIo = SocketIO()


def creat_app():
	app = Flask(__name__)
	CORS(app)
	app.config["SECRET_KEY"] = "secret"
	socketIo.init_app(app)
	app.register_blueprint( pages)
	app.register_blueprint(socket_bp)
	register_socket_events(socketio=socketIo)
	return  app




"""

from flask import Flask, render_template
from flask_socketio import SocketIO
from events.socket_events import socket_bp, register_socket_events

# Inicializa o Flask e o SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
socketio = SocketIO(app)

# Registra o Blueprint
app.register_blueprint(socket_bp)

# Registra os eventos Socket.IO
register_socket_events(socketio)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
"""