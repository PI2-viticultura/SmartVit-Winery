from settings import load_database_params
from extensions import client
import pymongo
import os


class MongoDB():
    def __init__(self):
        """Constructor to model class."""
        if(os.getenv('ENVIRONMENT') != 'developing_local'):
            self.client = client
        else:
            self.params = load_database_params()
            try:
                self.client = pymongo.MongoClient(
                    **self.params,
                    serverSelectionTimeoutMS=10
                )
            except Exception as err:
                print(f'Erro ao conectar no banco de dados: {err}')

    def test_connection(self):
        try:
            self.client.server_info()
            return True
        except Exception as err:
            print(f'Erro ao conectar no banco de dados: {err}')
            return False

    def close_connection(self):
        self.client.close()

    def get_collection(self, collection='winery'):
        db = self.client[os.getenv("DBNAME", "smart-dev")]
        return db[collection]

    def insert_one(self, body):
        try:
            collection = self.get_collection()
            return collection.insert_one(body)
        except Exception as err:
            print(f'Erro ao inserir no banco de dados: {err}')
            return False

    def update_one(self, identifier, body, collection='winery'):
        try:
            collection = self.get_collection(collection)

            collection.find_one_and_update(
                {"_id": identifier},
                {"$set": body}
            )
            return True

        except Exception as err:
            print(f'Erro ao atualizar no banco de dados: {err}')
            return False

    def delete_one(self, identifier):
        try:
            collection = self.get_collection()
            res = collection.delete_one({"id": identifier})
            return res.deleted_count
        except Exception as err:
            print(f'Erro ao deletar no banco de dados: {err}')
            return False

    def get_one(self, identifier, collection='winery'):
        collection = self.get_collection(collection)
        document = collection.find_one({"_id": identifier})
        return document

    def get_all(self, collection='winery'):
        collection = self.get_collection(collection)
        document = collection.find()
        return document

    def get_contract_by_winery_id(self, identifier):
        collection = self.get_collection('contracts')
        return collection.find_one({"winery._id": identifier})

    def get_winery_by_user(self, user_id):
        collection = self.get_collection('winery')
        return collection.find_one({"responsibles._id": user_id})
