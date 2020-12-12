from flask import render_template
from flask.views import MethodView

"""
The landing page.
"""
class Index(MethodView):
    def get(self):
        """
        Accepts GET request and renders landing page.
        """
        return render_template('index.html')

