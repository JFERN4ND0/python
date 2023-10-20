from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('mensaje', methods=['POST'])
def mensaje():
    nombre = request.form.get('nombre')
    mensajes = f'Bienvenido,{nombre}'
    return render_template('index.html', mensajes = mensajes)

if __name__ == '_main_':
    app.run(debug=True)