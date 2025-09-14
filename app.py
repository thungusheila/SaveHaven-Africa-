from flask import Flask, request, jsonify  
from dotenv import load_dotenv  
from hts_integration import create_token, mint_token  
from hcs_integration import create_topic, log_event  

load_dotenv()  
app = Flask(__name__)  

@app.route("/create_token", methods=["POST"])  
def api_create_token():  
    data = request.get_json()  
    token_id = create_token(data["name"], data["symbol"], int(data["initial_supply"]))  
    return jsonify({"tokenId": token_id})  

@app.route("/mint_token", methods=["POST"])  
def api_mint_token():  
    data = request.get_json()  
    status = mint_token(data["tokenId"], int(data["amount"]))  
    return jsonify({"status": status})  

@app.route("/create_topic", methods=["POST"])  
def api_create_topic():  
    topic_id = create_topic()  
    return jsonify({"topicId": topic_id})  

@app.route("/log_event", methods=["POST"])  
def api_log_event():  
    data = request.get_json()  
    status = log_event(data["topicId"], data["message"])  
    return jsonify({"status": status})  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)
