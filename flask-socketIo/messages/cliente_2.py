import socketio

# Cria uma instância do cliente Socket.IO
sio = socketio.Client()

# Conectando ao servidor
@sio.event
def connect():
    print('Conectado ao servidor!')
    # Registrando o usuário com ID 'usuario123'
    sio.emit('registrar_usuario', {'usuario_id': 'usuario123'})

# Recebendo mensagens privadas
@sio.on('mensagem_privada')
def on_mensagem_privada(data):
    print('Mensagem privada recebida:', data['mensagem'])

# Conectar ao servidor
sio.connect('http://localhost:5000')

# Enviar uma mensagem para outro usuário
sio.emit('enviar_mensagem', {'destinatario_id': 'usuario456', 'mensagem': 'Olá, tudo bem?'})

# Manter a conexão ativa
sio.wait()