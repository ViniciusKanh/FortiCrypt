from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carregar o modelo
model_path = 'FortiCrypt.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Função para extrair características da senha
def extract_features(password):
    return {
        'length': len(password),
        'num_uppercase': sum(1 for c in password if c.isupper()),
        'num_numbers': sum(1 for c in password if c.isdigit()),
        'num_symbols': sum(1 for c in password if not c.isalnum())
    }

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    password = data.get("password")
    features = extract_features(password)
    prediction = model.predict([list(features.values())])[0]
    strength = {0: "Fraca", 1: "Média", 2: "Forte"}.get(prediction, "Indefinido")
    return jsonify({'password': password, 'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
