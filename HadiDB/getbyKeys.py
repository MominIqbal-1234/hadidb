

from HadiDB.paths import Path
import os
import itertools
from HadiDB.engine import FileHandler



class GetByKeys:
    def __init__(self,collection,database) -> None:
        self.__collection = collection
        self.__database = database
        self.db_full_path = Path(self.__collection,self.__database).db_full_path


    def get(self, data: dict):
        self.__data = data
        result = []
        
        files = [file for file in os.listdir(self.db_full_path) if file.endswith('.json')]

        for file in itertools.islice(files, len(files)):
            file_path = os.path.join(self.db_full_path, file)
            
            filedata = FileHandler(file_path).read()

            if filedata is not None:
                for record_id, record in itertools.islice(filedata.get('data', [{}])[0].items(),len(filedata.get('data', [{}])[0].items())):
                    if all(record.get(key) == value for key, value in itertools.islice(self.__data.items(),len(self.__data.items()))):
                        result.append(record)
                        
                    else:
                        pass
        if result != []:
            return {
                "status":200,
                "data": result
            }           
        else:
            return {
                "status":404,
                "message":"Data not found"
            }
