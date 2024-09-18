
from HadiDB.paths import Path
import os
from HadiDB.hash import HASH
from HadiDB.engine import FileHandler
from HadiDB.haditechnique import HadiTechnique




SCHEMARULE = [
    "Text",
    "Hash",
    "Unique",
    "Image"
]


EMPTY_FILE  = {
    "data": []
    }

EMPTY_DATABASE  = {
    "database": [],
    "collection": [],
    "schema": [],
    "working_file": [],
    "reference_value": [],
    "delete_count": []
    }

class Schema:
    def __init__(self,schema:dict,database,collection) -> None:
        self.__schema = schema
        self.__database = database
        self.__collection = collection
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path
        self.__manage_File = Path(self.__database,self.__collection).manage_File
        self.__manage_path_File = Path(self.__database,self.__collection).manage_path_File

        self.__Unique = "Unique"
        self.__Text = "Text"

        os.makedirs(self.__manage_path_File,exist_ok=True)
        if os.path.exists(self.__manage_File):
            pass
        else:
            FileHandler(self.__manage_File).write(EMPTY_DATABASE)


        self.manage_json_data = FileHandler(self.__manage_File).read() 


    def __inital_configration_file(self,filepath:str,writable_data:dict):
        
        if os.path.exists(filepath):
            pass
        else:
            FileHandler(filepath).write(writable_data)


    def __createFile(self,folder_path_save_independent_value:str):
        os.makedirs(folder_path_save_independent_value,exist_ok=True)
        
        

        
        filename = HadiTechnique("1").map_number_to_range()

       
        
        __db_full_path_file = os.path.join(self.__db_full_path,f"{HASH(filename).encode()}.json")
        self.__inital_configration_file(__db_full_path_file,EMPTY_FILE)

        if  self.manage_json_data.get('collection') == []:
            
            self.manage_json_data.get('collection').append(
                {self.__collection:[self.__schema]}
                )

            self.manage_json_data.get('working_file').append(
                {self.__collection:[{
                    "fileName":f"{filename}",
                    "ID":""
                }]}
                )
            
            

        elif self.manage_json_data.get('collection')[0].get(self.__collection) == None:
            self.manage_json_data.get('collection')[0].update(
                {self.__collection:[self.__schema]}
                )
           


        elif self.manage_json_data.get('collection')[0][self.__collection]:
            
            self.manage_json_data['collection'][0].get(self.__collection)[0] = self.__schema
            
          




        if self.manage_json_data.get('working_file')[0].get(self.__collection) == None:

            

            self.manage_json_data.get('working_file')[0].update(
                {self.__collection:[{
                    "fileName":f"{filename}",
                    "ID":""
                }]}
                )



        FileHandler(self.__manage_File).write(self.manage_json_data)
        return 0
     


    def validate(self):
        for key, value in self.__schema.items():
            
            if value not in SCHEMARULE:
                return {
                    "status":401,
                    "message":"Invalid Schema"
                }
            if key == 'id' or key == 'ID' or key == '__id' or key == '__ID':
                
                return {
                    "status":400,
                    "message":"ID NOT Required ( ID Auto Generated )"
                }
            elif "" == value:
            
                return {
                    "status":400,
                    "message":"Empty Value"
                }
            elif self.__Unique == value:
                


                if self.manage_json_data.get('reference_value') == []:
                
                    self.manage_json_data.get('reference_value').append(
                        {self.__collection:[{
                            key:1
                        }]}
                        )
                else:
                    
                    
                    if self.manage_json_data.get('reference_value')[0].get(self.__collection) == None:
                        
                        self.manage_json_data.get('reference_value')[0].update(
                        {self.__collection:[{
                            key:1
                        }]}
                        )
                    

                    elif self.manage_json_data.get('reference_value')[0][self.__collection][0].get(key) != None:
                        pass
                    else:
                        self.manage_json_data.get('reference_value')[0][self.__collection][0][key] = 1
                 


                self.__unique_folder_path = os.path.join(self.__db_full_path,HASH(key).encode())
                self.__createFile(self.__unique_folder_path)

                __unique_folder_path_file = os.path.join(self.__unique_folder_path,f"{HASH('1').encode()}.json")
                self.__inital_configration_file(__unique_folder_path_file,EMPTY_FILE)

            elif self.__Text == value:
                

                if self.manage_json_data.get('reference_value') == []:
                
                    self.manage_json_data.get('reference_value').append(
                        {self.__collection:[{
                            key:1
                        }]}
                        )
                else:
                    if self.manage_json_data.get('reference_value')[0].get(self.__collection) == None:
                        self.manage_json_data.get('reference_value')[0].update(
                        {self.__collection:[{
                            key:1
                        }]}
                        )
                    

                    elif self.manage_json_data.get('reference_value')[0][self.__collection][0].get(key) != None:
                        pass
                    else:
                        self.manage_json_data.get('reference_value')[0][self.__collection][0][key] = 1
                    
                        
                    


                self.__No_unique_folder_path = os.path.join(self.__db_full_path,HASH(key).encode())
                self.__createFile(self.__No_unique_folder_path)

                __No_unique_folder_path_file = os.path.join(self.__No_unique_folder_path,f"{HASH('1').encode()}.json")
                self.__inital_configration_file(__No_unique_folder_path_file,EMPTY_FILE)
                
                
            elif "Hash" == value:
                pass
            elif "Image" == value:
                pass
            
            else:
                return False
        
            

def arrangeData(schema, data):
    arranged_data = {key: data.get(key, None) for key in schema.keys()}
    return arranged_data