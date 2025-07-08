import pymongo
import pandas as pd

class MongoDBConnector:
    def __init__(self, db_name, collection_name, uri="mongodb://localhost:27017/"):
       """
       Inicializa la conexión a MongoDB y selecciona la base de datos y colección
       """
       
       self.client = pymongo.MongoClient(uri)
       self.db = self.client[db_name]
       self.collection = self.db[collection_name]

    def insertar_data_from_dataframe(self, dataframe):
        """
        Inserta los datos de un DataFrame de pandas a la colección de MongoDB
        """

        data_dict = dataframe.to_dict(orient="records")

        self.collection.insert_many(data_dict)
        print("Datos insertados correctamente en MongoDB")

class ExcelToMongo:
    def __init__(self, file_path, db_name, collection_name):
        """
        Inicializa la carga de datos desde un archivo de Excel y la inserción a MongoDB
        """
        self.file_path = file_path
        self.db_name = db_name
        self.collection_name = collection_name
        self.data = self.load_data()
    
    def load_data(self):
        """
        Carga los datos desde un archivo Excel a un Dataframe
        """
        return pd.read_excel(self.file_path)
    
    def insert_data_to_mongo(self):
        """
        Inserta los datos cargados desde el Excel a MongoDB
        """

        db_connector = MongoDBConnector(self.db_name, self.collection_name)
        db_connector.insertar_data_from_dataframe(self.data)


if __name__ == "__main__":

    file_path = r"C:\Users\Kevin Prada\Downloads\dataset_vivienda.xlsx"

    db_name = 'vivienda'
    collection_name = 'propiedades'

    excel_to_mongo = ExcelToMongo(file_path, db_name, collection_name)

    excel_to_mongo.insert_data_to_mongo()
