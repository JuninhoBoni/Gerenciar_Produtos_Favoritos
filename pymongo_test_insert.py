import pymongo


class MongoDB:
    def __init__(self):
        conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = conexao["mydatabase"]
        self.collection = self.database["customers"]

    def contar_cliente(self):
        self.quantidade = self.collection.count_documents(self.filtrar)

    def criar_cliente(self):
        self.contar_cliente()
        if self.quantidade == 0:
            self.collection.insert_one(self.dicionario)

    def visualizar_cliente(self):
        print(self.collection.find_one(self.filtrar))

    def atualizar_cliente(self):
        x = self.collection.update_one(self.filtrar, self.novovalor)
        print(x.raw_result)

    def remover_cliente(self):
        self.collection.delete_one(self.filtrar)

mongo = MongoDB()
mongo.dicionario = {"nome" : "Peteswr", 
                    "email" : "teste@teste.com",
                    "status" : "P",
                    "chave" : "123",
                    "favoritos" : [""],
                    }
mongo.novovalor = {"$set": {'favoritos': ["asfd"]}}
mongo.filtrar = {'email': 'teste@teste.com'}
#mongo.criar_cliente()
#mongo.visualizar_cliente()
mongo.atualizar_cliente()
#mongo.visualizar_cliente()
#mongo.remover_cliente()
mongo.visualizar_cliente()