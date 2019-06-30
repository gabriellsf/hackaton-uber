from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)
import urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch

#es = Elasticsearch(['https://6vi035crgt:w8no1zyb2i@meu-favorito-dashboa-543171073.ap-southeast-2.bonsaisearch.net:443'])
es = Elasticsearch(
    'meu-favorito-dashboa-543171073.ap-southeast-2.bonsaisearch.net',
    http_auth=('6vi035crgt', 'w8no1zyb2i'),
    scheme="https",
    port=443,
    verify_certs=False
)

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('44KXC4kr2Jk8r3mV')

client = MongoClient('mongodb://%s:%s@meu-favorito.sv.ufabcnext.com:15003/' % (username, password))
db = client.uberhack

@app.route('/')
def hello():
    return  "Bem vindo a API MeuFavorito"

@app.route('/listar/<nome>/<empresa>')
def buscarTodos(nome, empresa):
    return db[nome].find({"empresa": empresa})

@app.route('/favorites/<cliente>', methods=['GET','POST'])
def favoritos(cliente):
    error = None 
    if request.method == 'GET':
        favoritos = db.favorito
        favoritos.find({"cliente.cliente_id": cliente})
        resultado = []

        for favorito in favoritos:
            resultado.append(favorito.motorista)

        return resultado
        
    if request.method == 'POST':
        motoristas = db.motorista
        motorista = motoristas.find_one({"motorista_empresa_id":request.form['motorista_empresa_id']})

        if motorista == None:   
            motorista = {
                "nome" : request.form['nome_motorista'],
                "foto" : request.form['foto'],
                "motorista_empresa_id" : request.form['motorista_empresa_id'],
                "empresa" : request.form['empresa'], 
                "data_insercao" : datetime.now()
            }
            motorista_id = motoristas.insert_one(motorista).inserted_id
            es.index(index="motorista", doc_type='_motorista', id=motorista_id, body=motorista)
        else:
            motorista_id = motorista['motorista_id']

        clientes = db.cliente
        cliente = clientes.find_one({"cliente_empresa_id":request.form['cliente_empresa_id']})

        if cliente == None:
            cliente = {
                "nome" : request.form['nome_cliente'],
                "cliente_empresa_id" : request.form['cliente_empresa_id'],
                "empresa" : request.form['empresa'],
                "data_insercao" : datetime.now()
            }
            cliente_id = clientes.insert_one(cliente).inserted_id
            es.index(index="cliente", doc_type='_cliente', id=cliente_id, body=cliente)
        else:
            cliente_id = cliente['cliente_id']

        favorito = {
            "motorista" : motorista,
            "cliente" : cliente,
            "empresa" : request.form['empresa'],
            "data_insercao" : datetime.now()
        }

        favoritos = db.favorito
        favorito_id = favoritos.insert_one(favorito).inserted_id
        es.index(index="favorito", doc_type='_favorito', id=favorito_id, body=favorito)

    return True

@app.route('/schedule', methods=['POST'])
def agendar():
    agendamentos = db.agendamento
    
    agendamento = {
        "motorista_id" : request.form['motorista_id'],
        "cliente_id" : request.form['cliente_id'],
        "empresa" : request.form['empresa'],
        "lat" : request.form['lat'],
        "long" : request.form['long'],
        "valor" : request.form['valor'],
        "datas" : request.form['data'],
        "data_insercao" : datetime.now()
    }

    agendamento_id = agendamentos.insert_one(agendamento).inserted_id
    es.index(index="agendamento", doc_type='_agendamento', id=agendamento_id, body=agendamento_id)

    return True

if __name__ == '__main__':
    app.run()