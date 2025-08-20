# O nome do arquivo precisa ser app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == '__main__': # quando executamos de forma manual o nosso arquivo, o __name__ é igual a __main__
    app.run(debug=True) #este parâmetro vai permitir que vejemos diversas informações de debug no terminal.  Apenas recomendado para desenvolvimento.
# Para produção, é recomendado desativar o modo debug.