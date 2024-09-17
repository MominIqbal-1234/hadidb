

class Write:
    def __init__(self,manage_file_data:dict,collection_name:str) -> None:

        self.manage_file_data = manage_file_data
        self.collection_name = collection_name

        print(self.manage_file_data['working_file'][0][self.collection_name])

    