from flask import Blueprint, render_template
from flask_socketio import emit, SocketIO
# 													entrar,	 sair
from flask_socketio import  join_room, leave_room

# Cria um Blueprint para eventos Socket.IO
socket_bp = Blueprint('socket_bp', __name__)

@socket_bp.route("/channel")
def channel():
	return render_template("room.html")




# Eventos Socket.IO
def register_socket_events(socketio: SocketIO):
    @socketio.on('mensagem_do_cliente')
    def handle_client_message(data):
        print(f"Mensagem recebida: {data}")
        # Responde de volta ao cliente
        emit('mensagem_do_servidor', {'resposta': f"Servidor recebeu: {data}"})
        
    @socketio.on("message")
    def mesage(data):
    	emit("message", data, broadcast=True)

    @socketio.on("channel")
    def channel(data):
    	emit("channel", data, broadcast=True, to=data["room"])
    	    	    	
    @socketio.on("join")
    def entrar(room):
    	name = room["name"]
    	join_room(room["room"])
    	emit("join", name+"   (-_-)  "+room["room"] )
 
    @socketio.on("leave")
    def sair(room):
    	name = room["name"]
    	leave_room(room["room"])
    	emit("leave", name+"   quicked  ")
    
    