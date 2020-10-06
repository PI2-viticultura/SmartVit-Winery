from settings import load_database_params
import pymongo


class MongoDB():
    def __init__(self):
        """Constructor to model class."""
        self.params = load_database_params()
        try:
            self.client = pymongo.MongoClient(**self.params,
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

    def get_collection(self, collection='winery'):
        db = self.client['smart-dev']
        collection = db['winery']
        return collection

    def insert_one(self, body):
        try:
            collection = self.get_collection()
            return collection.insert_one(body)
        except Exception as err:
            print(f'Erro ao inserir no banco de dados: {err}')
            return False

    def update_one(self, id, body, collection='winery'):
        try:
            collection = self.get_collection(collection)

            collection.find_one_and_update(
                {"_id": id},
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
            if res.deleted_count == 1:
                print(f'mensagem {identifier} removida com sucesso')
            else:
                print(f'Erro ao remover a mensagem {identifier}:'
                      ' nenhuma mensagem encontrada para o id')
        except Exception as err:
            print(f'Erro ao deletar no banco de dados: {err}')

    def get_one(self, identifier, collection='winery'):
        collection = self.get_collection(collection)
        document = collection.find_one({"id": identifier})
        return document
