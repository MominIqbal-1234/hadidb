from HadiDB.operation import Operation

db = Operation(username,password,database,collection)

data = {
    "username":"hadidb",
    "password":"12345",
    "cnic":"123232442",
    "picture":"user/my/hadidb.jpg",
    "bio":"HadiDB is the Best ;)"
}


result = db.insert(data)