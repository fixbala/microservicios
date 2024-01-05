from flask import Flask, request, jsonify

app = Flask(__name__)

# Definir las rutas del chatbot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    # Lógica del chatbot
    # Aquí puedes procesar la pregunta del usuario y generar la respuesta adecuada

    response = {
        'response': '¡Hola! ¿En qué puedo ayudarte hoy?'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
