from setuptools import setup, find_packages



VERSION = '0.1.1'
DESCRIPTION = "HadiDB is a lightweight, extremely horizontally scalable database written in Python."


# Setting up
setup(
    name="HadiDB",
    version=VERSION,
    author="mominiqbal1234",
    author_email="<mominiqbal1214@gmail.com>",
    description=DESCRIPTION,
    long_description="""
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
##### Result:

```josn
{'status': 200, 'message': 'Database user Created'}
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

username = "admin"
password = "admin"
database = "mefiz.com"
collection = "authUser"


db = Operation(username,password,database,collection)

data = {
    "username":"hadidb",
    "password":"12345",
    "cnic":"123232442",
    "picture":"user/my/hadidb.jpg",
    "bio":"HadiDB is the Best ;)"
}


result = db.insert(data)
print(result)
```
##### Result:
```json
{
'status': 200, 
'message': 'Data insert successfully',
'data': {
    'username': 'hadidb', 
    'password': '12345', 
    'cnic': '123232442', 
    'picture': 'user/my/hadidb.jpg', 
    'bio': 'HadiDB is the Best ;)',
     'id': 1
     }
}


```

## Update Data
Update Data `db.update(1, update_data)` updates the record with the ID `1` in the database using the provided `update_data`.
```python
from HadiDB.operation import Operation

username = "admin"
password = "admin"
database = "mefiz.com"
collection = "authUser"


db = Operation(username,password,database,collection)


update_data = {     
    "username": "hadidb_update",
    "password": "123455",
    "cnic": "1232324423",
    "picture": "user/my/hadidb1.jpg",
    "bio": "HadiDB is the Best ;) update bio" 
}

result = db.update(1,update_data)
print(result)
```
##### Result:
```json
{
    'status': 200, 
    'message': 'Data Update successfully',
    'data': {
    'username': 'hadidb_update', 
    'password': '123455', 
    'cnic': '1232324423', 
    'picture': 'user/my/hadidb1.jpg', 
    'bio': 'HadiDB is the Best ;) update bio', 
    'id': 1
    }
}
```


## GetByID
The unique identifier (ID) of the document you want to retrieve specific object or an error if the document does not exist.

```python
result = db.getbyID(1)
print(result)
```

## Get All Object
The `getAll` method retrieves all documents from the specified collection in the database.
```python
result = db.getAll()
print(result)
```

## GetByKey
The `getbykey` method retrieves all documents from the database where the specified key-value pair matches. `Not Support multi keys values pairs`
```python
result = db.getbykey({
    "username":"momin"
 })
print(result)
```

## GetByKeys

The getbykeys function uses an implicit `AND (&&)`operation. Both conditions `Example (cnic and bio)` if matched key values in the database then return the matched object.

```python
result = db.getbykeys({
    "cnic":"123232442",
    "bio":"HadiDB is the Best ;) update bio"
})
print(result)
```


## Count 
The `count` method returns the total number of documents (or objects) present in the specified collection in the database.

```python
result = db.count()
print(result)
```
##### Result:
```json
{'status': 200, 'count': 1}
```

## GeyByKeyCount
The `getbykeyCount` method counts the number of documents in the collection where the specified key-value pair matches.
```python
result = db.getbykeyCount({
    "username":"momin"
    })
```




## Delete 
Deletes a document from the database by its unique identifier (`id`)

```python
result = db.delete(1)
print(result)
```
##### Reuslt:
```json
{'status': 200, 'message': 'data delete successful'}
```


## Get All Database 
Retrieves all available databases by using the `get_database()` method of the `Configuration` class
```python
from HadiDB.operation import Configuration

print(Configuration().get_database())
```
## Get All Collection
Retrieves all collections from a specific database using the `get_collection() ` method of the `Configuration` class.

```python
from HadiDB.operation import Configuration

database = "mefiz.com"
print(Configuration(database).get_collection())
```
## Get Schema of Specfic Collection
Return Schema of a specific collection by using ` get_schema() `method from the `Configuration` class.
```python
from HadiDB.operation import Configuration
database = "mefiz.com"
collection = "authUser"
print(Configuration(database,collection).get_schema())
```



## Delete Collection
Deletes a specific collection from a database using the `deleteCollection()` method of the `DatabaseDeletionService` class.
```python
from HadiDB.operation import DatabaseDeletionService

db = DatabaseDeletionService(username,password,database,collection)
print(db.deleteCollection())
```
## Delete Database 
Deletes Database using the `deleteDatabase()` method of the `DatabaseDeletionService` class.
```python
from HadiDB.operation import DatabaseDeletionService

db = DatabaseDeletionService(username,password,database,collection)
print(db.deleteDatabase())
```

##### GitHub : https://github.com/MominIqbal-1234/hadidb
##### Check Our Site : https://mefiz.com/about </br>
##### Developed by : Momin Iqbal

    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["filelock"],
    keywords=['python','pyjsondb''python database', 'hadidb', 'python hadidb','hadidb django'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)