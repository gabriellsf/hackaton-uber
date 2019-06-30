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

@app.route('/favorites', methods=['GET','POST'])
def favoritos(cliente):
    error = None 
    if request.method == 'GET':
        favoritos = db.favorito
        favoritos.find({"cliente.cliente_id": request.args.get('cliente')})
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

@app.route('/riders')
def geraViagensRecentes():
    return {
    "count": 15,
    "history": [
        {
        "status": "completed",
        "distance": 1.4780860317,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475545183,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475545808,
        "request_id": "fb0a7c1f-2cf7-4310-bd27-8ba7737362fe",
        "request_time": 1475545095
        },
        {
        "status": "completed",
        "distance": 1.2792152568,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475513472,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475513898,
        "request_id": "d72338b0-394d-4f0e-a73c-78d469fa0c6d",
        "request_time": 1475513393
        },
        {
        "status": "completed",
        "distance": 1.5084526246,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475170251,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475171154,
        "request_id": "2b61e340-27bd-4937-8304-122009e4a393",
        "request_time": 1475170088
        },
        {
        "status": "completed",
        "distance": 1.4705337758,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475027766,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475028387,
        "request_id": "58cb7b3c-fe22-47b4-94c0-2cf08b34f4be",
        "request_time": 1475027705
        },
        {
        "status": "completed",
        "distance": 0.6489455763,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475002745,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475003150,
        "request_id": "57be6f97-e10f-411e-a87e-670011c46b55",
        "request_time": 1475002656
        },
        {
        "status": "completed",
        "distance": 0.6632030652,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1475001862,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1475002218,
        "request_id": "0ca65d53-3351-4f3b-b07f-55e4fe4c1ad9",
        "request_time": 1475001534
        },
        {
        "status": "completed",
        "distance": 1.3935675129,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1474995527,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1474995943,
        "request_id": "c0453d97-4330-4ec2-88ab-38678101cc0b",
        "request_time": 1474995056
        },
        {
        "status": "completed",
        "distance": 1.5046201975,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1474909791,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1474910341,
        "request_id": "35822455-e4f5-4339-b763-6fc3ea16dc61",
        "request_time": 1474909743
        },
        {
        "status": "completed",
        "distance": 2.4445998557,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1474685017,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1474685568,
        "request_id": "81a0ffda-a879-4443-beb8-e253f4d19ecc",
        "request_time": 1474684872
        },
        {
        "status": "completed",
        "distance": 1.3603866105,
        "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
        "start_time": 1474651767,
        "start_city": {
            "latitude": 37.7749,
            "display_name": "San Francisco",
            "longitude": -122.4194
        },
        "end_time": 1474652253,
        "request_id": "97736867-41ca-432a-b7e9-909e66d833ba",
        "request_time": 1474651636
        }
    ],
    "limit": 10,
    "offset": 0
}

@app.route('/estimate/price')
def geraEstimativa():
    return { "prices": [
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
      "high_estimate": null,
      "low_estimate": null,
      "duration": 1080,
      "estimate": "Metered",
      "currency_code": null
    }
  ]
}


if __name__ == '__main__':
    app.run()