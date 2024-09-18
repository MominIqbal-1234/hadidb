from HadiDB.haditechnique import HadiTechnique
from HadiDB.engine import FileHandler
from HadiDB.auth import Auth
import os
from HadiDB.paths import Path
from HadiDB.hash import HASH

class GetByID:
    def __init__(self,
                username:str,
                password:str,
                database:str,
                collection:str,
                
                 ) -> None:
        
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path

    def get(self,objectID):
        self.__id = objectID
        if Auth(self.__username,self.__password)._Authenticate() == None:
            return {
                "status":401,
                "message":"Wrong Username Password"
            }
        try:
            filename =  HASH(HadiTechnique(self.__id).map_number_to_range()).encode()
            filepath = os.path.join(self.__db_full_path,f"{filename}.json")
            data = FileHandler(filepath).read()
            if data['data'][0].get(str(self.__id)) == None:
                return {
                    "status":404,
                    "message":"data not found"
                }

            return {
                    "status":200,
                    "message":"Data Found",
                    "data":data['data'][0].get(str(self.__id))   
                }
        except:
            return {
                    "status":404,
                    "message":"data not found"
                }
        


    def get_all_data_file(self):

        if Auth(self.__username,self.__password)._Authenticate() == None:
            return {
                "status":401,
                "message":"Wrong Username Password"
            }

        filename = HASH(HadiTechnique(self.__id).map_number_to_range()).encode()
        filepath = os.path.join(self.__db_full_path,f"{filename}.json")
        data = FileHandler(filepath).read()
        if data['data'][0].get(str(self.__id)) == None:
            return {
                "status":404,
                "message":"data not found"
            }
        return data

