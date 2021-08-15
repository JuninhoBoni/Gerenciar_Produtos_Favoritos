import pymongo
import os


class MongoDB:
    def __init__(self):
        conn = pymongo.MongoClient(
            f"mongodb+srv://favoritos-clientes:{os.environ['MONGO_PASS']}@cluster0.8na2s.mongodb.net/database?retryWrites=true&w=majority")
        database = conn["database"]
        self.collection = database["client_favorites"]

    def count_client(self):
        self.quantidade = self.collection.count_documents(self.filter)

    def create_client(self):
        self.count_client()
        self.id_client = ''
        if self.quantidade == 0:
            status = self.collection.insert_one(self.dictionary)
            self.id_client = str(status.inserted_id)

    def view_client(self):
        self.client = self.collection.find_one(self.filter)

    def update_client(self):
        status = self.collection.update_one(self.filter, self.new_value)
        self.status = status.raw_result
        self.view_client()

    def remove_client(self):
        status = self.collection.delete_one(self.filter)
        self.status = status.raw_result
