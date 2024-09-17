from HadiDB.insert import Insert
from HadiDB.createDB import Database
from HadiDB.getbyID import GetByID
from HadiDB.delete import Delete
from HadiDB.auth import Auth
from HadiDB.update import Update
from HadiDB.config import Config
from HadiDB.get_all_data import GETALLDATA
from HadiDB.getbyKey import GetByKey
from HadiDB.count import Count
from HadiDB.countbyAll import CountByAll
from HadiDB.getbyKeys import GetByKeys
from HadiDB.delete_database import DeleteDatabase
from HadiDB.delete_collection import DeleteCollection
from filelock import FileLock



class User:
    def __init__(self,username,password) -> None:
        self.__username = username
        self.__password = password
        self.lock = FileLock("{}.lock")
    def createUser(self):
        with self.lock:
            return Auth(self.__username,self.__password)._createUser()
            

    def authentication(self):
        return Auth(self.__username,self.__password)._Authenticate()



class Configuration:
    def __init__(self,__database:str=None,__collection:str=None) -> None:
        self.__database = __database
        self.__collection = __collection
    def get_collection(self):
        return Config(self.__database).getallcollection()
    def get_database(self):
        return Config().getalldatabase()

    def get_schema(self):
        return Config(self.__database,self.__collection).getschema()



class DatabaseDeletionService:
    def __init__(self,username,password,database=None,collection=None) -> None:
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
    

    def authentication(self):
        return Auth(self.__username,self.__password)._Authenticate()


    def deleteDatabase(self):
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return DeleteDatabase(self.__database).delete()

    def deleteCollection(self):
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return DeleteCollection(self.__database,self.__collection).delete()

    



class Operation:
    def __init__(self,
            username:str,
            password:str,
            database:str,
            collection:str,
                 ) -> None:
        self.__username = username
        self.__password = password
        self.__database = database
        self.__collection = collection
        self.lock = FileLock("{}.lock")

    def authentication(self):
        return Auth(self.__username,self.__password)._Authenticate()


    def create_database(self,schema:dict=None):
        
        if type(schema).__name__ != "dict":
            return {
                "status":400,
                "message":"pass only dict"
            }
        
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        with self.lock:
            return Database(self.__username,self.__password,self.__database,self.__collection,schema).create()


    def insert(self,data:dict=None):

        if type(data).__name__ != "dict":
            return {
                "status":400,
                "message":"pass only dict"
            }

        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        with self.lock:
            
            return Insert(self.__username,self.__password,self.__database,self.__collection,data).insert()

    def getbyID(self,objectID:int=None):

        if type(objectID).__name__ != "int":
            return {
                "status":400,
                "message":"pass only int"
            }
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return GetByID(self.__username,self.__password,self.__database,self.__collection).get(objectID)

    def update(self,objectID:int=None,data:dict=None):

        
        if type(objectID).__name__ != "int":
            return {
                "status":400,
                "message":"Missing ID"
            }



        if type(data).__name__ != "dict":
            return {
                "status":400,
                "message":"missing dict or pass only wrong data"
            }


        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        with self.lock:
            return Update(self.__username,self.__password,self.__database,self.__collection,objectID,data).update()

    def delete(self,objectID:int=None):

        if type(objectID).__name__ != "int":
            return {
                "status":400,
                "message":"pass only int"
            }


        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        with self.lock:
            return Delete(self.__username,self.__password,self.__database,self.__collection,objectID).delete()

 
    def getAll(self):
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return GETALLDATA(self.__database,self.__collection).getall()


    def getbykey(self,data:dict=None):

        if type(data).__name__ != "dict" or data == {}:
            return {
                "status":400,
                "message":"pass only dict"
            }


        if len(data.items()) > 1:
            return {
                "message":"getbykey Support only single key Multiple keys use getbykeys"
            }

        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return GetByKey(self.__username,self.__password,self.__database,self.__collection,data).get()


    def getbykeyCount(self,data:dict=None):


        if type(data).__name__ != "dict" or data == {}:
            return {
                "status":400,
                "message":"pass only dict"
            }

        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return GetByKey(self.__username,self.__password,self.__database,self.__collection,data).count()



    def count(self):
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return Count(self.__database,self.__collection).get()


    def countbyAll(self):
        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return CountByAll(self.__database,self.__collection).get()
        
    def getbykeys(self,data:dict=None):

        
        if type(data).__name__ != "dict" or data == {}:
            return {
                "status":400,
                "message":"pass only dict"
            }


        if self.authentication() == None:
            return {
                "status":404,
                "message":"wrong username and password"
            }
        return GetByKeys(self.__database,self.__collection).get(data)



 