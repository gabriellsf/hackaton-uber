<p align="center">
  <img src="https://github.com/gabriellsf/hackaton-uber/blob/master/app/src/assets/logo.png" height="56" /><br /><br />
  <img src="https://github.com/gabriellsf/hackaton-uber/blob/master/demo-app.gif" />
</p>
<br />

# Meu Favorito - API + Interface Web/Mobile para fidelizar passageiros e motoristas

O Meu Favorito é um serviço para fidelização de confiança para plataformas de aplicativo de solicitação de corridas.

<img src="https://github.com/gabriellsf/hackaton-uber/blob/master/arquitetura.png" />

* Esse GIF representa a versão MVP com o uso da nossa API para o nosso primeiro cliente (Uber)

Rotas para Integração da API

```
# Endpoint para listagem dos favoritos
GET http://meu-favorito-api.herokuapp.com/favorites?cliente=<ID_DO_USUARIO_DA_EMPRESA>

{
  "favoritos": [
      {
          "data_insercao": 1561896256.280419,
          "empresa": "uber",
          "foto": "https://cdn-ofuxico.akamaized.net/img/upload/noticias/2018/05/03/tais-araujo-deixa-o-elenco-do-saia-justa-nota_303504_36_319447_36.jpg",
          "mongo_id": "0230371a344f4b5ca11125dc0aa68eec",
          "motorista_empresa_id": "123",
          "nome": "Thais"
      }
  ]
}

* ID do usuário no Uber/99/Cabify...
```

```
# Endpoint para favoritar motorista
POST http://meu-favorito-api.herokuapp.com/favorites
{
  "motorista_empresa_id" : "123",
  "nome_motorista" : "Thais",
  "foto" : "https://cdn-ofuxico.akamaized.net/img/upload/noticias/2018/05/03/tais-araujo-deixa-o-elenco-do-saia-justa-nota_303504_36_319447_36.jpg",
  "empresa" : "uber",
  "cliente_empresa_id" : "321",
  "nome_cliente" : "Marcelo"
}
```

```
# Endpoint para fazer estimativa de valor de acordo com o que foi agendado

GET http://meu-favorito-api.herokuapp.com/estimate/price
{
  "resultado": {
      "prices": [
          {
              "currency_code": "USD",
              "display_name": "uberX",
              "distance": 6.17,
              "duration": 1080,
              "estimate": "$13-17",
              "high_estimate": 17,
              "localized_display_name": "uberX",
              "low_estimate": 13,
              "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d"
          },
          {
              "currency_code": "",
              "display_name": "TAXI",
              "distance": 6.17,
              "duration": 1080,
              "estimate": "Metered",
              "high_estimate": "",
              "localized_display_name": "TAXI",
              "low_estimate": "",
              "product_id": "3ab64887-4842-4c8e-9780-ccecd3a0391d"
          }
      ]
  }
}
```

```
# Endpoint para retornar meus últimos motoristas

GET http://meu-favorito-api.herokuapp.com/riders
{
    "resultado": {
        "prices": [
            {
                "currency_code": "USD",
                "display_name": "uberX",
                "distance": 6.17,
                "duration": 1080,
                "estimate": "$13-17",
                "high_estimate": 17,
                "localized_display_name": "uberX",
                "low_estimate": 13,
                "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d"
            },
            {
                "currency_code": "",
                "display_name": "TAXI",
                "distance": 6.17,
                "duration": 1080,
                "estimate": "Metered",
                "high_estimate": "",
                "localized_display_name": "TAXI",
                "low_estimate": "",
                "product_id": "3ab64887-4842-4c8e-9780-ccecd3a0391d"
            }
        ]
    }
}
```

# Tecnologias Utilizadas:
- [Vue.js + PWA](https://vuejs.org/), 
- [Python3 + Flesk](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [ElasticSearch](https://www.elastic.co/pt/)
- [Kibana](https://www.elastic.co/pt/products/kibana)

Integrações:
- [Uber Developers](https://developer.uber.com/docs)

Infraestrutura:
- [Heroku](https://www.heroku.com/) - API
- [DigitalOcean](https://www.digitalocean.com/) - Banco de Dados
- [Bonsai](https://bonsai.io/) - Analytics + BI

