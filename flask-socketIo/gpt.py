from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Hello, World!'

@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    app.logger.critical(f"Mensagem recebida: {msg}")
    socketio.send("Mensagem recebida!")

if __name__ == '__main__':
    socketio.run(app)