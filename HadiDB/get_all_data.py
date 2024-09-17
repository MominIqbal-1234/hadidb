

from HadiDB.paths import Path
from HadiDB.engine import FileHandler
import os
import itertools


class GETALLDATA:
    def __init__(self,database:str,collection:str):
        self.__database = database
        self.__collection = collection
        self.db_full_path = Path(self.__database,self.__collection).db_full_path

    def getall(self):
        try:
            all_data = []
            
            listdir =  [file for file in os.listdir(self.db_full_path) if file.endswith('.json')]
            
            
            for file in itertools.islice(listdir, len(listdir)):
                
            
                result = FileHandler(
                    os.path.join(self.db_full_path,file)
                ).read()

                data = list(result['data'][0].values())

                all_data.append(data)


            return all_data
        except Exception as e:
            
            return {
                "status":404,
                "message":"DB is Empty"
            }



