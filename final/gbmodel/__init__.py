# set GCP's Datastore as the database

model_backend = 'datastore'
from .model_datastore import model

appmodel = model()

def get_model():
    return appmodel
