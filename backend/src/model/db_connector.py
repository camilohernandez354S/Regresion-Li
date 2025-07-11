import pymongo
import os
from dotenv import load_dotenv
from pymongo.errors import PyMongoError

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class MongoDBConnection:
    """
    Clase encargada de establecer la conexión con MongoDB.
    """
    def __init__(self):
        """
        Inicializa la conexión con MongoDB utilizando las variables de entorno.
        """
        self.client = None
        self.db = None
        self.collection = None
        
        try:
            # Verificar que las variables de entorno estén cargadas correctamente
            mongo_uri = os.getenv("MONGO_URI")
            db_name = os.getenv("DB_NAME")
            collection_name = os.getenv("COLLECTION_NAME")

            if not mongo_uri or not db_name or not collection_name:
                raise ValueError("Faltan variables de entorno para la conexión a MongoDB.")
            
            # Establecer la conexión con MongoDB
            self.client = pymongo.MongoClient(mongo_uri)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
            print("Conexión exitosa a MongoDB.")
        
        except ConnectionError as e:
            print(f"Error al conectar a MongoDB: {e}")
        except ValueError as e:
            print(f"Error de configuración: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def get_collection(self):
        """
        Devuelve la colección de MongoDB a la que se está conectado.
        """
        if  self.collection is None:
            print("No se ha establecido conexión con la colección.")
            return None
        return self.collection


class MongoDBInsertion:
    """
    Clase encargada de insertar datos en MongoDB después de verificar duplicados.
    """
    def __init__(self, collection):
        """
        Inicializa la clase de inserción con una colección específica de MongoDB.
        
        Args:
            collection: Colección de MongoDB a la que se insertarán los datos.
        """
        self.collection = collection

    def insert_data(self, data):
        """
        Inserta los datos en MongoDB si no existen duplicados basados en 'descripcion', 'precio' y 'area'.
        
        Args:
            data (list): Datos a insertar en MongoDB.
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
            else:
                print("Faltan campos ('descripcion', 'precio', 'area') en el documento.")
