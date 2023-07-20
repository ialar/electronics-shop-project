class InstantiateCSVError(Exception):
    """Подкласс исключения при ошибке чтения CSV-файла"""

    def __init__(self, path: str):
        super().__init__(f"Файл {path.split('/')[-1]} поврежден")
