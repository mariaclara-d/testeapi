from flask import Flask, request, jsonify
import json

app = Flask(__name__)

#criar rota para buscar id tendo como parametro o nome da skin


with open("cs2_marketplaceids.json", "r", encoding="utf-8") as file:
    skins_data = json.load(file)


def get_skin_id(skin_name):
   
    items = skins_data.get("items", {})
    
  
    for item_name, details in items.items():
        if item_name.lower() == skin_name.lower():
            return details.get("buff163_goods_id")  
    return None

# Rota para buscar o ID da skin
@app.route('/get_skin_id', methods=['GET'])
def get_skin():
    skin_name = request.args.get('name')
    if not skin_name:
        return jsonify({"error": "Skin name is required"}), 400

    skin_id = get_skin_id(skin_name)
    if skin_id is not None:
        return jsonify({"skin_name": skin_name, "skin_id": skin_id})
    else:
        return jsonify({"error": "Skin not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
