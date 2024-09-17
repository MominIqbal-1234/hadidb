import hashlib

class HadiTechnique:
    def __init__(self,objectID=None) -> None:
        if objectID == None:
            pass
        else:
            self.objectID = int(objectID)
        

    def hash_string(self,stringTohash):
        hasher = hashlib.sha256()
        hasher.update(stringTohash.encode('utf-8'))
        hashed_string = hasher.hexdigest()
        return hashed_string


    def map_number_to_range(self):
        range_start = ((self.objectID - 1) // 1000) * 1000 + 1
        range_end = ((self.objectID - 1) // 1000) * 1000 + 1000
        self.stringTohash = f"{range_start}_{range_end}"
        return self.stringTohash
        
