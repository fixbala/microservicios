from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Crear el chatbot
chatbot = ChatBot('ComidasRapidasBot')

# Entrenar el chatbot con el corpus en español
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.spanish')

# Ruta principal de la aplicación web
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para recibir y procesar las preguntas del usuario
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]
    bot_response = chatbot.get_response(user_message).text
    return bot_response

if __name__ == "__main__":
    app.run(debug=True, port=8000) 
