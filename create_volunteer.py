from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

"""
Gets and sets a volunteer from/to database.
"""
class Create_volunteer(MethodView):
    """
    Accepts GET requests and renders the volunteers view.
    """
    def get(self):
        return render_template('create_volunteer.html')

    def post(self):
        """
        Accepts POST requests, and processes volunteer creation from form;
        Redirect to service when completed.
        """
        model = gbmodel.get_model()
        hours_offered = 0
        try:
            hours_offered = int(request.form['hours_offered'])
        except ValueError:
            hours_offered = 1

        model.insert_volunteer(request.form['name'], request.form['expertise'], request.form['phone_number'], request.form['email'], hours_offered)
        return redirect(url_for('volunteer'))
