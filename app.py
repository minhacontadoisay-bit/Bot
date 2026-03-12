import os
from flask import Flask, request

app = Flask(__name__)

# Essa é a senha secreta que a Meta vai pedir (pode deixar essa mesma)
TOKEN_DESEJADO = "meubot123"

@app.route('/', methods=['GET'])
def home():
    return "Servidor do Bot rodando perfeitamente no Render!"

# Essa é a rota que a Meta vai tentar acessar
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Aqui o servidor faz o "aperto de mãos" com a Meta
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode and token:
            if mode == 'subscribe' and token == TOKEN_DESEJADO:
                print("WEBHOOK VERIFICADO COM SUCESSO!")
                return challenge, 200
            else:
                return 'Senha incorreta', 403
        return 'Hello World', 200

    elif request.method == 'POST':
        # Aqui é onde as mensagens de texto vão chegar no futuro!
        body = request.get_json()
        print("MENSAGEM RECEBIDA DO WHATSAPP:", body)
        return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
