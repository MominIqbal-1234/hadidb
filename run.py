from HadiDB.operation import Configuration

database = "mefiz.com"
collection = "authUser"
from HadiDB.operation import Configuration

print(Configuration().get_database())
print(Configuration(database,collection).get_schema())