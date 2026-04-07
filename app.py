from flask import Flask, request, jsonify

app = Flask(__name__)

# This creates a "listening station" at your-url.com/webhook
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # 1. Receive the data sent by Google Apps Script
    data = request.json
    
    protocol = data.get('protocol')
    location = data.get('location')
    issue = data.get('issue')
    
    # 2. Insert your existing WhatsApp logic here!
    # You can paste the code you previously used to message the WhatsApp group.
    # Use the 'protocol', 'location', and 'issue' variables in your message text.
    print(f"🚨 URGENT: {protocol} at {location}. Issue: {issue}")
    
    # 3. Tell Google Sheets the message was received successfully
    return jsonify({"status": "success", "message": "WhatsApp alert triggered!"}), 200

if __name__ == '__main__':
    app.run(debug=True)