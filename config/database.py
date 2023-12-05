from pymongo import MongoClient

class DataBase:
    __conexion: object = MongoClient("mongodb://localhost:27017/").dbfastapimongodb
    
    def get_conexion(self) -> object:
        return self.__conexion
