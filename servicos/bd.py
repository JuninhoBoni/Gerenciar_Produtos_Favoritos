import pymongo


class MongoDB:
    def __init__(self):
        conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = conexao["database"]
        self.collection = self.database["clientes"]

    def contar_cliente(self):
        self.quantidade = self.collection.count_documents(self.filtrar)

    def criar_cliente(self):
        self.contar_cliente()
        self.id_cliente = ''
        if self.quantidade == 0:
            status = self.collection.insert_one(self.dicionario)
            self.id_cliente = str(status.inserted_id)

    def visualizar_cliente(self):
        self.cliente = self.collection.find_one(self.filtrar)

    def atualizar_cliente(self):
        status = self.collection.update_one(self.filtrar, self.novovalor)
        self.status = status.raw_result
        self.visualizar_cliente()

    def remover_cliente(self):
        status = self.collection.delete_one(self.filtrar)
        self.status = status.raw_result
