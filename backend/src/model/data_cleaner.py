import pandas as pd

class DataCleaner:

    @staticmethod
    def clean_description(description):
        """
        Limpia la descripción y corrige los caracteres mal escritos
        """

        if isinstance(description, str):
            description = description.replace('Apartamento cÃ©ntrico', 'Apartamento céntrico')
            description = description.replace('Apartamento econÃ³mico', 'Apartamento económico')
            description = description.replace('Casa con jardÃ­n', 'Casa con jardín')
        return description
    

    @staticmethod
    def clean_data(df):
        """
        Aplica la limpieza de las descripciones en todo el DataFrame
        """

        df['descripcion'] = df['descripcion'].apply(DataCleaner.clean_description)
        return df