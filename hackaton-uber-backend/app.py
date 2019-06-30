import uuid
from pymongo import MongoClient
from flask import Flask 
from flask import request
from flask import jsonify
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
    return  jsonify(resultado=db[nome].find({"empresa": empresa}))

@app.route('/favorites', methods=['GET','POST'])
def favoritos():
    error = None 
    if request.method == 'GET':
        favoritos = db.favorito
        resultado = []

        for favorito in favoritos.find({"cliente.cliente_empresa_id": request.args.get('cliente')}):
            print(favorito)
            resultado.append(favorito["motorista"])

        return jsonify(favoritos=resultado) 
    
        
    if request.method == 'POST':
        req = request.json
        motoristas = db.motorista
        motorista = motoristas.find_one({"motorista_empresa_id":req['motorista_empresa_id']})

        if motorista == None:   
            motorista = { 
                "_id" : uuid.uuid4().hex,
                "nome" : req['nome_motorista'],
                "foto" : req['foto'],
                "motorista_empresa_id" : req['motorista_empresa_id'],
                "empresa" : req['empresa'], 
                "data_insercao" : datetime.timestamp(datetime.now())
            }
            motorista["mongo_id"] = motorista["_id"] 
            motoristas.insert_one(motorista)
            del motorista["_id"]
            es.index(index="motorista", doc_type='doc', id=uuid.uuid4().hex, body=motorista)

        clientes = db.cliente
        cliente = clientes.find_one({"cliente_empresa_id":req['cliente_empresa_id']})

        if cliente == None:
            cliente = {
                "_id" : uuid.uuid4().hex,
                "nome" : req['nome_cliente'],
                "cliente_empresa_id" : req['cliente_empresa_id'],
                "empresa" : req['empresa'],
                "data_insercao" : datetime.timestamp(datetime.now())
            }
            cliente["mongo_id"] = cliente["_id"] 
            clientes.insert_one(cliente)
            del cliente["_id"]
            es.index(index="cliente", doc_type='doc', id=uuid.uuid4().hex, body=cliente)

        favorito = {
            "_id" : uuid.uuid4().hex,
            "motorista" : motorista,
            "cliente" : cliente,
            "empresa" : req['empresa'],
            "data_insercao" : datetime.timestamp(datetime.now())
        }

        favoritos = db.favorito
        favorito["mongo_id"] = favorito["_id"] 
        favoritos.insert_one(favorito)
        del favorito["_id"]
        es.index(index="favorito", doc_type='doc', id=uuid.uuid4().hex, body=favorito)

    return jsonify(menssagem={"sucesso":"true"}) 

@app.route('/schedule', methods=['POST'])
def agendar():
    req = request.json
    agendamentos = db.agendamento
    motoristas = db.motorista
    motorista = motoristas.find_one({"motorista_empresa_id":req['motorista_empresa_id']})

    clientes = db.cliente
    cliente = clientes.find_one({"cliente_empresa_id":req['cliente_empresa_id']})

    agendamento = {
        "_id" : uuid.uuid4().hex,
        "motorista" : motorista,
        "cliente" : cliente,
        "empresa" : req['empresa'],
        "lat" : req['lat'],
        "long" : req['long'],
        "valor" : req['valor'],
        "datas" : req['datas'],
        "data_insercao" : datetime.timestamp(datetime.now())
    }

    agendamento["mongo_id"] = agendamento["_id"]
    agendamentos.insert_one(agendamento) 
    del agendamento["_id"]
    es.index(index="agendamento", doc_type='doc', id=uuid.uuid4().hex, body=agendamento)

    return jsonify(menssagem={"sucesso":"true"}) 

@app.route('/riders')
def geraViagensRecentes():
    return {
    
    }

@app.route('/estimate/price')
def geraEstimativa():
    return jsonify(resultado={"prices": [
    {
      "localized_display_name": "POOL",
      "distance": 6.17,
      "display_name": "POOL",
      "product_id": "26546650-e557-4a7b-86e7-6a3942445247",
      "high_estimate": 15,
      "low_estimate": 13,
      "duration": 1080,
      "estimate": "$13-14",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "uberX",
      "distance": 6.17,
      "display_name": "uberX",
      "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
      "high_estimate": 17,
      "low_estimate": 13,
      "duration": 1080,
      "estimate": "$13-17",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "uberXL",
      "distance": 6.17,
      "display_name": "uberXL",
      "product_id": "821415d8-3bd5-4e27-9604-194e4359a449",
      "high_estimate": 26,
      "low_estimate": 20,
      "duration": 1080,
      "estimate": "$20-26",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "SELECT",
      "distance": 6.17,
      "display_name": "SELECT",
      "product_id": "57c0ff4e-1493-4ef9-a4df-6b961525cf92",
      "high_estimate": 38,
      "low_estimate": 30,
      "duration": 1080,
      "estimate": "$30-38",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "BLACK",
      "distance": 6.17,
      "display_name": "BLACK",
      "product_id": "d4abaae7-f4d6-4152-91cc-77523e8165a4",
      "high_estimate": 43,
      "low_estimate": 43,
      "duration": 1080,
      "estimate": "$43.10",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "SUV",
      "distance": 6.17,
      "display_name": "SUV",
      "product_id": "8920cb5e-51a4-4fa4-acdf-dd86c5e18ae0",
      "high_estimate": 63,
      "low_estimate": 50,
      "duration": 1080,
      "estimate": "$50-63",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "ASSIST",
      "distance": 6.17,
      "display_name": "ASSIST",
      "product_id": "ff5ed8fe-6585-4803-be13-3ca541235de3",
      "high_estimate": 17,
      "low_estimate": 13,
      "duration": 1080,
      "estimate": "$13-17",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "WAV",
      "distance": 6.17,
      "display_name": "WAV",
      "product_id": "2832a1f5-cfc0-48bb-ab76-7ea7a62060e7",
      "high_estimate": 33,
      "low_estimate": 25,
      "duration": 1080,
      "estimate": "$25-33",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "TAXI",
      "distance": 6.17,
      "display_name": "TAXI",
      "product_id": "3ab64887-4842-4c8e-9780-ccecd3a0391d",
      "high_estimate": "",
      "low_estimate": "",
      "duration": 1080,
      "estimate": "Metered",
      "currency_code": ""
    }
  ]
  })


if __name__ == '__main__':
    app.run(debug=True)