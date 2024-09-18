from HadiDB.paths import Path
from HadiDB.engine import FileHandler
from HadiDB.auth import Auth
from HadiDB.hash import HASH
from HadiDB.haditechnique import HadiTechnique
import os
import itertools


class Delete:
    def __init__(self,
                username:str,
                password:str,
                database:str,
                collection:str,
                objectid:int,
                 ) -> None:
        self.__id = objectid
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection

        
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path
        self.__manage_File = Path(self.__database,self.__collection).manage_File
        self.__manage_json_file_data = FileHandler(self.__manage_File).read() 
        self.__delete_count = self.__manage_json_file_data.get('delete_count')



    def __is_collection_exist(self):
        if self.__manage_json_file_data.get('collection') == []:
            return 404
        elif self.__manage_json_file_data.get('collection')[0].get(self.__collection) == None:
            return 404
        else:
            return 200



    def delete(self):
        if Auth(self.__username,self.__password)._Authenticate() == None:
            return {
                "status":401,
                "message":"Wrong Username Password"
            }

        if self.__is_collection_exist() == 200:
            self.__schema = self.__manage_json_file_data.get('collection')[0].get(self.__collection)[0]
            fileName = HadiTechnique(self.__id).map_number_to_range()
            
            
            self.actual_data_file_path = os.path.join(self.__db_full_path,f"{HASH(f'{fileName}').encode()}.json")
            try:
                self.get_actual_data = FileHandler(self.actual_data_file_path).read()
            except:
                return {
                    "status":404,
                    "message":"ID not Found"
                }

               
            if self.get_actual_data['data'][0].get(str(self.__id)) == None:
                return {
                    "status":404,
                    "message":"ID not Found"
                }

            if self.get_actual_data['data'] == []:
                return {
                    "status":404,
                    "message":"collection is Empty"
                }
            
            if self.__delete_unique_values()['status'] == 200:

                if str(self.__id) in self.get_actual_data['data'][0]:
                    del (self.get_actual_data['data'][0][f"{self.__id}"])
                    FileHandler(self.actual_data_file_path).write(self.get_actual_data)

                    if self.__manage_json_file_data.get('delete_count') == []:

                        self.__manage_json_file_data.get('delete_count').append({
                            self.__collection:1
                        })
                    else:
                        
                        if self.__manage_json_file_data.get('delete_count')[0].get(self.__collection) != None:
                            self.__manage_json_file_data.get('delete_count')[0][self.__collection] += 1
                        else:
                            self.__manage_json_file_data.get('delete_count').append({
                            self.__collection:1
                        })
                    

                    FileHandler(self.__manage_File).write(self.__manage_json_file_data) 

                    return {
                        "status":200,
                        "message":"data delete successful"
                    }
        else:
            return {
                        "status":404,
                        "message":"collection not found"
                    }


    def __delete_unique_values(self):
        self.__cache_data = []
        self.__count = 0
        for key,value in self.__schema.items():
            if value == "Unique":
                self.__count = self.__count + 1
                __key = HASH(key).encode()


                self.folder_path = os.path.join(self.__db_full_path,__key)
                # files = os.listdir(self.folder_path)
                files = [file[:-5] for file in os.listdir(self.folder_path) if file.endswith('.json')]
                get_actual_key_value = self.get_actual_data['data'][0].get(str(self.__id))[key]
                
                for filename in itertools.islice(files,len(files)):
                    
                    # self.filepath_unique = os.path.join(self.__db_full_path,__key,f"{HASH(filename).encode()}.json")
                    self.filepath_unique = os.path.join(self.__db_full_path,__key,f"{filename}.json")
                    self.unique_file_data = FileHandler(self.filepath_unique).read()


                    try:
                        
                        # get_actual_key_value = self.get_actual_data['data'][0].get(str(self.__id))[key]
                        
                        del self.unique_file_data['data'][0][get_actual_key_value]
                        self.__cache_data.append({
                                
                                    "filepath":self.filepath_unique,
                                    "data":self.unique_file_data
                                
                            })
                    except:
                        pass


            elif value == "Text":
                self.__count = self.__count + 1
                __key = HASH(key).encode()

                self.folder_path = os.path.join(self.__db_full_path,__key)
                # files = os.listdir(self.folder_path)
                files = [file[:-5] for file in os.listdir(self.folder_path) if file.endswith('.json')]
                get_actual_key_value = self.get_actual_data['data'][0].get(str(self.__id))[key]
                
                for filename in itertools.islice(files,len(files)):
                    
                    # self.filepath_text = os.path.join(self.__db_full_path,__key,f"{HASH(filename).encode()}.json")
                    self.filepath_text = os.path.join(self.__db_full_path,__key,f"{filename}.json")
                    self.no_unique_file_data = FileHandler(self.filepath_text).read()
                
                    for item in itertools.islice(self.no_unique_file_data['data'] ,len(self.no_unique_file_data['data'])):
                        if item[0] == get_actual_key_value:
                            index = self.no_unique_file_data['data'].index(item)
                            
                            self.no_unique_file_data['data'].pop(int(index))
                            
                            self.__cache_data.append({
                                    
                                        "filepath":self.filepath_text,
                                        "data":self.no_unique_file_data
                                    
                                })
                        else:
                            pass



                #
        
        for i in self.__cache_data:
            FileHandler(i['filepath']).write(i['data'])

        


        return {
            "status":200
        }