
from HadiDB.paths import Path
from HadiDB.engine import FileHandler
from HadiDB.auth import Auth
from HadiDB.schema import arrangeData
import os
from HadiDB.write import Write
from HadiDB.haditechnique import HadiTechnique
from HadiDB.hash import HASH




EMPTY_FILE  = {
    "data": []
    }


class Insert:
    def __init__(self,
            username:str,
            password:str,
            database:str,
            collection:str,
            data:dict
                 ) -> None:
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
        self.__data = data
        self.__db_full_path = Path(self.__database,self.__collection).db_full_path
        self.__manage_File = Path(self.__database,self.__collection).manage_File
        self.__manage_json_file_data = FileHandler(self.__manage_File).read() 

        self.filepath_unique = None
        self.unique_file_data = None
        self.filepath_text = None
        self.no_unique_file_data = None
    

 


    def __is_collection_exist(self):
        if self.__manage_json_file_data.get('collection') == []:
            return 404

        elif self.__manage_json_file_data.get('collection')[0].get(self.__collection) == None:
            return 404
        else:
            return 200


    def __write_working_file_ID_and_validate_unique_vlaues(self):
        
        if self.__manage_json_file_data['working_file'][0][self.__collection][0]['ID'] != '':
            self.__ID =  int(self.__manage_json_file_data['working_file'][0][self.__collection][0]['ID']) + 1
            self.__manage_json_file_data['working_file'][0][self.__collection][0]['ID'] = self.__ID
            
          
        else:
            
            self.__manage_json_file_data['working_file'][0][self.__collection][0]['ID'] = 1
            self.__ID = 1
            
        if self.__write_unique_values().get('status') != 409:
            
           
            return {
                "status":200,
                "filename":HASH(HadiTechnique(self.__ID).map_number_to_range()).encode()
            }
             
        else:
        
            return {
                    "status":409,
                    "error": "Conflict",
                    "message": "Data already exists"
                        }
            

    def count_unique_vlaues(self):
        self.total_keys = []
        for value in self.__schema.values():
            if value == "Unique" or value == "Text":
                self.total_keys.append(value)
        return self.total_keys


    def __write_unique_values(self):
        self.__cache_data = []
        self.__count = 0




        for key,value in self.__schema.items():
            
            self.reference_value = self.__manage_json_file_data['reference_value'][0].get(self.__collection)[0]
            
           



            if value == "Unique":
                
                self.__count = self.__count + 1
                __key = HASH(key).encode()

                

                self.filepath_unique = os.path.join(self.__db_full_path,__key,f"{HASH(str(self.reference_value[key])).encode()}.json")
                self.unique_file_data = FileHandler(self.filepath_unique).read()

               
               
                if self.unique_file_data['data'] != []:
                    if len(self.unique_file_data['data'][0]) >= 1000: # Single Chunk size write the data
                        
                        

                        self.filepath_unique = os.path.join(self.__db_full_path,__key,f"{HASH(int(self.reference_value[key]) + 1).encode()}.json")
                        FileHandler(self.filepath_unique).write(EMPTY_FILE)
                        
                        self.unique_file_data = FileHandler(self.filepath_unique).read()
                        self.reference_value[key] = int(self.reference_value[key]) + 1
                        

            
                       
                
                
                

                


                
                if self.unique_file_data['data'] == []:

                    self.unique_file_data['data'].append({
                        self.__data.get(key):self.__ID
                    })
                    
                    self.__cache_data.append({
                        
                            "filepath":self.filepath_unique,
                            "data":self.unique_file_data
                        
                    })
                    

                    
                    
                else:
                    self.__count = self.__count + 1
                    if bool(self.unique_file_data['data'][0].get(self.__data.get(key,None))) != True:
                        self.unique_file_data['data'][0][self.__data.get(key)] = self.__ID
                        
                        self.__cache_data.append({
                        
                            "filepath":self.filepath_unique,
                            "data":self.unique_file_data
                        
                    })
                       

                    else:
                        
                        return {
                            "status":409,
                            "error": "Conflict",
                            "message": "Data already exists"
                        }
                

            elif value == "Text":
                self.__count = self.__count + 1
                __key = HASH(key).encode()
                self.filepath_text = os.path.join(self.__db_full_path,__key,f"{HASH(int(self.reference_value[key])).encode()}.json")
                self.no_unique_file_data = FileHandler(self.filepath_text).read()



                if self.no_unique_file_data['data'] != []:
                    if len(self.no_unique_file_data['data']) >= 1000:
                        
                        

                        self.filepath_text = os.path.join(self.__db_full_path,__key,f"{HASH(int(self.reference_value[key]) + 1).encode()}.json")
                        FileHandler(self.filepath_text).write(EMPTY_FILE)
                        self.no_unique_file_data = FileHandler(self.filepath_text).read()
                        
                        self.reference_value[key] = int(self.reference_value[key]) + 1
                        
                        




                if self.no_unique_file_data['data'] == []:
                    self.no_unique_file_data['data'].append(
                       
                        [self.__data.get(key),self.__ID]
                        
                    )
                    
                    self.__cache_data.append({
                        
                            "filepath":self.filepath_text,
                            "data":self.no_unique_file_data
                        
                    })
                  
                else:
                    self.__count = self.__count + 1
                    self.no_unique_file_data['data'].append(
                        
                        [self.__data.get(key),self.__ID]
                    )
                    
                    self.__cache_data.append({
                        
                            "filepath":self.filepath_text,
                            "data":self.no_unique_file_data
                        
                    })
                    

            
        if len(self.count_unique_vlaues()) == len(self.__cache_data):
            
            for i in self.__cache_data:
                FileHandler(i['filepath']).write(i['data'])
        else:
            return {"status":404}




        
        return {
            "status":200
        }
                    
                


    def insert(self):
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
                
                filename = self.__write_working_file_ID_and_validate_unique_vlaues()

                if filename['status'] == 409:
                    return {
                            "status":409,
                            "error": "Conflict",
                            "message": "Data already exists"
                        }


                else:
                    arrange_data['id'] = self.__ID
                    

                    filepath = os.path.join(self.__db_full_path,f"{filename['filename']}.json")
                    if os.path.exists(filepath) == False:
                        FileHandler(os.path.join(self.__db_full_path,f"{filename['filename']}.json")).write(
                            {
                                "data":[]
                            }
                        )
                    


                    readFile = FileHandler(os.path.join(self.__db_full_path,f"{filename['filename']}.json"))
                    
                    read_file = readFile.read()

                

                    if read_file['data'] == []:
                        read_file['data'].append({
                            arrange_data.get('id'):arrange_data
                        })


                    else:
                        
                        if len(read_file['data'][0]) >= 1000: # single Chunk size write the data
                            self.__manage_json_file_data.get('working_file')[0].get(self.__collection)[0]['fileName'] = HASH(HadiTechnique(self.__ID).map_number_to_range()).encode()
                            
                            


                        read_file['data'][0].update({
                        arrange_data.get('id'): arrange_data
                        
                    } )

                    

                    FileHandler(self.__manage_File).write(self.__manage_json_file_data)
                    readFile.write(read_file)
                    return {
                        "status":200,
                        "message":"Data insert successfully",
                        "data":arrange_data
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