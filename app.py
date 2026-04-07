from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota que o Google Sheets vai acessar
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    dados = request.json
    
    protocolo = dados.get('protocol')
    local = dados.get('location')
    problema = dados.get('issue')
    
    # Texto formatado da mensagem para o WhatsApp
    mensagem_whatsapp = (
        f"🚨 *REPARO URGENTE SEDUC* 🚨\n\n"
        f"*Protocolo:* {protocolo}\n"
        f"*Local:* {local}\n"
        f"*Problema:* {problema}\n\n"
        f"Por favor, verifique imediatamente."
    )
    
    # Exibe no terminal do servidor
    print(f"🚨 URGENTE recebido: Protocolo {protocolo} no local {local}.")
    
    # =========================================================
    # INSIRA SUA LÓGICA DE ENVIO DO WHATSAPP AQUI
    # (Ex: pywhatkit.sendwhatmsg_to_group(...) passando a variável mensagem_whatsapp)
    # =========================================================
    
    # Responde ao Google Sheets que tudo ocorreu bem
    return jsonify({
        "status": "sucesso", 
        "mensagem": "Alerta do WhatsApp acionado com sucesso!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)