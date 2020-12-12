from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import os

"""
Gets the services from database.
"""
class Service(MethodView):
    def get(self):
        """
        Accepts GET request and renders the services.
        """
        model = gbmodel.get_model()
        services = [
                dict(name=row[0], 
                    description=row[1], 
                    street_address=row[2], 
                    city=row[3], 
                    state=row[4], 
                    zipcode=row[5], 
                    phone_number=row[6], 
                    hours_of_operation=row[7], 
                    hours_needed=row[8], 
                    lat=row[9], 
                    lng=row[10], 
                    place_id=row[11] ) for row in model.select_service()]
        
        return render_template('service.html', services=services)
