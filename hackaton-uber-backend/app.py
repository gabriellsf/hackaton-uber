import uuid
from pymongo import MongoClient
from flask import Flask 
from flask import request
from flask import jsonify
app = Flask(__name__)
import urllib.parse
from datetime import datetime
from elasticsearch import Elasticsearch

#Conexão com banco ElasticSearch
es = Elasticsearch(
    'meu-favorito-dashboa-543171073.ap-southeast-2.bonsaisearch.net',
    http_auth=('6vi035crgt', 'w8no1zyb2i'),
    scheme="https",
    port=443,
    verify_certs=False 
)

#Conexão com banco MongoDB
username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('44KXC4kr2Jk8r3mV')
client = MongoClient('mongodb://%s:%s@meu-favorito.sv.ufabcnext.com:15003/' % (username, password))
db = client.uberhack

#Rota Inicial
@app.route('/')
def hello():
    return  "Bem vindo a API MeuFavorito"

#Endpoint GET para buscar favoritos de um cliente 
#Endpoint POST para salvar favorito entre cliente e motorista
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
                "data_insercao" : datetime.now().isoformat()
            }
            motorista["mongo_id"] = motorista["_id"] 
            motoristas.insert_one(motorista)
            del motorista["_id"]
            es.index(index="motorista", doc_type='doc_motorista', id=uuid.uuid4().hex, body=motorista)

        clientes = db.cliente
        cliente = clientes.find_one({"cliente_empresa_id":req['cliente_empresa_id']})

        if cliente == None:
            cliente = {
                "_id" : uuid.uuid4().hex,
                "nome" : req['nome_cliente'],
                "cliente_empresa_id" : req['cliente_empresa_id'],
                "empresa" : req['empresa'],
                "data_insercao" : datetime.now().isoformat()
            }
            cliente["mongo_id"] = cliente["_id"] 
            clientes.insert_one(cliente)
            del cliente["_id"]
            es.index(index="cliente", doc_type='doc_cliente', id=uuid.uuid4().hex, body=cliente)

        favorito = {
            "_id" : uuid.uuid4().hex,
            "motorista" : motorista,
            "cliente" : cliente,
            "empresa" : req['empresa'],
            "data_insercao" : datetime.now().isoformat()
        }

        favoritos = db.favorito
        favorito["mongo_id"] = favorito["_id"] 
        favoritos.insert_one(favorito)
        del favorito["_id"]
        es.index(index="favorito", doc_type='doc_favorito', id=uuid.uuid4().hex, body=favorito)

    return jsonify(menssagem={"sucesso":"true"}) 

#Agendamento de corridas com um favorito
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
        "data_insercao" : datetime.now().isoformat()
    }

    agendamento["mongo_id"] = agendamento["_id"]
    agendamentos.insert_one(agendamento) 
    del agendamento["_id"]
    es.index(index="agendamento", doc_type='doc_agendamento', id=uuid.uuid4().hex, body=agendamento)

    return jsonify(menssagem={"sucesso":"true"}) 

## Mock da API da uber pois a mesma está com problemas de como confirmado pelo Engenheiro responsavel no evento
## At 30 de Julho
@app.route('/riders')
def geraViagensRecentes():
    return jsonify(resultado={"drivers": [
    {
        "id": "1",
        "name": "Carlos Abreu",
        "photo": "https://randomuser.me/api/portraits/men/25.jpg"
    },
    {
        "id": "2",
        "name": "Roberto Ricardo",
        "photo": "https://randomuser.me/api/portraits/men/86.jpg",
    },
    {
        "id": "3",
        "name": "Giovanna Luz",
        "photo": "https://randomuser.me/api/portraits/women/82.jpg",
    },
    {
        "id": "4",
        "name": "Roberta Campos",
        "photo": "https://randomuser.me/api/portraits/women/95.jpg",
    },
    {
        "id": "5",
        "name": "Marcela Santos",
        "photo": "https://randomuser.me/api/portraits/women/41.jpg",
    },
    {
        "id": "6",
        "name": "Luana Ramos",
        "photo": "https://randomuser.me/api/portraits/women/62.jpg",
    }
  ]
  })

## Mock da API da uber pois a mesma está com problemas de como confirmado pelo Engenheiro responsavel no evento
## At 30 de Julho
@app.route('/estimate/price')
def geraEstimativa():
    return jsonify(resultado={"prices": [
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