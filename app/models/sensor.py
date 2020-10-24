from settings import load_database_sensor_params
import pymongo


class MongoDB():
    def __init__(self):
        """Constructor to model class."""
        self.sensor_params = load_database_sensor_params()
        try:
            self.client = pymongo.MongoClient(**self.sensor_params,
                                              serverSelectionTimeoutMS=10)
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

    def get_collection(self, collection='sensor'):
        db = self.client['smart-dev']
        return db[collection]

    def insert_one(self, body):
        try:
            collection = self.get_collection()
            collection.insert_one(body)
            return True
        except Exception as err:
            print(f'Erro ao inserir no banco de dados: {err}')
            return False

    def update_one(self, identifier, body, collection='sensor'):
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

    def get_one(self, identifier, collection='sensor'):
        collection = self.get_collection(collection)
        document = collection.find_one({"_id": identifier})
        return document

    def get_all(self, collection='sensor'):
        collection = self.get_collection(collection)
        document = collection.find()
        return document

    def get_winery_by_sensor_id(self, identifier):
        collection = self.get_collection('winery')
        return collection.find_one({"sensor._id": identifier})
