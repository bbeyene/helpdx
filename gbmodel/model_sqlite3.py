"""
A scalable flask app for listing volunteers, organizations, charities and social services in Portland.

services (name text, description text, street_address text, phone_number text, hours_of_operation text, hours_needed integer);
"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'helpdx.db'    # file for Database

class model(Model):
    def __init__(self):
        # Make sure database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from services")
        except sqlite3.OperationalError:
            cursor.execute(
                    """
                    create table services(
                    name text, 
                    description text, 
                    street_address text, 
                    phone_number text, 
                    hours_of_operation text, 
                    hours_needed integer)
                    """);
        try:
            cursor.execute("select count(rowid) from volunteers")
        except sqlite3.OperationalError:
            cursor.execute(
                    """
                    create table volunteers(
                    name text, 
                    expertise text, 
                    phone_number text, 
                    email text, 
                    hours_offered integer)
                    """);
        cursor.close()

    def select_service(self):
        """
        Gets all rows from the database
        Each row contains: name, description, street_address, phone_number, hours_of_operation, hours_needed 
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM services")
        return cursor.fetchall()

    def insert_service(self, name, description, street_address, phone_number, hours_of_operation, hours_needed):
        """
        Inserts service into database
        :param name: String
        :param description: String
        :param street_address: String
        :param phone_number: String
        :param hours_of_operation: String
        :param hours_needed: Integer
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {
                    'name':name, 
                    'description':description, 
                    'street_address':street_address, 
                    'phone_number':phone_number, 
                    'hours_of_operation':hours_of_operation, 
                    'hours_needed':hours_needed
                }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
                """
                insert into services (
                    name, 
                    description, 
                    street_address, 
                    phone_number, 
                    hours_of_operation, 
                    hours_needed) VALUES (
                        :name, 
                        :description, 
                        :street_address, 
                        :phone_number, 
                        :hours_of_operation, 
                        :hours_needed)
                """, params)

        connection.commit()
        cursor.close()
        return True

    def select_volunteer(self):
        """
        Gets all rows from the database
        Each row contains: name, expertise, phone_number, email, hours_needed 
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM volunteers")
        return cursor.fetchall()

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
        params = {
                    'name':name, 
                    'expertise':expertise, 
                    'phone_number':phone_number, 
                    'email':email, 
                    'hours_offered':hours_offered
                }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
                """
                insert into volunteers(
                    name, 
                    expertise, 
                    phone_number, 
                    email, 
                    hours_offered) VALUES (
                        :name, 
                        :expertise, 
                        :phone_number, 
                        :email, 
                        :hours_offered)
                """, params)

        connection.commit()
        cursor.close()
        return True
