from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def set_cookie():
    response = make_response("Cookie is set")
    # cookies nao acessíveis pelo js
    response.set_cookie('my_secure_cookie', 'cookie_value', httponly=True)
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('my_secure_cookie')
    return f"Cookie value: {cookie_value}"

if __name__ == '__main__':
    app.run(debug=True)
