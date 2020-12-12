class Model():
    def select_service(self):
        """
        Gets all services from the database
        :return: Tuple containing all rows of database
        """
        pass

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
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
    def select_volunteer(self):
        """
        Gets all volunteers from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert_volunteer(self, name, expertise, phone_number, email, hours_offered):
        """
        Inserts service into database
        :param name: String
        :param expertise: String
        :param phone_number: String
        :param email: String
        :param hours_offered: Integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
