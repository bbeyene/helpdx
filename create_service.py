from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import os
import requests

"""
Gets and sets a service from/to database.
"""
class Create_service(MethodView):
    def get(self):
        """
        Accepts GET requests and renders the services creation view.
        """
        return render_template('create_service.html')

    def post(self):
        """
        Accepts POST requests, and processes service creation from form;
        Redirect to service when completed.
        """
        model = gbmodel.get_model()
        hours_needed = 0
        try:
            hours_needed = int(request.form['hours_needed'])
        except ValueError:
            hours_needed = 1000

        # fetch address from google
        maps_key = os.environ.get('MAPS_KEY')
        name = request.form['name']
        description = request.form['description']
        street_address = request.form['street_address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        phone_number = request.form['phone_number']
        hours_of_operation = request.form['hours_of_operation']

        address = f'{street_address}, {city}, {state} {zipcode}'
        fetch = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={maps_key}'
        fetched = requests.get(fetch)
        result = fetched.json()

        if result['status'] == 'OK':
            found_address = dict()
            components = dict()
            formatted_address = result['results'][0]['formatted_address']
            lat = result['results'][0]['geometry']['location']['lat']
            lng = result['results'][0]['geometry']['location']['lng']
            place_id = result['results'][0]['place_id']
            for ac in result['results'][0]['address_components']:
                k = ac['types'][0]
                v = ac['short_name']
                components[k] = v
            if 'street_number' in components:
                found_address['street_address'] = components['street_number']
                if 'route' in components:
                    found_address['street_address'] += ' '
                    found_address['street_address'] += components['route']
            if 'locality' in components:
                found_address['city'] = components['locality']
            if 'administrative_area_level_1' in components:
                found_address['state'] = components['administrative_area_level_1']
            if 'postal_code' in components:
                found_address['zipcode'] = components['postal_code']

            if ('street_address' in found_address) and ('city' in found_address) and ('state' in found_address) \
            and (found_address['street_address'].lower() == street_address.lower()) \
            and (found_address['city'].lower() == city.lower()) \
            and (found_address['state'].lower() == state.lower()) \
            and (found_address['zipcode'] == zipcode):
                model.insert_service(name, description, street_address, city, state, zipcode, phone_number, hours_of_operation, hours_needed, lat, lng, place_id)
                return redirect(url_for('service'))
            else:
                errors = f"We found a similar address: {formatted_address}, fix it and try again"
                found_address['street_address'] = street_address
                return render_template('create_service.html', name=name, description=description, address=found_address, \
                        phone_number=phone_number, hours_of_operation=hours_of_operation, hours_needed=hours_needed, errors=errors)

        elif result['status'] == 'ZERO_RESULTS':
            original_address = dict()
            original_address['street_address'] = street_address
            original_address['city'] = city
            original_address['state'] = state
            original_address['zipcode'] = zipcode
            errors = "Use a real address ..."
            return render_template('create_service.html', name=name, description=description, address=original_address, \
                    phone_number=phone_number, hours_of_operation=hours_of_operation, hours_needed=hours_needed, errors=errors)

