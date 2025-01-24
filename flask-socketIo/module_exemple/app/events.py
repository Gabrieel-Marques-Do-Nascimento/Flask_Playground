from flask import Blueprint
from flask_socketio import emit

# Cria um Blueprint para eventos Socket.IO
socket_bp = Blueprint('socket_bp', __name__)

# Eventos Socket.IO
def register_socket_events(socketio):
    @socketio.on('mensagem_do_cliente')
    def handle_client_message(data):
        print(f"Mensagem recebida: {data}")
        # Responde de volta ao cliente
        emit('mensagem_do_servidor', {'resposta': f"Servidor recebeu: {data}"})