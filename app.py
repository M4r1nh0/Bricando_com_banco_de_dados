from flask import Flask
from requests import post
from flask_restful import Resource, Api, reqparse
from lsuinox.Banco.Database import *
from console_logging.console import Console
console = Console()

#db = dataset.connect('sqlite:///:memory:')

db = Banco()
app = Flask(__name__)
api = Api(app)

class CADASTRAR_USUARIO(Resource):
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("id")
        argumentos.add_argument("nome")
        argumentos.add_argument("cpf")
        argumentos.add_argument("plano")
        argumentos.add_argument("cidade")
        argumentos.add_argument("bairro")
        argumentos.add_argument("rua")
        argumentos.add_argument("cep")
        argumentos.add_argument("quant_porcos")
        argumentos.add_argument("datetime")
        argumentos.add_argument("carencia")
        argumentos.add_argument("status_solicitacao")
        argumentos.add_argument("Forma_pagamento")
        argumentos.add_argument("Fatura")
        argumentos.add_argument("Mensalidade")
        dados = argumentos.parse_args()
        #print(dados)
        print("[*] cadastrando.... ")
        db.cadastro(dados)
        console.success("USUARIO CADASTRADO ")
        return {"mesage":"Cadasto feito com Sucesso !"}, 200

class about(Resource):
    def get(self):
        return {"mesage": "api construida pela suino-x"}, 200

class ATUALIZA_USUARIO(Resource):
    def post(self):
      argumentos = reqparse.RequestParser()
      #argumentos.add_argument("id")
      argumentos.add_argument("nome")
      argumentos.add_argument("cpf")
      argumentos.add_argument("plano")
      argumentos.add_argument("cidade")
      argumentos.add_argument("bairro")
      argumentos.add_argument("rua")
      argumentos.add_argument("cep")
      argumentos.add_argument("quant_porcos")
      #argumentos.add_argument("datetime")
      argumentos.add_argument("carencia")
      argumentos.add_argument("status_solicitacao")
      argumentos.add_argument("Forma_pagamento")
      argumentos.add_argument("Fatura")
      argumentos.add_argument("Mensalidade")
      dados = argumentos.parse_args()
      result = db.atualiza(dados['cpf'],dados)
      console.info("ATUALIZANDO DADOS DO USUARIO CADASTRADO ")
      return {"mesage": result}, 200


class LISTA_USUARIO(Resource):
     def post(self):
       console.info("LISTANDO USUARIOS ")
       argumentos = reqparse.RequestParser()
       argumentos.add_argument("busca")
       dados = argumentos.parse_args()
       result = db.lista(dados['busca'])       
       return {"mesage":result}, 200

class DELETA_USUARIO(Resource):
    def post(self):
      console.error("DELETANDO USUARIO ")
      argumentos = reqparse.RequestParser()
      argumentos.add_argument("cpf") 
      dados = argumentos.parse_args()
      print("DELETANDO USUARIO")
      result = db.deleta(dados['cpf'])
      return {"mesage": result}, 200


api.add_resource(about, "/")
api.add_resource(ATUALIZA_USUARIO, "/suinox/api/v1/update")
api.add_resource(LISTA_USUARIO, "/suinox/api/v1/lista")
api.add_resource(DELETA_USUARIO, "/suinox/api/v1/delete")
api.add_resource(CADASTRAR_USUARIO, "/suinox/api/v1/cadastro")


if __name__ == '__main__':
    console.log("START APP ")
    app.run(host="0.0.0.0", debug=True)
