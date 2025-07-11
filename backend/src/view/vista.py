from tabulate import tabulate

class DataViewer:
    """
    Clase encargada de mostrar los datos a los usuarios.
    """

    @staticmethod
    def display_table(data: list) -> None:
        """
        Muestra los datos en una tabla con formato.

        Args:
            data (list): Datos a mostrar.
        """
        if data:
            print(tabulate(data, headers="keys", tablefmt="pretty"))
        else:
            print("No hay datos disponibles para mostrar.")
