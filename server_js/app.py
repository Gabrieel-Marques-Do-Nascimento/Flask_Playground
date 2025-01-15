from flask import Flask, send_from_directory
from flask_cors import CORS

# The Flask application instance. This is the main entry point for the Flask application and is used to handle incoming HTTP requests and route them to the appropriate view functions.
app = Flask(__name__)
CORS(app)


@app.route('/export', methods=['GET'])
def export():
    # A função de exportação é uma função de visualização que lida com a solicitação de exportação. Ele retorna um arquivo com o nome "export.js" que contém as funcionalidades de usuarios.
    # server_js\js\export.mjs
    print('C:\__projetos_V@___\Flask_Playground\server_js\js\\', 'export.mjs')
    return send_from_directory('C:/__projetos_V@___/Flask_Playground/server_js/js/', 'export.mjs', mimetype='text/javascript')
    return '<h1> hello</h1>'    #


if __name__ == '__main__':
    app.run(debug=True)
