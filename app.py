import os
from flask import Flask, request

app = Flask(__name__)

# Rota de teste para ver se o site está no ar
@app.route('/', methods=['GET'])
def home():
    return "Servidor do Bot rodando perfeitamente no Render!"

# Rota que o WhatsApp vai usar para se comunicar com seu bot
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    return "Webhook ativo e escutando!", 200

if __name__ == '__main__':
    # O Render exige que o app puxe a porta do sistema
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
