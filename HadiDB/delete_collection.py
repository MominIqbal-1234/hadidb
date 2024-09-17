from HadiDB.paths import Path
from HadiDB.hash import HASH
from HadiDB.engine import FileHandler
import os
import shutil


class DeleteCollection:
    def __init__(self,database:str,collection:str) -> None:
        self.collection = collection
        self.database = database
        self.__collection = collection
        self.__database = database
    def delete(self):
        try:

            collection_path = Path(self.database,self.collection).db_full_path
            
            collection_path_manage = Path(self.database,self.collection).db_full_path_json
            read_manage = FileHandler(collection_path_manage).read()

            collection = read_manage.get('collection',None)
            working_file = read_manage.get('working_file',None)
            reference_value = read_manage.get('reference_value',None)
            delete_count = read_manage.get('delete_count',None)

            if collection != None and collection != []:
                collection[0].pop(self.__collection)
            if working_file != None and working_file != []:

                working_file[0].pop(self.__collection)
            if reference_value != None and reference_value != []:

                reference_value[0].pop(self.__collection)
            # if delete_count != None and delete_count != []:

            #     delete_count[0].pop(self.__collection)

            shutil.rmtree(collection_path)
            FileHandler(collection_path_manage).write(read_manage)
            return {
                    "status":200,
                    "message":f"{self.__collection} Collection delete successful"
                }
        except:
            return {
                    "status":404,
                    "message":f"{self.__collection} Collection Not Found"
                }
        

