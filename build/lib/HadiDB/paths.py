import os
from HadiDB.hash import HASH

class Path:
    def __init__(self,database:str=None,collection:str=None) -> None:
        

        ParentFolder = HASH(".Hadi").encode()
        authFile = HASH(".auth").encode()
        manageFile = HASH(".manage").encode()
        Bin = HASH(".bin").encode()
        

        self.bin_full_path = os.path.join(ParentFolder,Bin)
        self.auth_File = os.path.join(ParentFolder,Bin,f"{authFile}.json")
        self.manage_File_bin = os.path.join(ParentFolder,Bin,f"{manageFile}.json")
        if database != None:
            self.__database = HASH(database).encode()
            self.manage_File = os.path.join(ParentFolder,self.__database,f"{manageFile}.json")
            self.manage_path_File = os.path.join(ParentFolder,self.__database)
        if database != None and collection != None:
            self.__collection = HASH(collection).encode()
            self.__database = HASH(database).encode()
            self.db_full_path = os.path.join(ParentFolder,self.__database,self.__collection)
            self.db_full_path_json = os.path.join(ParentFolder,self.__database,f"{manageFile}.json")
    