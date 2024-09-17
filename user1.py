
from HadiDB.operation import Operation,User,Configuration,DatabaseDeletionService
import random
import json



username = "admin"
password = "admin"
database = "mefiz"
collection = "collection_5"

schema = {
    "username":"Unique",
    "password":"Hash",
    "cnic":"Unique",
    "picture":"Image",
    "bio":"Text"
}

# print(Configuration().get_database())
# print(Configuration(database,collection).get_schema())

update_data = {

         
        "username": "momin_3_again",
        "password": "12345",
        "cnic": "563204028533_3_again",
        "picture": "user/image/1.jpg",
        "bio": "I am python_3_again"
    
    }
# for i in range(1,105):
for i in range(1,2):


    data = {

        "password":"12345",
        "username":f"momin3{random.randint(1,12345678)}",
        # "username":f"momin3",
        # "username":f"momin3",
        # "cnic":f"36302",
        "cnic":f"{random.randint(1,1234567890)}",
        "picture":"user/image/1.jpg",
        "bio":f"I am python {random.randint(1,1234567890)}"
        # "bio":f"I am python"
    }
 

    
    db = Operation(username,password,database,collection)


    # a = User("admin","admin")
    # a.createUser()

    # result = db.create_database(schema)
    result = db.insert(data)
    # result = db.update(2008,update_data)
    # result = db.delete(2006)
    # result = db.getbyID(2007)
    # result = db.getAll()
    # result = db.count()
    # result = db.countbyAll()
    # result = db.getbykey({
    #     #  "bio":"I am python",
    #      "username":"momin37778191"
    # })
    # result = db.getbykeyCount({
    #     # "bio":"I am python 8853510",
    #     "username":"momin37778191"
    # })

    # result = db.getbykeys({
    #     "username":"momin31595754",
    #     # "password":"12345",
    #     "cnic":"124083897",
    #     # "bio":"I am python 407876268"
    # })

 




    print(result)


# for i in range(1,2):





# import time


# db = Operation(username,password,database,collection)
# s = time.time()
# # result = db.getbykeys({
# #         "username":"momin31133080",
# #         "password":"12345",
# #         "cnic":"210431913"
# #     })

# # result = db.getbyID(1)


# e = time.time()
# print(e-s)
# print(result)


# result = DatabaseDeletionService(username,password,database,collection).deleteCollection()
# # result = DatabaseDeletionService(username,password,database,collection).deleteDatabase()
# print(result)