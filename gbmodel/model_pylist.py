"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.services= []

    def select(self):
        """
        Returns services list of lists
        Each list in services contains: [name, description, street_address, type_of_service, phone_number, hours_of_operation, hours_needed 
        :return: List of lists
        """
        return self.services

    def insert(self, name, description, street_address, type_of_service, phone_number, hours_of_operation, hours_needed):
        """
        Appends a new list of values representing new service into services
        :param name: String
        :param description: String
        :param street_address: String
        :param type_of_service: String
        :param phone_number: String
        :param hours_of_operation: String
        :param hours_needed: Integer
        :return: True
        """
        params = [name, description, street_address, type_of_service, phone_number, hours_of_operation, hours_needed]
        self.services.append(params)
        return True
