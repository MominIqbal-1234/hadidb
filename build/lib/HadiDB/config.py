from HadiDB.paths import Path
from HadiDB.engine import FileHandler


class Config:

    def __init__(self,database:str=None,collection:str=None) -> None:
        self.collection = collection
        self.__database = database

    def getallcollection(self):
        collection = []
        self.manage_file = Path(self.__database).manage_File
        all_collection = FileHandler(self.manage_file).read()['collection'][0]
        for key,value in all_collection.items():
            collection.append(key)
        return collection
    
    def getalldatabase(self):
        database = []
        self.manage_File_bin = Path().manage_File_bin
        all_database = FileHandler(self.manage_File_bin).read()['database']
        for key in all_database:
            database.append(key)
        return database

    def getschema(self):
        self.manage_file = Path(self.__database).manage_File
        return FileHandler(self.manage_file).read()['collection'][0].get(self.collection)
        
        