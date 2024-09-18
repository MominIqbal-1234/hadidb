
from HadiDB.paths import Path
from HadiDB.hash import HASH
from HadiDB.engine import FileHandler
import shutil
import os

class DeleteDatabase:
    def __init__(self,database:str) -> None:
        self.database = database
        self.__database = database

    def delete(self):
        try:

            database_path = Path(self.database).manage_path_File
            manage = Path(self.database).manage_File_bin
            shutil.rmtree(database_path)
            read_manage = FileHandler(manage).read()
            remove_db = read_manage['database']
            remove_db.remove(self.database)
            FileHandler(manage).write(read_manage)
            return {
                "status":200,
                "message":f"{self.__database} Database delete successful"
            }
        except:
            return {
                "status":404,
                "message":f"{self.__database} database not found"
            }