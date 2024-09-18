# HadiDB
HadiDB is a lightweight, extremely horizontally scalable database written in Python

# How to install hadidb

```python
pip install hadidb
```

## Create User HadiDB
Creates a new user with the `example` username  `admin` and `example` password `admin` using `createUser()`. It then authenticates the same user by calling the `authentication()` method. 

```python
from HadiDB.operation import User
user = User("admin", "admin")
user.createUser() # Creating a new user in the HadiDB
user.authentication() # Authenticating the HadiDB user
```


## Create Databse , Collection and Schema
This code sets up user credentials and a schema for a database collection. It initializes a database operation using the `Operation` class with the specified `username`, `password`, `database`, and `collection`. Finally, it inserts the provided `data` into the collection and stores the result.

```python
from HadiDB.operation import Operation

username = "admin"
password = "admin"
database = "mefiz.com"
collection = "authUser"

schema = {
    "username":"Unique",
    "password":"Hash",
    "cnic":"Unique",
    "picture":"Image",
    "bio":"Text"
}
db = Operation(username,password,database,collection)
db.create_database(schema)
```
## Insert Data
Insert Data into the Collection use `db.insert(data)` inserts the `data` into the specified database collection.
```python
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
```
## Update Data
Update Data `db.update(1, update_data)` updates the record with the ID `1` in the database using the provided `update_data`.
```python
from HadiDB.operation import Operation

db = Operation(username,password,database,collection)


update_data = {     
    "username": "hadidb_update",
    "password": "123455",
    "cnic": "1232324423",
    "picture": "user/my/hadidb1.jpg",
    "bio": "HadiDB is the Best ;) update bio" 
}

result = db.update(1,update_data)
```

## Delete 
Deletes a document from the database by its unique identifier (`id`)

```python
result = db.delete(1)
```

## GetByID
The unique identifier (ID) of the document you want to retrieve specific object or an error if the document does not exist.

```python
result = db.getbyID(1)
```

## Get All Object
The `getAll` method retrieves all documents from the specified collection in the database.
```python
result = db.getAll()
```
## Count 
The `count` method returns the total number of documents (or objects) present in the specified collection in the database.

```python
result = db.count()
```
## GetByKey
The `getbykey` method retrieves all documents from the database where the specified key-value pair matches. `Not Support multi keys values pairs`
```python
result = db.getbykey({
    "username":"momin"
 })

```

## GeyByKeyCount
The `getbykeyCount` method counts the number of documents in the collection where the specified key-value pair matches.
```python
result = db.getbykeyCount({
    "username":"momin"
    })
```

# Documentation
open Github repository for the WebRaft Python library. The link is included in the package's documentation to provide
users with access to the source code and additional information about the library.
<br>
https://github.com/MominIqbal-1234/hadidb



Check Our Site : https://mefiz.com/about </br>
Developed by : Momin Iqbal
