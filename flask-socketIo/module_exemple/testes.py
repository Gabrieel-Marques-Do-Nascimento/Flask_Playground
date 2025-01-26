import pytest
from main import app, socketIo
# Substitua "app" pelo nome do arquivo da aplicação


@pytest.fixture
def socketio_client():
    # Configura o Flask-SocketIO com um cliente de teste
    app.config['TESTING'] = True
    test_client = socketIo.test_client(app)
    return test_client


def test_mensagem_do_cliente(socketio_client):
    # Envia dados para o evento 'mensagem_do_cliente'
    socketio_client.emit('mensagem_do_cliente', {'msg': 'Olá do cliente!'})

    # Captura os eventos recebidos pelo cliente
    received = socketio_client.get_received()
    # Verifica a resposta
    assert len(received) > 0
    assert received[0]['name'] == 'mensagem_do_servidor'  # Evento de resposta
    assert received[0]['args'][0]['resposta'] == "Servidor recebeu: {'msg': 'Olá do cliente!'}"


# run in `  pytest testes.py `
