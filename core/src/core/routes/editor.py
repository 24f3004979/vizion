'''
Universal routing service for the editor interface

With editing, fetch, and update routers connections
'''
from fastapi import APIRouter 
from core.service import Data
from core.service.Data import DataModel

# temporary fixing
df = DataModel(dataset='/home/madhav/workstation/Lab/DataSet/titanic.csv')


editor_route = APIRouter(prefix='/editor')

@editor_route.get('/data')
def fetch_data():
    data_frame = df.get()
    return {"data": data_frame}

