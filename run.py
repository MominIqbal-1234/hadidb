from HadiDB.operation import Operation

username = "admin"
password = "admin"
database = "mefiz.com"
collection = "authUser"


db = Operation(username,password,database,collection)



result = db.delete(1)
print(result)