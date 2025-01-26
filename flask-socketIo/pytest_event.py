import pytest
from flask_socketio import SocketIO
# Substitua "app" pelo nome do seu arquivo de aplicação
from gpt import app, socketio


@pytest.fixture
def socketio_client():
    # Configura o Flask-SocketIO com um cliente de teste
    app.config['TESTING'] = True
    test_client = socketio.test_client(app)
    return test_client


def test_socketio_message(socketio_client):
    # Envia uma mensagem ao servidor usando o evento padrão 'message'
    socketio_client.send('Olá, servidor!')

    # Captura a resposta do servidor
    received = socketio_client.get_received()

    # Verifica se a resposta é válida
    assert len(received) > 0
    # nome do evento
    assert received[0]['name'] == 'message'
    assert received[0]['args'][0] == 'Mensagem recebida!'


# pytest pytest_event.py
