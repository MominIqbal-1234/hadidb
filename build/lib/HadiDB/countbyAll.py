
from HadiDB.paths import Path
from HadiDB.engine import FileHandler


class CountByAll:
    def __init__(self,database,collection) -> None:
        self.__database = database
        self.__collection = collection
        self.manage_File = Path(self.__database,self.__collection).manage_File
        self.manageFile = FileHandler(self.manage_File).read()



    def get(self):
        
        working_file = self.manageFile['working_file'][0].get(self.__collection)
        delete_count = self.manageFile['delete_count'][0].get(self.__collection)
        
        if working_file != None and delete_count != None:
            total_count = int(working_file[0]['ID']) - int(delete_count)
            return {
                "status":200,
                "total_count":total_count
            }
            
