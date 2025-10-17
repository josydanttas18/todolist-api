# Importação das bibliotecas
from flask import Flask

#Cria o objeto do flask
app = Flask(__name__)

#Criando nossa primeira rota
@app.route('/api')
def imdex():
    return 'Api rodando'

    #Identifica que é arquivo principal
    #E liga o servidor executando o Flask 😊
if __name__ == '__main__':
     app.run(debug=True)
