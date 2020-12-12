from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

"""
Gets the volunteers from database.
"""
class Volunteer(MethodView):
    def get(self):
        """
        Accepts GET request and renders the volunteers.
        """
        model = gbmodel.get_model()
        volunteers = [dict(name=row[0], expertise=row[1], phone_number=row[2], email=row[3], hours_offered=row[4] ) for row in model.select_volunteer()]
        return render_template('volunteer.html', volunteers=volunteers)
