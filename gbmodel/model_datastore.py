"""
A scalable flask app for listing volunteers, organizations, charities and social services in Portland.

services (name text, description text, street_address text, phone_number text, hours_of_operation text, hours_needed integer);
"""
from .Model import Model
from google.cloud import datastore

def services_from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, email, date, message ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['description'],entity['street_address'],entity['city'],entity['state'],entity['zipcode'],entity['phone_number'],entity['hours_of_operation'],entity['hours_needed'],entity['lat'],entity['lng'],entity['place_id']]

def volunteers_from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, email, date, message ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['expertise'],entity['phone_number'],entity['email'],entity['hours_offered']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-f20-bruh-beyene-bbeyene')

    def select_service(self):
        """
        Gets all rows from the database
        Each row contains: name, description, street_address, city, state, zipcode, phone_number, hours_of_operation, hours_needed 
        :return: List of lists containing all rows of database
        """
        query = self.client.query(kind = 'services')
        entities = list(map(services_from_datastore,query.fetch()))
        return entities

    def select_volunteer(self):
        """
        Gets all rows from the database
        Each row contains: name, expertise, phone_number, email, hours_needed 
        :return: List of lists containing all rows of database
        """
        query = self.client.query(kind = 'volunteers')
        entities = list(map(volunteers_from_datastore,query.fetch()))
        return entities

    def insert_service(self, name, description, street_address, city, state, zipcode, phone_number, hours_of_operation, hours_needed, lat, lng, place_id):
        """
        Inserts service into database
        :param name: String
        :param description: String
        :param street_address: String
        :param city: String
        :param state: String
        :param zipcode: Integer
        :param phone_number: String
        :param hours_of_operation: String
        :param hours_needed: Integer
        :param lat: String
        :param lng: String
        :param place_id: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        key = self.client.key('services')
        service = datastore.Entity(key)
        service.update( {
                            'name':name, 
                            'description':description, 
                            'street_address':street_address, 
                            'city':city, 
                            'state':state, 
                            'zipcode':zipcode, 
                            'phone_number':phone_number, 
                            'hours_of_operation':hours_of_operation, 
                            'hours_needed':hours_needed,
                            'lat':lat,
                            'lng':lng,
                            'place_id':place_id

            })
        self.client.put(service)
        return True

    def insert_volunteer(self, name, expertise, phone_number, email, hours_offered):
        """
        Inserts service into database
        :param name: String
        :param expertise: String
        :param phone_number: String
        :param email: String
        :param hours_needed: Integer
        :return: True
        :raises: Database errors on connection and insertion
        """
        key = self.client.key('volunteers')
        volunteer = datastore.Entity(key)
        volunteer.update( {
                        'name':name, 
                        'expertise':expertise, 
                        'phone_number':phone_number, 
                        'email':email, 
                        'hours_offered':hours_offered
            })
        self.client.put(volunteer)
        return True
