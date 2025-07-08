import pymongo
import os
from dotenv import load_dotenv


load_dotenv()

class MongoDBInsertion:
    def __init__(self):
        """
        Inicializa la conexión a MongoDB y selecciona la base de datos y colección.
        """

        self.client = pymongo.MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("DB_NAME")]
        self.collection = self.db[os.getenv("COLLECTION_NAME")]

    def insert_data(self, data):
        """
        Inserta los datos en MongoDB si no existen duplicados basados en 'descripcion', 'precio' y 'area'.
        """

        for record in data:
            descripcion = record.get('descripcion')
            precio = record.get('precio')
            area = record.get('area')

            if descripcion and precio and area:
                existing_doc = self.collection.find_one({"descripcion": descripcion, "precio": precio, "area": area})

                if not existing_doc:
                    self.collection.insert_one(record)
                    print(f"Documento con descripción '{descripcion}' insertado")
                else: 
                    print(f"Documento con descripción '{descripcion}', precio {precio}, y área {area} ya existe. Omitido")