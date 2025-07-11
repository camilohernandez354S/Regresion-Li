import pandas as pd 
from model.db_connector import MongoDBInsertion
from model.data_cleaner import DataCleaner

class ExcelToMongo:
    def __init__(self, file_path):
        """
        Inicializa la carga de datos desde un archivo de Excel y la inserción a MongoDB
        """
        self.file_path = file_path
        self.data = self.load_data()
    
    def load_data(self): 
        """
        Carga los datos desde un archivo Excel a un DataFrame
        """
        return pd.read_excel(self.file_path)
    
    def insert_data_to_mongo(self):
        """
        Limpia los datos y luego los inserta en MongoDB
        """
        cleaned_data = DataCleaner.clean_data(self.data)
        db_connector = MongoDBInsertion()
        db_connector.insert_data(cleaned_data.to_dict(orient="records"))

if __name__ == "__main__":
    file_path = r"C:\Documentos\trabajos\Programing\todo de codigo\visulal\ADSO_8\Relacion_lineal\dataset_vivienda.xlsx"

    excel_to_mongo = ExcelToMongo(file_path)
    excel_to_mongo.insert_data_to_mongo()