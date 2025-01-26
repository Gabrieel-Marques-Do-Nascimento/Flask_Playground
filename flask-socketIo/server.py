from flask import Flask
from flask_socketio import SocketIO


# utilizar SocketIO no app flask
# -----------------------------------------------------
app = Flask(__name__)

app.config["SECRET_KEY"] = "secreto"

soklcketio = SocketIO(app)

# inicia o server
# if __name__ == "__main__":
# soklcketio.run(app)

# -----------------------------------------------------

# caso use html css e js com front and

"""
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io();
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
</script>
"""

# -----------------------------------------------------


# inicia o server
if __name__ == "__main__":
    soklcketio.run(app)
