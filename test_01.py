#autor: Michel
#data: 27/12/2027
# teste automatizado para criar um banco de dados no Appwrite

# criando as importações necessárias
from appwrite.client import Client
from appwrite.services.databases import Databases


Client = Client()
Client.set_endpoint('http://localhost/v1') # substitua pelo endpoint do seu Appwrite
Client.set_project('seu_id_de_projeto') # substitua pelo ID do seu projeto
Client.set_key('sua_chave_de_api') # substitua pela sua chave de API

db = Databases(Client)

# criando registro de teste
db.create_document(
    database_id='seu_id_de_banco_de_dados', # substitua pelo ID do seu banco de dados
    collection_id='seu_id_de_colecao', # substitua pelo ID da sua coleção
    document_id='unique()', # cria um ID único para o documento
    data={
        'titulo': 'Buraco na frente da escola',
        'descricao': 'Um buraco enorme que surgiu após a chuva.',
        'tipo': 'buraco',
        'lat': -23.5505,
        'long': -46.6333,
        'fotoid': 'id_da_foto_aqui'
    }
)
print("Documento criado com sucesso!")
