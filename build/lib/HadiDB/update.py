from HadiDB.paths import Path
from HadiDB.auth import Auth
from HadiDB.schema import arrangeData
from HadiDB.engine import FileHandler
from HadiDB.hash import HASH
from HadiDB.getbyID import GetByID
from HadiDB.haditechnique import HadiTechnique
import os
import itertools


class Update:
    def __init__(self,
                username:str,
                password:str,
                database:str,
                collection:str,
                objectid:int,
                data:dict
                 ) -> None:
        self.__id = objectid
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
        self.__message = "DB something Wrong"

        self.__data = data
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path
        self.__manage_File = Path(self.__database,self.__collection).manage_File
        self.__manage_json_file_data = FileHandler(self.__manage_File).read() 
        



    def __is_collection_exist(self):
        if self.__manage_json_file_data.get('collection') == []:
            return 404
        elif self.__manage_json_file_data.get('collection')[0].get(self.__collection) == None:
            return 404
        else:
            return 200



    def update(self):
        if Auth(self.__username,self.__password)._Authenticate() == None:
            return {
                "status":401,
                "message":"Wrong Username Password"
            }

        if self.__is_collection_exist() == 200:
            
            
            self.__schema = self.__manage_json_file_data.get('collection')[0].get(self.__collection)[0]

            validate_schema = self.__data.keys() == self.__schema.keys()

            if validate_schema == True:
                
                arrange_data = (arrangeData(self.__schema,self.__data))
                self.working_file = self.__manage_json_file_data.get('working_file')[0].get(self.__collection)[0]
                fileName = HadiTechnique(self.__id).map_number_to_range()
                
                self.actual_data_file_path = os.path.join(self.__db_full_path,f"{HASH(fileName).encode()}.json")
                
                self.get_actual_data = FileHandler(self.actual_data_file_path).read()
                

                if self.get_actual_data['data'] == []:
                    return {
                        "status":404,
                        "message":"collection is Empty"
                    }

                
                if self.get_actual_data['data'][0].get(str(self.__id)) == None:
                    return {
                        "status":404,
                        "message":"ID not Exist"
                    }

                

                
                if self.__update_unique_values()['status'] == 200:
                    arrange_data['id'] = self.__id
                    self.get_actual_data['data'][0].get(f"{self.__id}").update(arrange_data)
                    
                    FileHandler(self.actual_data_file_path).write(self.get_actual_data)
                    
                    return {
                        "status":200,
                        "message":"Data Update successfully",
                        "data":arrange_data
                    }

                else:
                    return {
                        "status":409,
                        "message": self.__message
                    }
            else:
                return {
                    "status":404,
                    "message":"Invalid Schema missmatch key"
                }
        else:
            return {
                "status":404,
                "message":"collection not found"
            }


    def __update_unique_values(self):
        self.__cache_data = []
        self.__count = 0
        for key,value in self.__schema.items():
            if value == "Unique":
                self.__count = self.__count + 1
                __key = HASH(key).encode()
                self.folder_path = os.path.join(self.__db_full_path,__key)
                
                files = [file[:-5] for file in os.listdir(self.folder_path) if file.endswith('.json')]
                
                get_actual_key_value = self.get_actual_data['data'][0].get(str(self.__id))[key]
                
                for filename in itertools.islice(files,len(files)):

            
                    
                    self.filepath_unique = os.path.join(self.__db_full_path,__key,f"{filename}.json")
                    self.unique_file_data = FileHandler(self.filepath_unique).read()

                
                    if bool(self.unique_file_data['data'][0].get(self.__data.get(key,None))) == True:
                        self.__message = f" {key} Already Available"
                        return {
                            "status":409
                        }


                    try:

                        del self.unique_file_data['data'][0][get_actual_key_value]
                        self.unique_file_data['data'][0][self.__data.get(key)] = self.__id
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
                
                files = [file[:-5] for file in os.listdir(self.folder_path) if file.endswith('.json')]
                get_actual_key_value = self.get_actual_data['data'][0].get(str(self.__id))[key]
                
                for filename in itertools.islice(files,len(files)):

                    self.filepath_text = os.path.join(self.__db_full_path,__key,f"{filename}.json")
                    
                    self.no_unique_file_data = FileHandler(self.filepath_text).read()

                    
                    
                    for item in itertools.islice(self.no_unique_file_data['data'] ,len(self.no_unique_file_data['data'])):
                        if item[0] == get_actual_key_value:
                            index = self.no_unique_file_data['data'].index(item)
                            
                            self.no_unique_file_data['data'].pop(int(index))
                            
                    
                            self.no_unique_file_data['data'].append([self.__data[key],self.__id])
                

                            self.__cache_data.append({
                                    
                                        "filepath":self.filepath_text,
                                        "data":self.no_unique_file_data
                                    
                                })
                        else:
                            pass

                        
        if len(self.count_unique_vlaues()) == len(self.__cache_data):
            for i in self.__cache_data:
                FileHandler(i['filepath']).write(i['data'])

        else:
            return {"status":404}


        return {
            "status":200
        }


    def count_unique_vlaues(self):
        self.total_keys = []
        for value in self.__schema.values():
            if value == "Unique" or value == "Text":
                self.total_keys.append(value)
        return self.total_keys