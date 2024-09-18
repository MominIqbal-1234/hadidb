import hashlib

class HASH:
    def __init__(self,data:str) -> None:
        self.data = str(data)

    def encode(self):
        return hashlib.sha512(self.data.encode('utf-8')).hexdigest()
        


