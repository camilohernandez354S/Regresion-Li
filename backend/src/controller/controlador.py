from model.db_connector import MongoDBInsertion, MongoDBConnection
from model.data_cleaner import DataCleaner
from view.vista import DataViewer

class PropertyController:
    """
    Controlador encargado de gestionar la lógica entre el modelo y la vista.
    """

    def __init__(self):
        """
        Inicializa el controlador.
        """
        self.db_connection = MongoDBConnection()
        self.db_insertion = MongoDBInsertion(self.db_connection)
        self.data_viewer = DataViewer()

    def load_and_clean_data(self, data):
        """
        Carga, limpia e inserta los datos en MongoDB.

        Args:
            data (list): Datos a cargar e insertar.
        """
        cleaned_data = DataCleaner.clean_data(data)
        self.db_insertion.insert_data(cleaned_data.to_dict(orient="records"))

    def show_data(self):
        """
        Muestra los datos almacenados en la base de datos.
        """
        data = list(self.db_connection.get_collection().find())
        self.data_viewer.display_table(data)
