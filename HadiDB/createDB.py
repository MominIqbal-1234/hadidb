from HadiDB.hash import HASH
from HadiDB.paths import Path
from HadiDB.auth import Auth
from HadiDB.engine import FileHandler
from HadiDB.schema import Schema

class Database:
    def __init__(self,
                 username:str,
                 password:str,
                 database:str,
                 collection:str,
                 schema:dict
                 ) -> None:
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
        self.__schema = schema

    def create(self):      

        if type(self.__schema).__name__ != "dict":
            return {
                "message":"pass only dict"
            }

        self.auth_file = Path().auth_File
        self.__manage_File_bin = Path(self.__database).manage_File_bin
        if Auth(self.__username,self.__password)._Authenticate():
            manage_json_bin = FileHandler(self.__manage_File_bin).read()
            if self.__database in manage_json_bin['database']:
                pass
            else:
                manage_json_bin['database'].append(self.__database)
                FileHandler(self.__manage_File_bin).write(manage_json_bin)

            return Schema(self.__schema,self.__database,self.__collection).validate()

            
        else:
            return { "status":401,"message":"Wrong username and password" }
        
    def jsonKeyExists(self,collection,list_of_dicts):
        for rng in range(0,len(list_of_dicts)):
            for key in (list_of_dicts[rng].keys()):
                if collection == key:
                    return True
                else:
                    return False