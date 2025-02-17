from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dicionário para armazenar usuários conectados e seus IDs de sessão
usuarios_conectados = {}

# Quando um usuário se conecta
@socketio.on('connect')
def handle_connect():
    print(f'Novo usuário conectado: {request.sid}')

# Evento para registrar o ID do usuário
@socketio.on('registrar_usuario')
def registrar_usuario(data):
    usuario_id = data['usuario_id']
    usuarios_conectados[usuario_id] = request.sid
    print(f'Usuário {usuario_id} registrado com SID {request.sid}')

# Enviar mensagem para um usuário específico
@socketio.on('enviar_mensagem')
def enviar_mensagem(data):
    destinatario_id = data['destinatario_id']
    mensagem = data['mensagem']

    # Verifica se o destinatário está conectado
    if destinatario_id in usuarios_conectados:
        destinatario_sid = usuarios_conectados[destinatario_id]
        emit('mensagem_privada', {'mensagem': mensagem}, room=destinatario_sid)
        print(f'Mensagem enviada para {destinatario_id}: {mensagem}')
    else:
        print(f'O usuário {destinatario_id} não está conectado.')

# Quando o usuário desconectar
@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    for usuario_id, conectado_sid in list(usuarios_conectados.items()):
        if conectado_sid == sid:
            print(f'Usuário {usuario_id} desconectado.')
            del usuarios_conectados[usuario_id]
            break

if __name__ == '__main__':
    socketio.run(app, debug=True)