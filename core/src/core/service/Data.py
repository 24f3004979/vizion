import pandas as pd

from core.schema.editor_schema import EditRequest
from core.schema.editor_schema import FetchRequest

from core.schema.exceptions import WrongLocation


'''
Data Model
features
1. Version df changes
2. fetch information
'''

class DataModel:
    """
    Simple data frame abstraction with version storing
    and managing dataframe instances
    """
    
    def __init__(self, dataset:str):
        self.DF: pd.DataFrame = pd.read_csv(dataset)
        
        self.versions = []
        # Root version initiated
        self.versions.append(self.DF)

    def get(self):
        '''
        Returning the original data frame
        INFO: Needs to be worked on to make it real statefull
        '''
        return self.DF.to_json()

    def fetch(self, fetch:FetchRequest):
        location = fetch.location
        try:
            info = self.DF.loc[location]
            return info
        except KeyError as e:
            raise WrongLocation("Fetch Faild with wrong location problem")

    def edit(self, request:EditRequest):
        """
        store changes
        build the new changed df and return it
        """
        
        # edit the df
        location = request.location
        edit = request.content
        try:
            self.DF.loc[location] = edit

            # Into node about data state
            self.versions.append(EditRequest)
        except KeyError as e:
            raise WrongLocation("Wrong location given for editing")
