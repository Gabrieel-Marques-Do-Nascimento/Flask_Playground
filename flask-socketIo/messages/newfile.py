from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dicionário para armazenar inscrições de notificações
user_subscriptions = {}

@app.route('/')
def index():
    return render_template('index.html')  # Vamos usar um HTML simples para o cliente

@socketio.on('connect')
def handle_connect():
    print(f'Usuário conectado: {request.sid}')

@socketio.on('subscribe_to_notifications')
def handle_subscription(data):
    room = data['room']
    user_id = request.sid

    if room not in user_subscriptions:
        user_subscriptions[room] = set()

    user_subscriptions[room].add(user_id)
    print(f'Usuário {user_id} inscrito para notificações da sala {room}')

@socketio.on('join_room')
def handle_join(data):
    room = data['room']
    join_room(room)
    print(f'Usuário {request.sid} entrou na sala {room}')
    emit('message', f'Usuário {request.sid} entrou na sala {room}', to=room)

@socketio.on('send_message')
def handle_message(data):
    room = data['room']
    message = data['message']
    print(f'Mensagem para sala {room}: {message}')

    # Envia a mensagem para todos na sala
    emit('message', f'{request.sid}: {message}', to=room)

    # Notificação para usuários inscritos que NÃO estão na sala
    if room in user_subscriptions:
        for user_id in user_subscriptions[room]:
            if user_id != request.sid:  # Evitar notificar o próprio remetente
                emit('new_message_notification', {
                    'room': room,
                    'message': f'Nova mensagem em {room}: {message}'
                }, to=user_id)

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Usuário desconectado: {request.sid}')
    # Remove o usuário de todas as inscrições
    for room in user_subscriptions:
        user_subscriptions[room].discard(request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)