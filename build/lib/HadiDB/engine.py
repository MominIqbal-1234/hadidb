import io
import json
import os
import gzip

class FileHandler1:
    def __init__(self, filepath:str, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self._object_read = None
        self._object_write = None

    def write(self,content:dict):
        
        temp_file_path = self.filepath + "_temp.json"
        
        self._object_write = io.open(temp_file_path, 'w', encoding=self.encoding)
        json.dump(content, self._object_write, indent=4)
        self._object_write.close()
        os.replace(temp_file_path, self.filepath)

        return None


    def read(self):

        self._object_read = io.open(self.filepath, 'r', encoding=self.encoding)
        data =  json.load(self._object_read)
        self._object_read.close()
        return data




class FileHandler:
    def __init__(self, filepath: str, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self._object_read = None
        self._object_write = None

    def write(self, content: dict):
        try:
            temp_file_path = self.filepath + "_temp.json"
        
            with gzip.open(temp_file_path, 'wt', encoding=self.encoding) as self._object_write:
                json.dump(content, self._object_write, indent=4)
            os.replace(temp_file_path, self.filepath)
        except:
            return {
                "status":404
            }
            # self._object_write.close()

    def read(self):
        
        try:

            with gzip.open(self.filepath, 'rt', encoding=self.encoding) as self._object_read:
                data = json.load(self._object_read)
            # self._object_read.close()
            return data
        except:
            return {
                "status":404
            }
    



