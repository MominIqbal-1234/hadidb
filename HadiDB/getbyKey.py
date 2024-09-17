from HadiDB.paths import Path
from HadiDB.engine import FileHandler
from HadiDB.operation import GetByID
from HadiDB.hash import HASH
import os
import itertools


class GetByKey:
    def __init__(self,
                username:str,
                password:str,
                database:str,
                collection:str,
                data:dict,
                 ) -> None:
        self.__data = data
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection

        
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path
        self.get_data = GetByID(self.__username,self.__password,self.__database,self.__collection)
        
        



    def get(self):
    
        values = []
        __key = HASH(list(self.__data.keys())[0]).encode()
        self.full_file_path = os.path.join(self.__db_full_path,__key)
        

        if os.path.exists(self.full_file_path) == False:
            return {
                "status":404,
                "message":"Key Not Found"
            }
    
        files = os.listdir(self.full_file_path)
        
        
        for file in itertools.islice(files, len(files)):
            
            filedata = FileHandler(
                os.path.join(self.full_file_path,file)
            ).read()
            try:
                
                for item in itertools.islice(filedata['data'], len(filedata['data'])):
                    if item[0] == list(self.__data.values())[0]:
                        values.append(self.get_data.get(item[1])['data'])
            except:
                
                for item in itertools.islice(filedata['data'], len(filedata['data'])):
                    result = item.get(list(self.__data.values())[0])
                    if result != None:
                        values.append(self.get_data.get(result))

            
        if values != []:
            return values
        else:
            return {
                "status":404,
                "message":"Data not Found"
            }
                


    def count(self):
        values = []
        __key = HASH(list(self.__data.keys())[0]).encode()
        self.full_file_path = os.path.join(self.__db_full_path,__key)
        

        if os.path.exists(self.full_file_path) == False:
            return {
                "status":404,
                "message":"Key Not Found"
            }
    
        files = os.listdir(self.full_file_path)
        
        
        for file in itertools.islice(files, len(files)):
            
            filedata = FileHandler(
                os.path.join(self.full_file_path,file)
            ).read()
            try:
                for item in itertools.islice(filedata['data'], len(filedata['data'])):
                    if item[0] == list(self.__data.values())[0]:
                        
                        values.append(self.get_data.get(item[1])['data'])
            except:
                for item in itertools.islice(filedata['data'], len(filedata['data'])):
                    result = bool(item.get(list(self.__data.values())[0]))
                    if result == True:
                        values.append(1)

            

        return len(values)
            
                
               