from flask import Flask, request
import json

app = Flask(__name__)

VERIFY_TOKEN = "meu_token_secreto"

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if token == VERIFY_TOKEN:
        return challenge
    return "Token inválido", 403

@app.route('/webhook', methods=['POST'])
def receive_message():
    data = request.get_json()
    print(json.dumps(data, indent=2))
    return "Evento recebido", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
