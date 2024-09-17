from HadiDB.hash import HASH
from HadiDB.engine import FileHandler
from HadiDB.paths import Path
import os




EMPTY_DATABASE  = {
    "database": [],
    "collection": [],
    "schema": [],
    "working_file": [],
    "uniqueValues": [],
    "delete_count": []
    }

class Auth:
    def __init__(self,username:str , password: str) -> None:
        self.username = HASH(username).encode()
        self.password = HASH(password).encode()
        # ------------------Files --------------------------
    
       
        self.bin_path = Path().bin_full_path
        self.auth_file = Path().auth_File
        self.manage_File_bin = Path().manage_File_bin


    def _createUser(self):
        os.makedirs(self.bin_path, exist_ok=True)


        """========================== Create Auth.json ==========================="""
        FileHandler(self.auth_file).write({
            "username":self.username,
            "password":self.password
        })
        """========================== END Auth.json ==========================="""
        
        """========================== Create Manage.json ==========================="""
        if os.path.exists(self.manage_File_bin):
            pass
        else:
            FileHandler(self.manage_File_bin).write(EMPTY_DATABASE)
            return {
                "status":200,
                "message":"Database user Created"
            }
        """========================== End Manage.json ==========================="""
    def _Authenticate(self):
        user = FileHandler(self.auth_file).read()
        if user.get('username') == self.username and user.get('password') == self.password:
            return {
                "status":200,
                "message":"login successful"
            }
        else:
            return None  


