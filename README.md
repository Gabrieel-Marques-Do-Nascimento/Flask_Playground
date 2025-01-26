
# Repositório de Exemplos com Flask e Flask-SocketIO  

Este repositório contém exemplos práticos para quem deseja explorar os recursos oferecidos pelo framework Flask e sua extensão Flask-SocketIO. Aqui, você encontrará implementações que demonstram desde o uso básico de rotas RESTful até a integração de WebSockets para comunicação em tempo real.  

## Estrutura do Repositório  

- **`/api_basico`**:  
  Exemplo de uma API RESTful simples com Flask. Este exemplo cobre:
  - Configuração básica do Flask.
  - Criação de rotas para métodos HTTP (GET, POST, PUT, DELETE).
  - Validação de dados de entrada com bibliotecas como `flask-restful` ou `marshmallow`.

- **`/websocket_exemplo`**:  
  Exemplo de comunicação em tempo real usando Flask-SocketIO. Este exemplo cobre:
  - Configuração do Flask-SocketIO para integrar WebSockets ao projeto.
  - Emissão e escuta de eventos entre cliente e servidor.
  - Aplicações práticas, como notificações em tempo real ou chats.  

- **`/auth_jwt`**:  
  Implementação de autenticação e autorização usando JWT (JSON Web Tokens).  
  - Registro e login de usuários.
  - Proteção de rotas com validação de tokens JWT.
  - Expiração e renovação de tokens.  

- **`/integracao_frontend`**:  
  Integração de uma API Flask com um front-end básico (usando HTML, CSS e JavaScript).  
  - Comunicação com a API por meio de `fetch` no front-end.
  - Exemplos de consumo de WebSockets no navegador.  

---

## Pré-Requisitos  
Certifique-se de ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual para instalar as dependências.  

### Instalação  
1. Clone este repositório:  
   ```bash  
   git clone https://github.com/seu_usuario/exemplos-flask  
   cd exemplos-flask  
   ```  

2. Crie um ambiente virtual e ative-o:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # Linux/macOS  
   venv\Scripts\activate     # Windows  
   ```  

3. Instale as dependências:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## Como Executar os Exemplos  

### API Básica  
Acesse a pasta `api_basico` e execute o arquivo principal:  
```bash  
cd api_basico  
python app.py  
```  
A API estará disponível em [http://localhost:5000](http://localhost:5000).  

### WebSocket com Flask-SocketIO  
Acesse a pasta `websocket_exemplo` e execute o servidor:  
```bash  
cd websocket_exemplo  
python app.py  
```  
Abra o arquivo `index.html` no navegador para testar a comunicação em tempo real.  

---

## Contribuição  
Contribuições são bem-vindas! Se você tiver sugestões ou exemplos adicionais, sinta-se à vontade para abrir uma issue ou enviar um pull request.  

---

## Licença  
Este repositório é licenciado sob a licença MIT.  

---  

Com este repositório, você terá uma base sólida para criar APIs e sistemas modernos utilizando Flask e Flask-SocketIO!