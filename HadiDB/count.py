from HadiDB.paths import Path
from HadiDB.engine import FileHandler
import itertools
import os

class Count:
    def __init__(self,database:str,collection:str) -> None:

        self.__database = database
        self.__collection = collection
        self.db_full_path = Path(self.__database,self.__collection).db_full_path
        
    def get(self):
        try:
            length__all_data = []
            
            listdir =  [file for file in os.listdir(self.db_full_path) if file.endswith('.json')]
            
            # for file in listdir:
            for file in itertools.islice(listdir, len(listdir)):
                
            
                result = FileHandler(
                    os.path.join(self.db_full_path,file)
                ).read()

                length_data = len(result['data'][0])
                
                length__all_data.append(length_data)
                


            
            return {
                "status":200,
                "count":sum(length__all_data)
            }

        except Exception as e:
            
            return {
                "status":404,
                "message":"DB is Empty"
            }